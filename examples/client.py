from pydoc import cli
from switchml.client import Client
import torch
import random
import utils
from torch.utils.data import DataLoader
from collections import OrderedDict


class CifarClient:
    def __init__(self, trainset, testset, device: str, validation_split: int = 0.1):
        self.device = device
        self.trainset = trainset
        self.testset = testset
        self.validation_split = validation_split

    def get_parameters(self):
        model = utils.load_efficientnet(classes=10)
        model_weights = [val.cpu().numpy() for _, val in model.state_dict().items()]
        return model_weights

    def set_parameters(self, parameters):
        """Loads a efficientnet model and replaces it parameters with the ones
        given."""
        model = utils.load_efficientnet(classes=10)
        params_dict = zip(model.state_dict().keys(), parameters)
        state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
        model.load_state_dict(state_dict, strict=True)
        return model

    def fit(self, parameters, config):
        """Train parameters on the locally held training set."""

        # Update local model parameters
        model = self.set_parameters(parameters)

        # Get hyperparameters for this round
        batch_size: int = int(config["batch_size"])
        epochs: int = int(config["local_epochs"])

        n_valset = int(len(self.trainset) * self.validation_split)

        valset = torch.utils.data.Subset(self.trainset, range(0, n_valset))
        trainset = torch.utils.data.Subset(
            self.trainset, range(n_valset, len(self.trainset))
        )

        trainLoader = DataLoader(trainset, batch_size=batch_size, shuffle=True)
        valLoader = DataLoader(valset, batch_size=batch_size)

        results = utils.train(model, trainLoader, valLoader, epochs, self.device)

        parameters_prime = utils.get_model_params(model)
        num_examples_train = len(trainset)

        return parameters_prime, num_examples_train, results

    def evaluate(self, parameters, config):
        """Evaluate parameters on the locally held test set."""
        # Update local model parameters
        model = self.set_parameters(parameters)

        # Get config values
        steps: int = int(config["val_steps"])

        # Evaluate global model parameters on the local test data and return results
        testloader = DataLoader(self.testset, batch_size=16)

        loss, accuracy = utils.test(model, testloader, steps, self.device)
        return float(loss), len(self.testset), {"accuracy": float(accuracy)}

    def run(self, data, client):
        weights = data.get("weights")
        config = data.get("config")
        agg_weights, fit_examples, fit_metrics = self.fit(weights, config)
        loss, eval_examples, eval_metrics = self.evaluate(weights, config)
        data = {
            "weights": agg_weights,
            "fit_examples": fit_examples,
            "fit_metrics": fit_metrics,
            "loss": loss,
            "eval_examples": eval_examples,
            "eval_metrics": eval_metrics,
        }

        client.send_weights(data)


def main(toy, client):
    print("running")
    index = random.randint(1, 10)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    trainset, testset = utils.load_partition(index)

    if toy:
        trainset = torch.utils.data.Subset(trainset, range(10))
        testset = torch.utils.data.Subset(testset, range(10))

    handler = CifarClient(trainset, testset, device)

    data = client.fetch_weights()

    handler.run(data, client)


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port number")

    args = parser.parse_args()
    client = Client()

    client.port(f"{args.port}").start()

    main(True, client)

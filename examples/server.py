from switchml.server import Server
import utils

from functools import reduce

import numpy as np
import torch
from torch.utils.data import DataLoader
from collections import OrderedDict


def aggregate(results):
    """Compute weighted average."""
    # Calculate the total number of examples used during training
    num_examples_total = sum([num_examples for _, num_examples in results])

    # Create a list of weights, each multiplied by the related number of examples
    weighted_weights = [
        [layer * num_examples for layer in weights] for weights, num_examples in results
    ]

    # Compute average weights of each layer
    weights_prime = [
        reduce(np.add, layer_updates) / num_examples_total
        for layer_updates in zip(*weighted_weights)
    ]
    return weights_prime


def weighted_loss_avg(results):
    """Aggregate evaluation results obtained from multiple clients."""
    num_total_evaluation_examples = sum([num_examples for num_examples, _ in results])
    weighted_losses = [num_examples * loss for num_examples, loss in results]
    return sum(weighted_losses) / num_total_evaluation_examples


class CustomStrategy:
    def __init__(self, evaluate_fn=None):
        self.evaluate_fn = evaluate_fn

    def evaluate(self, server_round: int, parameters):
        """Evaluate model parameters using an evaluation function."""
        if self.evaluate_fn is None:
            # No evaluation function provided
            return None
        parameters_ndarrays = parameters
        eval_res = self.evaluate_fn(parameters)
        if eval_res is None:
            return None
        loss, metrics = eval_res
        return loss, metrics

    def aggregate_fit(self, weights):
        weights_results = [
            (
                client["fit_res"]["weights"],
                client["fit_res"]["num_examples"],
            )
            for client in weights
        ]

        parameters_aggregated = aggregate(weights_results)

        return parameters_aggregated

    def aggregate_eval(self, weights):
        loss_aggregated = weighted_loss_avg(
            [
                (client["eval_res"]["num_examples"], client["eval_res"]["loss"])
                for client in weights
            ]
        )

        return loss_aggregated


def get_eval_fn(model, toy: bool):
    """Return an evaluation function for server-side evaluation."""

    # Load data and model here to avoid the overhead of doing it in `evaluate` itself
    trainset, _, _ = utils.load_data()

    n_train = len(trainset)
    if toy:
        # use only 10 samples as validation set
        valset = torch.utils.data.Subset(trainset, range(n_train - 10, n_train))
    else:
        # Use the last 5k training examples as a validation set
        valset = torch.utils.data.Subset(trainset, range(n_train - 5000, n_train))

    valLoader = DataLoader(valset, batch_size=16)
    # The `evaluate` function will be called after every round
    def evaluate(weights):
        # Update model with the latest parameters
        params_dict = zip(model.state_dict().keys(), weights)
        state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
        model.load_state_dict(state_dict, strict=True)

        loss, accuracy = utils.test(model, valLoader)
        return loss, {"accuracy": accuracy}

    return evaluate


model = utils.load_efficientnet(classes=10)

model_weights = [val.cpu().numpy() for _, val in model.state_dict().items()]


server = Server()

config = {"batch_size": 16, "local_epochs": 1, "val_steps": 5}

server.port("5000").config(config).strategy(
    CustomStrategy(get_eval_fn(model, True))
).weights(model_weights).start()

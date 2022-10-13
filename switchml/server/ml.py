from dataclasses import dataclass, field
from switchml.strategies import FedAverage


from typing import Any

from switchml.utils import parameters_to_weights


@dataclass
class SwitchMl:
    strategy: Any = field(default=FedAverage())
    config: Any = field(default_factory=dict)
    weights: Any = field(default_factory=list)

    def set_config(self, config):
        self.config = config
        return self

    def set_strategy(self, strategy):
        self.strategy = strategy
        return self

    def set_weights(self, weights):
        self.weights.append(weights)
        return len(self.weights) >= self.config.get("min_clients", 2)

    def run_strategy(self, weights):
        data = [self.parse_data(weight) for weight in weights]
        agg_weights = self.strategy.aggregate_fit(data)
        agg_loss = self.strategy.aggregate_eval(data)
        self.strategy.evaluate(1, agg_weights)
        return agg_weights

    def parse_data(self, data):
        weights = parameters_to_weights(data.fit_res.parameters)
        return {
            "fit_res": {
                "weights": weights,
                "num_examples": data.fit_res.num_examples,
                "metrics": data.fit_res.metrics,
            },
            "eval_res": {
                "loss": data.eval_res.loss,
                "num_examples": data.eval_res.num_examples,
                "metrics": data.eval_res.metrics,
            },
        }

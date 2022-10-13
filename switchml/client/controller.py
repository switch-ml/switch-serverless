import logging
import requests
from switchml.protobuf.service_pb2 import (
    EvalRes,
    FitRes,
    Parameters,
    WeightsInvocation,
    WeightsResponse,
)
from switchml.utils import parameters_to_weights, weights_to_parameters


class ProxyController:

    default_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def send_weights(self, weights):
        register_uri = "/api/v1/state/"
        try:

            proxy_url = "http://{}:{}{}".format(self.host, self.port, register_uri)
            parameters = weights_to_parameters(weights.get("weights"))

            fit_res = FitRes(
                parameters=parameters,
                num_examples=weights.get("fit_examples"),
                metrics=weights.get("fit_metrics"),
            )
            eval_res = EvalRes(
                loss=weights.get("loss"),
                num_examples=weights.get("eval_examples"),
                metrics=weights.get("eval_metrics"),
            )

            weights_invocation = WeightsInvocation(fit_res=fit_res, eval_res=eval_res)

            binary_payload = weights_invocation.SerializeToString()

            resp = requests.post(
                proxy_url, data=binary_payload, headers=self.default_headers
            )

            logging.info("response %s", resp)
        except Exception as e:
            logging.error("ERROR: %s", e)
            logging.error("Shit %s", e.__cause__)

    def fetch_weights(self):
        register_uri = "/api/v1/server-weights/"
        try:

            proxy_url = "http://{}:{}{}".format(self.host, self.port, register_uri)

            weights_request = requests.get(proxy_url, headers=self.default_headers)

            databytes = bytes(weights_request.content)
            weights_response = WeightsResponse()
            weights_response.ParseFromString(databytes)

            return {
                "weights": parameters_to_weights(weights_response.parameters),
                "config": weights_response.config,
            }

        except Exception as e:
            logging.error("ERROR: %s", e)
            logging.error("Shit %s", e.__cause__)

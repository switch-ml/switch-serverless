import logging
import requests
import io

from switchml.protobuf.service_pb2 import Parameters, WeightsResponse
from switchml.utils import weights_to_parameters


class ProxyController:

    register_uri = "/api/v1/server-weights/"

    default_headers = {
        "Accept": "application/octet-stream",
        "Content-Type": "application/octet-stream",
    }

    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def send_weights(self, weights, config):
        try:
            weights_response = WeightsResponse(
                parameters=weights_to_parameters(weights), config=config
            )

            data = weights_response.SerializeToString()

            logging.info("PROXY REQUEST SHOULD BE SENT FOR INITIAL WEIGHTS")

            proxy_url = "http://{}:{}{}".format(self.host, self.port, self.register_uri)

            resp = requests.post(proxy_url, data=data, headers=self.default_headers)

            logging.info("response %s", resp)
        except Exception as e:
            logging.error("ERROR: %s", e)
            logging.error("Shit %s", e.__cause__)

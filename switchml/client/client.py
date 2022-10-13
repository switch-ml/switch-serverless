from threading import Thread
from spawn.sdk import Spawn
from dataclasses import dataclass

import os

from switchml.client.controller import ProxyController
from switchml.client.handler import action_handler


@dataclass
class Client(Spawn):
    __proxyController = ProxyController(
        os.environ.get("PROXY_HOST", "localhost"),
        os.environ.get("PROXY_PORT", "9001"),
    )

    def register_blueprint(self, handler):
        self.app.register_blueprint(handler, url_prefix=f"/api/v1/")

    def start_client(self):
        self.app = self._Spawn__app
        self.host = self._Spawn__host
        self.port = self._Spawn__port

        self.register_blueprint(action_handler)

        self.app.run(host=self.host, port=self.port, use_reloader=False, debug=True)

    def start(self):
        thread = Thread(target=lambda: self.start_client())
        try:
            thread.start()
        except Exception as e:
            print(e)

    def fetch_weights(self):
        weights = self.__proxyController.fetch_weights()
        return weights

    def send_weights(self, data):
        self.__proxyController.send_weights(data)
        return self

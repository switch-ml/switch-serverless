from spawn.sdk import Spawn
import os
from dataclasses import dataclass
from threading import Thread


from switchml.server.ml import SwitchMl
from switchml.server.handler import action_handler
from switchml.server.controller import ProxyController


@dataclass
class Server(Spawn):
    proxyController = ProxyController(
        os.environ.get("PROXY_HOST", "localhost"),
        os.environ.get("PROXY_PORT", "9001"),
    )
    switchml = SwitchMl()

    def register_blueprint(self, handler):
        self.app.register_blueprint(handler, url_prefix=f"/api/v1/")

    def start_server(self):
        self.app = self._Spawn__app
        self.host = self._Spawn__host
        self.port = self._Spawn__port

        self.register_blueprint(action_handler)
        self.app.config["switchml"] = self.switchml
        self.app.config["controller"] = self.proxyController

        self.app.run(host=self.host, port=self.port, use_reloader=False, debug=True)

    def start(self):
        thread = Thread(target=lambda: self.start_server())
        try:
            thread.start()
        except Exception as e:
            print(e)

    def config(self, config):
        self.switchml.set_config(config)
        return self

    def strategy(self, strategy):
        self.switchml.set_strategy(strategy)
        return self

    def weights(self, weights):
        res = self.switchml.strategy.evaluate(0, weights)
        if res is not None:
            pass
        self.proxyController.send_weights(weights, self.switchml.config)
        return self

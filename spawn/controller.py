"""
Copyright 2022 Eigr.
Licensed under the Apache License, Version 2.0.
"""
from spawn.eigr.actor_pb2 import (
    Actor,
    ActorDeactivateStrategy,
    ActorSnapshotStrategy,
    ActorState,
    ActorSystem,
    Registry,
    TimeoutStrategy,
)
from spawn.eigr.protocol_pb2 import (
    RegistrationRequest,
    RegistrationResponse,
    ServiceInfo,
)

from spawn.entity import ActorEntity

import logging
import platform
import requests

from typing import Any, List


class SpawnActorController:

    register_uri = "/api/v1/system"

    default_headers = {
        "Accept": "application/octet-stream",
        "Content-Type": "application/octet-stream",
    }

    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def invoke(
        self, actor_name: str, actor_command: str, arg: Any, output_type: Any
    ) -> Any:
        print(actor_command, actor_name, arg, output_type, "cc")
        return ""

    def register(self, actors: List[ActorEntity]):
        logging.info("Registering Actors on the Proxy %s", actors)
        try:

            proxy_url = "http://{}:{}{}".format(self.host, self.port, self.register_uri)

            # Create actor params via ActorEntity
            deactivate_timeout_strategy = TimeoutStrategy()
            deactivate_timeout_strategy.timeout = 10000

            snaphot_timeout_strategy = TimeoutStrategy()
            snaphot_timeout_strategy.timeout = 120000

            actor_state = ActorState()

            deactivate_strategy = ActorDeactivateStrategy()
            deactivate_strategy.timeout.CopyFrom(deactivate_timeout_strategy)

            snaphot_strategy = ActorSnapshotStrategy()
            snaphot_strategy.timeout.CopyFrom(snaphot_timeout_strategy)

            actor_01 = Actor()
            actor_01.name = "user_actor_01"
            actor_01.persistent = True
            actor_01.state.CopyFrom(actor_state)
            actor_01.deactivate_strategy.CopyFrom(deactivate_strategy)
            actor_01.snapshot_strategy.CopyFrom(snaphot_strategy)

            registry = Registry()
            registry.actors.get_or_create("user_actor_01").CopyFrom(actor_01)

            actor_system = ActorSystem()
            actor_system.name = "spawn-system"
            actor_system.registry.CopyFrom(registry)

            service_info = ServiceInfo()
            service_info.service_name = "spawn-python-sdk"
            service_info.service_version = "0.1.0"
            service_info.service_runtime = (
                "Python "
                + platform.python_version()
                + " ["
                + platform.python_implementation()
                + " "
                + platform.python_compiler()
                + "]"
            )

            service_info.support_library_name = "spawn-python-sdk"
            service_info.support_library_version = "0.1.0"
            service_info.protocol_major_version = 1
            service_info.protocol_minor_version = 1

            response = RegistrationRequest()
            response.service_info.CopyFrom(service_info)
            response.actor_system.CopyFrom(actor_system)

            binary_payload = response.SerializeToString()

            resp = requests.post(
                proxy_url, data=binary_payload, headers=self.default_headers
            )

            logging.info("Actors register response %s", resp)
        except Exception as e:
            logging.error("ERROR: %s", e)
            logging.error("Shit %s", e.__cause__)

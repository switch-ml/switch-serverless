"""
Copyright 2022 Switchml.
Licensed under the Apache License, Version 2.0.
"""
from flask import Blueprint, request, send_file, current_app, Response


import io
import logging
from threading import Thread
from switchml.protobuf.service_pb2 import WeightsInvocation
from switchml.utils import parameters_to_weights

action_handler = Blueprint("action_endpoint", __name__)


def run_strategy(switchml, controller):
    weights = switchml.run_strategy(switchml.weights)

    # send aggregated weights as send_file response.
    # format aggregated weights with protobuf
    controller.send_weights(weights, switchml.config)


@action_handler.route("state/", methods=["POST"])
def action():
    data = request.data
    # parse fit_res, eval_res from protobuf data using serializer
    logging.info("Received request from proxy")
    databytes = bytes(data)

    weights_invocation = WeightsInvocation()
    weights_invocation.ParseFromString(databytes)
    logging.debug("Weights invocation data")

    switchml = current_app.config["switchml"]
    controller = current_app.config["controller"]

    can_run_strategy = switchml.set_weights(weights_invocation)

    if can_run_strategy:
        thread = Thread(target=lambda: run_strategy(switchml, controller))
        try:
            thread.start()
        except Exception as e:
            print(e)

    return Response("")

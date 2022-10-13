"""
Copyright 2022 Switchml.
Licensed under the Apache License, Version 2.0.
"""
from flask import Blueprint, request, send_file, current_app, Response


import io
import logging

action_handler = Blueprint("action_endpoint", __name__)


@action_handler.route("state/", methods=["POST"])
def action():
    data = request.data
    logging.info("Received request: %s", data)
    # current_app.config["client_callback"](data)

    return Response("")

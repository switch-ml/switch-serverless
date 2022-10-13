from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

app.config["weights"] = []
app.config["server-weights"] = None


@app.route("/api/v1/state/", methods=["POST"])
def send_weights():

    default_headers = {
        "Accept": "application/octet-stream",
        "Content-Type": "application/octet-stream",
    }

    proxy_url = "http://{}:{}{}".format("localhost", "5000", "/api/v1/state/")

    resp = requests.post(proxy_url, data=request.data, headers=default_headers)

    return jsonify(message="success")


@app.route("/api/v1/server-weights/", methods=["POST", "GET"])
def server_weights():
    if request.method == "GET":

        # sending initial weights and config to switch-sdk client
        return app.config["server-weights"]

    # recieved initial weights and config from switch-sdk server
    app.config["server-weights"] = request.data
    # except sender/servers send requests to connected clients.

    return jsonify(message="success")

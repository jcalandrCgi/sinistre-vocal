# -*- coding: utf-8 -*-

import os
import json
import pandas as pd

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

annuaire = pd.read_csv("annuaire.csv")
contrat = pd.read_csv("contrat.csv", delimiter=";")


@app.route("/")
def start():
    return "The server is starting"

@app.route("/webhook", methods=["POST"])
def webhook():
    """ This method handles the http requests for the Dialogflow webhook
    """
    req = request.get_json(force=True)
    print(req)
    action = req.get('queryResult').get('action')
    print(action)
    return "webhook : "+action

if __name__ == "__main__":
    PORT=5000
    print("Demarrage du serveur")
    app.run(host="0.0.0.0",
            port=PORT,
            debug=True
    )

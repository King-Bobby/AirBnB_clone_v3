#!/usr/bin/python3
"""This module contains the Flask application for the Airbnb Clone API.
"""


from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
import os


app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception):
    """after each session, close query"""
    storage.close()


@app.errorhandler(404)
def notfound(error):
    """Error handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5002))
    app.run(host=host, port=port, threaded=True)

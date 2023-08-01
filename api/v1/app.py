#!/usr/bin/python3
"""this module contains the Flask application for the Airbnb Clone API"""


from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)


@app.teardown.appcontext
def tear_down(exception):
    """after each session, close query"""
    storage.close()


@app.errorhandler(404)
def notfound(error):
    """Error handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))

    app.run(host=host, port=port, threaded=true)

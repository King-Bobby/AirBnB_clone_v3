#!/usr/bin/python3
"""
This module contains the Flask application for the Airbnb Clone API.

It registers the blueprint `app_views` from the `api.v1.views` package to handle API routes.
The application uses the `models.storage` module to interact with the database and retrieve data.
"""


from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
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

#!/usr/bin/python3
"""
This module contains the file index.py.
It registers the blueprint `app_views` from the `api.v1.views` package to handle API routes.
The application uses the `models.storage` module to interact with the database and retrieve data
"""


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def numofobjects_by_type():
    classes = {
            "Amenity": storage.count(Amenity),
            "Cities": storage.count(City),
            "Places": storage.count(Place),
            "Reviews": storage.count(Review),
            "States": storage.count(State),
            "Users": storage.count(User)
        }
    return jsonify(classes)

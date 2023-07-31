#!/usr/bin/python3
"""
This contains the Module index
"""


from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods['GET'])
def numofobjects_by_type():
    classes = {
            "Amenity": storage.count(Amenity),
            "Cities": storage.count(City),
            "Places": storage.count(Places),
            "Reviews": storage.count(Reviews),
            "States": storage.count(State),
            "Users": storage.count(User)
        }
    return jsonify(classes)

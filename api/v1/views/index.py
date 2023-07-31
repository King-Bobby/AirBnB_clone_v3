#!/usr/bin/python3
"""
Contains Module index
"""


from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status:
    return jsonify({"status": "OK"})

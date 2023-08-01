#!/usr/bin/python3
"""This contains the module user.py
"""


from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models.user import User
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """Retrieves the list of all User objects"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>'. methods=['GET'], strict_slashes=False)
def get_one_user(user_id):
    """Retrieves a User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a User"""
    req_json = request.get_json()
    if not req_json:
        abort(400, 'Not a JSON')
    if 'email' not in req_json:
        abort(400, 'Missing email')
    if 'password' not in req_json:
        abort(400, 'Missing password')
    new_user = (**req_json)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    req_json = request.get_json()
    if not req_json:
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in req_json.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200

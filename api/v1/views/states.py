#!/usr/bin/python3
"""
This contains the Module states.py
"""


from app.v1.views import app_views
from models import storage
from models.state import State
from flask import Flask, jsonify, request, abort


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State"""
    req_json = request.get_json()
    if not req_json:
        abort(400, 'Not a JSON')
    if 'name' not in req_json:
        abort(400, 'Missing name')
    new_state = (**req_json)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<states_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if not state:
        aboort(404)
    req_json = request.get_json()
    if not req_json:
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in req_json.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200

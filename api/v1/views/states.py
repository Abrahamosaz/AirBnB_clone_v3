#!/usr/bin/python3
"""view for state objects in the database"""
from api.v1.views import app_views
from flask import jsonify, make_response, abort
from flask import request
from models import storage
from models.state import State

@app_views.route('/states/', strict_slashes=False)
def get_states():
    """get all states in the database"""
    state_objs = storage._DBStorage__session.query(State).all()
    state_list = [obj.to_dict() for obj in state_objs]
    return jsonify(state_list)

@app_views.route('/states/<state_id>', strict_slashes=False)
def state_by_id(state_id):
    """get state from the database by id"""
    state_obj = storage.get(State, state_id)
    if state_obj is None:
        abort(404)
    return (make_response(jsonify(state_obj.to_dict())))

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """delete state from the database"""
    state_obj = storage.get(State, state_id)
    print("state  objects", state_obj)
    if state_obj is None:
        abort(404)
    storage.delete(state_obj)
    storage.save()
    return make_response({}, 200)

@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """create a new state object"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    json_data = request.get_json()
    if json_data.get('name') is None:
        abort(400, 'Missing name')
    new_state = State(**json_data)
    storage.new(new_state)
    storage.save()
    return make_response(jsonify(new_state.to_dict()), 201)

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """update the state with the state_id in the database"""
    state_obj = storage.get(State, state_id)
    if state_obj is None:
        abort(404)
    if not request.is_json:
        abort(400, 'Not a JSON')
    json_data = request.get_json()

    ignore_attr = ['created_at', 'updated_at', 'id']
    for key, value in json_data.items():
        if key not in ignore_attr:
            setattr(state_obj, key, value)
    storage.save()
    return (make_response(jsonify(state_obj.to_dict()), 200))
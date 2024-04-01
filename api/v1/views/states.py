#!/usr/bin/python3
"""State objects that handles all default RESTFul API actions:"""
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def GETStates():
    """"""
    AllStates = storage.all(State).values()
    StatesList = []
    for st in AllStates:
        StatesList.append(st.to_dict())
    return jsonify(StatesList)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def GETState(state_id):
    """"""
    st = storage.get(State, state_id)
    if not st:
        abort(404)
    return jsonify(st.to_dict())


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def POSTState():
    """"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    Data = request.get_json()
    Inst = State(**Data)
    Inst.save()
    return make_response(jsonify(Inst.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def PUTState(state_id):
    """"""
    st = storage.get(State, state_id)
    if not st:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    deb = ['id', 'created_at', 'updated_at']
    Data = request.get_json()
    for Key, val in Data.items():
        if Key not in deb:
            setattr(st, Key, val)
    storage.save()
    return make_response(jsonify(st.to_dict()), 200)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def DELETEState(state_id):
    """"""
    st = storage.get(State, state_id)
    if not st:
        abort(404)
    storage.delete(st)
    storage.save()
    return make_response(jsonify({}), 200)

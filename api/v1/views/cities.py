#!/usr/bin/python3
"""cities.py"""
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def GETCities(state_id):
    """Get"""
    CitiesList = []
    st = storage.get(State, state_id)
    if not st:
        abort(404)
    for CT in st.cities:
        CitiesList.append(CT.to_dict())
    return jsonify(CitiesList)


@app_views.route('/cities/<city_id>/', methods=['GET'], strict_slashes=False)
def GETCity(city_id):
    """get"""
    CT = storage.get(City, city_id)
    if not CT:
        abort(404)
    return jsonify(CT.to_dict())


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def POSTCity(state_id):
    """get"""
    st = storage.get(State, state_id)
    if not st:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    Data = request.get_json()
    Inst = City(**Data)
    Inst.state_id = st.id
    Inst.save()
    return make_response(jsonify(Inst.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def PUTCity(city_id):
    """put"""
    CT = storage.get(City, city_id)
    if not CT:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    deb = ['id', 'state_id', 'created_at', 'updated_at']
    Data = request.get_json()
    for key, value in Data.items():
        if key not in deb:
            setattr(CT, key, value)
    storage.save()
    return make_response(jsonify(CT.to_dict()), 200)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def DELCity(city_id):
    """del"""
    CT = storage.get(City, city_id)
    if not CT:
        abort(404)
    storage.delete(CT)
    storage.save()
    return make_response(jsonify({}), 200)

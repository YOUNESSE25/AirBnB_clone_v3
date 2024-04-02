#!/usr/bin/python3
"""user.py"""
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def GETUsers():
    """"""
    USers = storage.all(User).values()
    UsersList = []
    for U in USers:
        UsersList.append(U.to_dict())
    return jsonify(UsersList)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def GETUser(user_id):
    """get"""
    USer = storage.get(User, user_id)
    if not USer:
        abort(404)
    return jsonify(USer.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def POSTUser():
    """post """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    Data = request.get_json()
    instance = User(**Data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def PUTUser(user_id):
    """put"""
    USer = storage.get(User, user_id)

    if not USer:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    deb = ['id', 'email', 'created_at', 'updated_at']

    Data = request.get_json()
    for key, value in Data.items():
        if key not in deb:
            setattr(USer, key, value)
    storage.save()
    return make_response(jsonify(USer.to_dict()), 200)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def DELUser(user_id):
    """del"""
    USer = storage.get(User, user_id)
    if not USer:
        abort(404)
    storage.delete(USer)
    storage.save()
    return make_response(jsonify({}), 200)

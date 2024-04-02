#!/usr/bin/python3
""""""
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def GETAmenitie():
    """"""
    Amenities = storage.all(Amenity).values()
    list_amenities = []
    for amty in Amenities:
        list_amenities.append(amty.to_dict())
    return jsonify(list_amenities)


@app_views.route('/amenities/<amenity_id>/', methods=['GET'],
                 strict_slashes=False)
def GETAmenity(amenity_id):
    """"""
    amty = storage.get(Amenity, amenity_id)
    if not amty:
        abort(404)
    return jsonify(amty.to_dict())


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def POSTAmenity():
    """"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    Data = request.get_json()
    instance = Amenity(**Data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def PUTAmenity(amenity_id):
    """"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    deb = ['id', 'created_at', 'updated_at']
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    data = request.get_json()
    for Key, value in data.items():
        if Key not in deb:
            setattr(amenity, Key, value)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def DELAmenity(amenity_id):
    """"""
    amty = storage.get(Amenity, amenity_id)
    if not amty:
        abort(404)
    storage.delete(amty)
    storage.save()
    return make_response(jsonify({}), 200)

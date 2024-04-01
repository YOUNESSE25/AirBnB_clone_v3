#!/usr/bin/python3
"""create a file index.py"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def GetStatus():
    """returns a JSON: "status": "OK"/"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def Getstats():
    """"""
    objects = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    for Key, Val in objects.items():
        objects[Key] = storage.count(Val)
    return jsonify(objects)
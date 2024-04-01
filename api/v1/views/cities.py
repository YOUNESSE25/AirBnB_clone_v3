#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
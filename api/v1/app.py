#!/usr/bin/python3
"""
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def closedb(error):
    """ close db """
    storage.close()


@app.errorhandler(404)
def pageNotFound(error):
    """"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """main"""
    HOST = environ.get('HBNB_API_HOST')
    if not HOST:
        HOST = '0.0.0.0'
    PORT = environ.get('HBNB_API_PORT')
    if not PORT:
        port = '5000'
    app.run(host=HOST, port=PORT, debug=True, threaded=True)

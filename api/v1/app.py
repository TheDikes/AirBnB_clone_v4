#!/usr/bin/python3
"""
Flask App
"""
from flask import Flask, jsonify, abort
from os import getenv
from api.v1.views import app_views
from models import storage


# Global Flask Application Variable: app
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def downtear(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode': 404, 'error': 'Not found'})


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)

#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage

@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')

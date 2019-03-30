import json
from datetime import date
from flask import jsonify, Blueprint, request
from queries import *

app_ = Blueprint('app_', __name__)

# User routes
@app_.route('/users/', methods=['GET'])
def get_users_route():
    result = get_users()
    return jsonify(result)

@app_.route('/users/<int:index>', methods=['GET'])
def get_user_route(index):
    result = get_user(index)
    return jsonify(result)

@app_.route('/users/', methods=['POST'])
def create_user_route():
    name = request.json['name']
    code = request.json['code']
    user = create_user(name, code)
    resp = user.save()
    return jsonify(resp)

@app_.route('/users/', methods=['PUT'])
def update_user_route():
    id = request.json['id']
    name = request.json['name']
    code = request.json['code']
    resp = update_user(id, name, code)
    return jsonify(resp)

@app_.route('/users/<int:index>', methods=['DELETE'])
def delete_user_route(index):
    result = delete_user(index)
    return jsonify(result)

# Lab routes
@app_.route('/labs/', methods=['GET'])
def get_labs_route():
    result = get_labs()
    return jsonify(result)

@app_.route('/labs/<int:index>', methods=['GET'])
def get_lab_route(index):
    result = get_lab(index)
    return jsonify(result)

@app_.route('/labs/', methods=['POST'])
def create_lab_route():
    name = request.json['name']
    description = request.json['description']
    lab = create_lab(name, description)
    resp = lab.save()
    return jsonify(resp)

@app_.route('/labs/', methods=['PUT'])
def update_lab_route():
    id = request.json['id']
    name = request.json['name']
    description = request.json['description']
    taken = request.json['taken']
    resp = update_lab(id, name, description, taken)
    print(resp)
    return jsonify(resp)

@app_.route('/labs/<int:index>', methods=['DELETE'])
def delete_lab_route(index):
    result = delete_lab(index)
    return jsonify(result)

# Measurement routes
@app_.route('/measurements/', methods=['GET'])
def get_measurements_route():
    result = get_measurements()
    return jsonify(result)

@app_.route('/measurements/<int:index>', methods=['GET'])
def get_measurement_route(index):
    result = get_measurement(index)
    return jsonify(result)

@app_.route('/measurements/', methods=['POST'])
def create_measurement_route():
    lab_id = request.json['lab_id']
    user_id = request.json['user_id']
    results = request.json['results']
    
    measurement = create_measurement(lab_id, user_id, results)
    resp = measurement.save()
    return jsonify(resp)

@app_.route('/measurements/', methods=['PUT'])
def update_measurement_route():
    id = request.json['id']
    results = request.json['results']
    resp = update_measurement(id, results)
    return jsonify(resp)

@app_.route('/measurements/<int:index>', methods=['DELETE'])
def delete_measurement_route(index):
    result = delete_measurement(index)
    return jsonify(result)

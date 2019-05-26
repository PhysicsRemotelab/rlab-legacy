import json
from datetime import date
from flask import jsonify, Blueprint, request
from queries import *
from models import Lab
from playhouse.shortcuts import model_to_dict, dict_to_model
from peewee import DateTimeField

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
    lab = create_lab(name)
    resp = lab.save()
    return jsonify(resp)

@app_.route('/labs/', methods=['PUT'])
def update_lab_route():
    id = request.json['id']
    name = request.json['name']
    description = request.json['description']
    taken = request.json['taken']
    access_token = request.json['access_token']
    resp = update_lab(id, name, description, taken, access_token)
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
    access_token = request.json['access_token']
    results = request.json['results']
    
    measurement = create_measurement(lab_id, access_token, results)
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

@app_.route('/check_token/', methods=['POST'])
def check_token_route():
    id = request.json['id']
    access_token = request.json['access_token']
    lab = Lab.get(Lab.id == id)

    if(lab.taken == True):
        if(lab.access_token == access_token):
            if lab.updated > datetime.datetime.now() - datetime.timedelta(seconds=60):
                return jsonify({ 'result': '1', 'note': 'Lab was taken, access token valid', 'lab': model_to_dict(lab) })
            else:
                lab.taken = False
                lab.access_token = ''
                lab.save()
                return jsonify({ 'result': '0', 'note': 'Lab was taken, access token not valid', 'lab': model_to_dict(lab) })
        else:
            return jsonify({ 'result': '0', 'note': 'Lab was taken, access token not valid', 'lab': model_to_dict(lab) })
    else:
        lab.taken = True
        lab.access_token = access_token
        lab.updated = datetime.datetime.now()
        print(datetime.datetime.now())
        lab.save()
        return jsonify({ 'result': '1', 'note': 'Lab was not taken, access token activated', 'lab': model_to_dict(lab) })

    return jsonify({ 'result': '-1', 'note': 'Limbo, you should not be here' })

@app_.route('/free_lab/', methods=['POST'])
def free_lab_route():
    id = request.json['id']
    access_token = request.json['access_token']
    lab = Lab.get(Lab.id == id)

    if(lab.access_token == access_token):
        lab.taken = False
        lab.access_token = ''
        lab.updated = datetime.datetime.now() - datetime.timedelta(seconds=100) 
        lab.save()
        return jsonify({ 'result': '1', 'note': 'Lab was set free' })
    else:
        return jsonify({ 'result': '0', 'note': 'Lab was not set free' })

    return jsonify({ 'result': '-1', 'note': 'Limbo, you should not be here' })

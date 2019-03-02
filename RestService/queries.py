from datetime import date
from models import User, Lab, Measurement
from playhouse.shortcuts import model_to_dict, dict_to_model

# User queries
def get_users():
    query = User.select()
    users = []
    for user in query:
        users.append(model_to_dict(user))
    return users

def get_user(id):
    query = User.select().where(User.id == id).get()
    result = model_to_dict(query)
    return result

def create_user(name, code):
    user = User(name=name, code=code)
    user.save()
    return user

def update_user(id, name, code):
    user = User.get(User.id == id)
    user.name = name
    user.code = code
    result = user.save()
    return result

def delete_user(id):
    user = User.get(User.id == id)
    result = user.delete_instance()
    return result

# Lab queries
def get_labs():
    query = Lab.select()
    labs = []
    for lab in query:
        labs.append(model_to_dict(lab))
    return labs

def get_lab(id):
    query = Lab.select().where(Lab.id == id).get()
    result = model_to_dict(query)
    return result

def create_lab(name, description):
    lab = Lab(name=name, description=description)
    lab.save()
    return lab

def update_lab(id, name, description, taken):
    lab = Lab.get(Lab.id == id)
    lab.name = name
    lab.description = description
    lab.taken = taken
    result = lab.save()
    return result

def delete_lab(id):
    lab = Lab.get(Lab.id == id)
    result = lab.delete_instance()
    return result

# Measrement queries
def get_measurements():
    query = Measurement.select()
    measurements = []
    for measurement in query:
        measurements.append(model_to_dict(measurement))
    return measurements

def get_measurement(id):
    query = Measurement.select().where(Measurement.id == id).get()
    result = model_to_dict(query)
    return result

def create_measurement(lab_id, user_id, results):
    measurement = Measurement(lab_id=lab_id, user_id=user_id, results=results)
    measurement.save()
    return measurement

def update_measurement(id, results):
    measurement = Measurement.get(Measurement.id == id)
    measurement.results = results
    response = measurement.save()
    return response

def delete_measurement(id):
    measurement = Measurement.get(Measurement.id == id)
    result = measurement.delete_instance()
    return result

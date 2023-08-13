from flask import  jsonify, request
from app.user import userbp
import json
import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
user_file = os.path.join(location, "../data/users.json")

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file )

def write_json(file_path, data):
    with open(file_path, "w") as file:
        return json.dump(data, file, indent=2)

@userbp.route("/users", methods=['GET'])
def get_all_user():
    data = read_json(user_file)
    response = jsonify(
        {
            "success": True,
            "data": data
        }
    )
    return response

@userbp.route("/users/<int:id>", methods=['GET'])
def get_one_user(id):
    users = read_json(user_file)

    user = [user for user in users["data"] if user["_id"] == id]
    if not user:
        response = jsonify({
            "message": "User Not Found",
        })

        return response
    
    response = jsonify({
         "success":True,
         "data": user[0]
    })

    return response

@userbp.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    newData = {
        "_id": data["_id"],
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }

    temp_data = read_json(user_file)
    temp_data ['data'].append(newData)

    write_json(user_file, temp_data)
    response = jsonify(
        {
            "success": True,
            "message": "User is Created"
        }
    )
    return response

@userbp.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
    data = request.get_json()
    users = read_json(user_file)

    user = [user for user in users["data"] if user["_id"] == id]

    if not user:
        response = jsonify({
            "message": "User Not Found",
        })

        return response
    
    for user in users["data"]:
        if user["_id"] == id:
            user["name"] = data["name"]
            user["email"] = data["email"]
            user["password"] = data["password"]
            break
    
    write_json(user_file, users)
    response = jsonify({
        "success": True,
        "message": "User Successfully Updated"
    })

    return response

@userbp.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    users = read_json(user_file)

    for user in users["data"]:
        if user["_id"] == id:
            users["data"].remove(user)
    
    write_json(user_file, users)

    response = jsonify({
        "success": True,
        "message": "User successfully deleted"
    })

    return response

    
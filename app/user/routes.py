from flask import  jsonify, request
from app.user import userbp
import json
import os
from app.models.user import Users
from app.extensions import db 
from app.models.tasks import Tasks

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
user_file = os.path.join(location, "../data/users.json")

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file )

def write_json(file_path, data):
    with open(file_path, "w") as file:
        return json.dump(data, file, indent=2)

@userbp.route("/", methods=["GET"])
def get_all_user():
    """fungsi untuk mengambil semua data user dari tabel users"""
    limit = request.args.get('limit', 10)
    if type(limit) is not int:
        return jsonify({"message": "invalid parameter"}), 422
    
    users = db.session.execute(
        db.select(Users).limit(limit)
    ).scalars()

    result = []
    for user in users:
        result.append(user.serialize())
    
    response = jsonify(
        success = True,
        data = result
    )

    return response, 200


@userbp.route("/", methods=["POST"], strict_slashes=False)
def create_new_user():
    """fungsi untuk membuat user baru"""
    data = request.get_json()
    input_name = data.get('name')
    input_email = data.get('email')
    input_password = data.get('password')

    if not input_name or not input_email or not input_password:
        return jsonify({"message": "Terdapat Data Kosong"}), 422
    
    newUser = Users(
        name = input_name,
        email = input_email,
        password = input_password
    )

    db.session.add(newUser)
    db.session.commit()

    response = jsonify(
        success = True,
        data = newUser.serialize(),
        message = "Pengguna berhasil dibuat"
    )

    return response, 200


@userbp.route("/<int:id>", methods=["PUT"], strict_slashes=False)
def update_data_user(id):
    """fungsi untuk update data user"""
    data = request.get_json()
    input_name = data.get('name')
    input_email = data.get('email')
    input_password = data.get('password')

    user = Users.query.filter_by(id=id).first()

    if not input_name or not input_email or not input_password:
        return jsonify({"message": "Terdapat Data Kosong"}), 422
    else: 
        user.name = input_name
        user.email = input_email
        user.password = input_password
    
    db.session.commit()

    response = jsonify(
        success = True,
        message = "Pengguna berhasil diubah"
    )

    return response, 200


@userbp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete_data_user(id):
    """fungsi untuk menghapus data pengguna"""
    user = Users.query.filter_by(id=id).first()

    if not user:
        return jsonify({"message": "Data pengguna tidak dapat ditemukan"}), 422
    else:
        db.session.delete(user)
        db.session.commit()
    
    response = jsonify(
        success = True,
        message = "Data pengguna berhasil di hapus"
    )

    return response, 200

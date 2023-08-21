from app.task import taskbp
from flask import request, jsonify
from app.extensions import db
from app.models.tasks import Tasks
from app.models.user import Users


@taskbp.route("/", strict_slashes= False, methods=["GET"])
def get_all_task():
    """ fungsi mengambil semua task dari tabel tasks"""
    limit = request.args.get("limit", 10)
    if type(limit) is not int:
        return jsonify({"message": "invalid parameter"}), 422
    
    tasks = db.session.execute(
        db.select(Tasks).limit(limit)
    ).scalars()

    result = []
    for task in tasks:
        result.append(task.serialize())
    
    response = jsonify(
        success = True,
        data = result
    )

    return response, 200


@taskbp.route("/", strict_slashes= False, methods=["POST"])
def create_new_task():
    """fungsi untuk membuat task baru"""
    # mengambil data yang diinputkan client dan masukkan ke dalam task
    # mengambil data request dari client yang berbentuk json
    data = request.get_json()
    input_title = data.get('title')
    input_description =  data.get('description')
    input_user_id = data.get('user_id')

    # melakukan validasi apakah terdapat data yang kosong atau tidak
    if not input_title or not input_description or not input_user_id:
        return jsonify({"message": "Terdapat Data Kosong"}), 422

    # memasukkan data hasil request dari client ke tabel dalam database
    newTask = Tasks(
        title = input_title,
        description = input_description,
        user_id = input_user_id
        )
    
    db.session.add(newTask)
    db.session.commit()

    response = jsonify({
       "message": 'Task berhasil dibuat',
       "task": newTask.serialize()
    })

    return response, 200


@taskbp.route("/<int:id>", methods = ["PUT"], strict_slashes=False)
def update_data_task(id):
    """fungsi untuk memperbarui data task"""
    data = request.get_json()
    input_title = data.get('title')
    input_description = data.get('description')
    input_user_id = data.get('user_id')

    task = Tasks.query.filter_by(id=id).first()

    # melakukan validasi input apakah tidak ada yang kosong
    if not input_title or not input_description or not input_user_id:
        return jsonify({"message": "Terdapat Data Kosong"})
    else:
        task.title = input_title
        task.description = input_description
        task.user_id = input_user_id
    
    db.session.commit() 

    response = jsonify(
        success = True,
        message = "Data Berhasil Diubah"
    )

    return response, 200


@taskbp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete_data_task(id):
    """fungsi untuk menghapus data task"""
    task = Tasks.query.filter_by(id=id).first()

    if not task:
        return jsonify({"message": "Task tidak dapat ditemukan"}), 422
    else:
        db.session.delete(task)
        db.session.commit()
    
    response = jsonify(
        success = True,
        message = "Data task berhasil di hapus"
    )
    
    return response, 200



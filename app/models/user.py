# model tabel/ schema tabel

from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(90))
    email = db.Column(db.String(90))
    password = db.Column(db.String(1024))

    tasks = db.relationship('Tasks', back_populates='user')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            # 'email': self.email,
            'password': self.password,

            #untuk memanggil data task berdasarkan id pengguna
            'task': [task.serialize() for task in self.tasks]
    }
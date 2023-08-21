# model tabel/ schema tabel

from app.extensions import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(125))
    description = db.Column(db.String(1024))

    user = db.relationship('Users', back_populates='tasks')

    def serialize(self):
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'title': self.title,
            'description' : self.description,
        }
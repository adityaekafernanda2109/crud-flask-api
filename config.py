#untuk menyimpan konfigurasi yang digunakan oleh flask

import os 

# mengambil absolute url dari flask app
basedir = os.path.abspath(os.path.dirname(__file__))


DB_PATH = 'sqlite:///' + os.path.join(basedir, 'app.db')

class Config:
    SECRET_KEY = '123'
    SQLALCHEMY_DATABASE_URI = DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False



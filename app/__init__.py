from flask import Flask
from app.user import userbp
from config import Config
from app.extensions import db, migrate
from app.task import taskbp


def create_app(config_class = Config):
    app = Flask(__name__)

    #memanggil konfigurasi untuk digunakan oleh flask
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(userbp, url_prefix='/users')
    app.register_blueprint(taskbp, url_prefix='/tasks')
    return app

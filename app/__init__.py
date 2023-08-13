from flask import Flask
from app.user import userbp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(userbp)

    return app

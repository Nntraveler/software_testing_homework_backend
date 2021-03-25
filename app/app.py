from flask import Flask
from flask_cors import CORS

from controller import api


def create_app():
    app = Flask(__name__)
    CORS(app, resources='/*')
    api.init_app(app)
    return app

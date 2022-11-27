from os import getenv
from flask import Flask
from db import db
from config import DATABASE_URL
from routes import routes


def create_app():
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.register_blueprint(routes)

    db.init_app(app)

    return app

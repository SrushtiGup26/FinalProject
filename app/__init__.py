# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/final_project'
    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

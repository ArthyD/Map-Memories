from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()
DB_NAME = "database.db"


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
script_directory = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(script_directory,"../dashboard-app/src/assets")
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)
    

    from .website import views

    app.register_blueprint(views, url_prefix='/')

    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
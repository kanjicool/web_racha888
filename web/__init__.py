from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.sqlite3'

def create_database():
    db.create_all()
    print('Database Created')


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "kanjicool"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)


    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_blueprint(views, url_prefix="/")  # localhost:5000/about-us
    app.register_blueprint(auth, url_prefix="/auth")  # localhost:5000/auth/change-password
    app.register_blueprint(admin, url_prefix="/")

    with app.app_context():
        create_database()
        




    return app
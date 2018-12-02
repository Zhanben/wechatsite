from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    from app import models

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .user import user as login_blueprint
    app.register_blueprint(login_blueprint)

    return app

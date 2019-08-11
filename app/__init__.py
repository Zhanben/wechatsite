from flask import Flask
from config import config_dict
from .models import db
from flask_migrate import Migrate

migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    db.init_app(app)
    migrate.init_app(app, db)

    from .view import api_blueprint
    app.register_blueprint(api_blueprint)

    return app

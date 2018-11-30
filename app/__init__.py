from flask import Flask


def create_app():
    app = Flask(__name__)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .oauth import login as login_blueprint
    app.register_blueprint(login_blueprint)

    return app

from flask import Blueprint
from flask_restful import Api
from .user import UserHandler, UsersHandler, FakeDataHandler
from .login import LoginHandler
from .article import ArticleHandler, ArticlesHandler

api_blueprint = Blueprint("api_blueprint", __name__, url_prefix='/api')
api = Api(api_blueprint)
api.add_resource(UsersHandler, '/users')
api.add_resource(UserHandler, '/user/<int:user_id>')
api.add_resource(ArticlesHandler, '/articles')
api.add_resource(ArticleHandler, '/article/<int:article_id>')
api.add_resource(FakeDataHandler, '/fake/')  # create test data
api.add_resource(LoginHandler, '/login')

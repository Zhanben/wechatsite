from flask import Blueprint
from flask_restful import Api

user = Blueprint("user", __name__, url_prefix='/user')
api = Api(user)

from . import views

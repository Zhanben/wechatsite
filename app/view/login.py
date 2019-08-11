import logging
from flask_restful import Resource, reqparse, fields
from flask import request, jsonify
from ..models import db
from ..models.user import User


class LoginHandler(Resource):
    def post(self):
        res = {
            "Action": "Login",
            "Message": "login success",
            "RetCode": 1
        }
        return jsonify(res)

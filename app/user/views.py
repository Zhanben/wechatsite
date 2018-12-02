import logging
import json
from . import api
from .. import db
from ..models import User
from flask import jsonify, request
from flask_restful import Resource, abort, reqparse


@api.resource("/login")
class Login(Resource):
    def get(self):
        logging.info("login success")
        return {'login': ' success!'}


@api.resource("/")
class UserList(Resource):
    def get(self):
        # list user infomation
        result = []
        user_info = User.query.all()
        for user in user_info:
            result.append(user.to_json())
        logging.info("get all user list")
        return jsonify(result)


@api.resource("/<username>")
class UserInfo(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username", location="json", action="append")

    def get(self):
        data = self.parser.parse_args()
        user_name = data.get('username')
        # list user infomation
        result = []
        logging.info("query user info:%s" % user_name)
        user_info = User.query.filter_by(username=user_name)
        for user in user_info:
            result.append(user.to_json())
        logging.info("hello world")
        return jsonify(result)

    def post(self):
        # add user
        # logging.info("get user info:%s" % request.headers)
        data = request.get_data()
        user_info = json.loads(data)
        logging.info("get user info:%s" % user_info)
        user = User(username=user_info["username"], email=user_info["email"], password_hash=["password_hash"],
                    avatar=user_info["avatar"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"AddUserResponse": "success", "retCode": 0})


def abort_if_user_not_exist(user_name):
        abort(404, message={"GetUserResponse": "false", "retCode": 0, "Error": "%s : user not exist" % user_name})

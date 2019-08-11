import logging
import json
import random
from faker import Faker
from flask_restful import Resource, reqparse, fields
from flask import request, jsonify
from ..models import db
from ..models.user import User
from ..models.article import Article


class UserHandler(Resource):
    @staticmethod
    def get(user_id=0):
        res = {
            "Action": "GetOneUser",
            "Message": "get user success",
            "RetCode": 0,
            "Data": dict()
        }
        try:
            user = User.query.filter_by(id=user_id).one()
            logging.info("get user list:%s" % user.to_dict())
            res["Data"] = user.to_dict()
        except Exception as e:
            logging.error("get one user error:%s" % e)
            res["Message"] = "user id not exist"
            res["RetCode"] = -1
        return jsonify(res)

    def post(self):
        res = {
            "Action": "AddOneUser",
            "Message": "add user success",
            "RetCode": 0,
            "Data": dict()
        }
        data = request.get_data()
        json_data = json.dumps(data.decode('utf-8'))
        admin = User(json_data["username"], json_data["email"])
        res["Data"] = admin.to_dict()
        db.session.add(admin)
        db.session.commit()
        return jsonify(res)


class UsersHandler(Resource):
    @staticmethod
    def get():
        res = {
            "Action": "GetAllUser",
            "Message": "get all user success",
            "RetCode": 0,
            "Data": dict()
        }
        # logging.info("get users query string:%s" % request.query_string)
        # print('page=', request.args['page'])
        # print('limit=', request.args['limit'])
        user_list = User.query.all()
        user_dict_list = [i.to_dict() for i in user_list]
        logging.info("get user list:%s" % user_dict_list)
        res["Data"] = user_dict_list
        return jsonify(res)


class FakeDataHandler(Resource):
    def post(self):
        fake = Faker("zh_CN")
        for i in range(40):
            username = fake.name()
            u = User.query.filter_by(username=username).all()
            if len(u) != 0:
                continue
            user = User(username=username, email=fake.email())
            article = Article(username=username,
                              title=fake.text(max_nb_chars=10),
                              content=fake.text(max_nb_chars=200),
                              read_times=random.randint(1, 100000),
                              good=random.randint(1, 100000),
                              bad=random.randint(1, 100000),
                              create_time=fake.date_time(tzinfo=None),
                              update_time=fake.date_time(tzinfo=None),
                              is_delete=0,
                              )
            db.session.add(user)
            db.session.add(article)
        db.session.commit()
        logging.info("fake data for test success!")

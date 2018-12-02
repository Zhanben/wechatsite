import logging
from . import api
from flask import jsonify
from flask_restful import Resource


@api.resource("/")
class Main(Resource):
    def get(self):
        result = {"welcome" : "hello world"}
        logging.info("hello world")
        return jsonify(result)


import logging
from flask_restful import Resource
from flask import request, jsonify
from app.models.article import Article


class ArticleHandler(Resource):
    @staticmethod
    def get(article_id=0):
        res = {
            "Action": "GetOneArticle",
            "Message": "get article detail success",
            "RetCode": 0,
            "Data": dict()
        }
        try:
            article = Article.query.filter_by(id=article_id).one()
            logging.info("get article list:%s" % article.to_dict())
            res["Data"] = article.to_dict()
        except Exception as e:
            logging.error("get one article error:%s" % e)
            res["Message"] = "article id not exist"
            res["RetCode"] = -1
        return jsonify(res)

    @staticmethod
    def put(user_id):
        request.query_string()
        return {'name': 'Hello world %s' % user_id}


class ArticlesHandler(Resource):
    @staticmethod
    def get():
        res = {
            "Action": "GetAllArticle",
            "Message": "get all article success",
            "RetCode": 0,
            "Data": dict()
        }
        # logging.info("get users query string:%s" % request.query_string)
        # print('page=', request.args['page'])
        # print('limit=', request.args['limit'])
        article_list = Article.query.all()
        article_dict_list = [i.to_dict() for i in article_list]
        logging.info("get article list:%s" % article_dict_list)
        res["Data"] = article_dict_list
        return jsonify(res)

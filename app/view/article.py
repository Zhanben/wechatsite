import logging
from flask_restful import Resource
from flask import request, jsonify
from app.models.article import Article
from .base import BaseResponse


class ArticleHandler(Resource):
    @staticmethod
    def get(article_id=0):
        res = BaseResponse(
            data=dict(),
            action="GetOneArticle",
            message="get article detail success",
            ret_code=0,
        )
        try:
            article = Article.query.filter_by(id=article_id).one()
            logging.info("get article list:%s" % article.to_dict())
            res.data = article.to_dict()
        except Exception as e:
            logging.error("get one article error:%s" % e)
            res.message = "article id not exist"
            res.ret_code = -1
        return jsonify(res.to_dict())

    @staticmethod
    def put(user_id):
        request.query_string()
        return {'name': 'Hello world %s' % user_id}


class ArticlesHandler(Resource):
    @staticmethod
    def get():
        res = BaseResponse(
            data=dict(),
            action="GetAllArticle",
            message="get all article success",
            ret_code=0,
        )
        # logging.info("get users query string:%s" % request.query_string)
        # print('page=', request.args['page'])
        # print('limit=', request.args['limit'])
        article_list = Article.query.all()
        article_dict_list = [i.to_dict() for i in article_list]
        logging.info("get article list:%s" % article_dict_list)
        res.data = article_dict_list
        return jsonify(res.to_dict())

from flask_restful import Resource


class BaseResponse(Resource):
    def __init__(self, data=None, message="", action="", ret_code=0):
        if data is None:
            data = dict()
        self.message = message
        self.ret_code = ret_code
        self.action = action
        self.data = data

    def to_dict(self):
        rv = {
            'Message': self.message,
            'RetCode': self.ret_code,
            'Data': self.data,
            'Action': self.action
        }
        return rv

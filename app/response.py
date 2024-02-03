from flask import make_response


class MyResponse:
    header = {
        "Content-Type": "application/json; charset=utf-8"
    }

    @classmethod
    def success(cls,data):
        obj={
            "code":200,
            "data":data,
            "msg":"成功"
        }
        return make_response(obj,200,cls.header)

    @classmethod
    def fail(cls,msg='失败'):
        obj = {
            "code": 500,
            "msg": msg
        }
        return make_response(obj, 200, cls.header)
from flask import Blueprint, request
from exts import db
from response import MyResponse
from blueprints.models import User

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/add',methods=['POST'])
def saveData():
    result=request.json
    username=result['username']
    data=User(username=username)
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)
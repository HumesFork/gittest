from flask import Blueprint, request
from exts import db
from response import MyResponse
from blueprints.models import PointRule

bp = Blueprint('point', __name__, url_prefix='/point')

#获取积分规则
@bp.route('/rule',methods=['GET'])
def getRule():
    item=PointRule.query.first()
    if(item!=None):
        return MyResponse.success(item.to_json())
    else:
        return MyResponse.success(None)

#提交积分规则
@bp.route('/addRule',methods=['POST'])
def addRule():
    result=request.json
    content=result['content']
    data=PointRule(content=content)
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)

#修改积分规则
@bp.route('editRule',methods=['POST'])
def editRule():
    result=request.json
    id=result['id']
    content=result['content']
    data=PointRule.query.filter_by(id=id).first()
    data.content=content
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)


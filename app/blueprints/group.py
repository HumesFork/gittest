from flask import Blueprint, request
from exts import db
from response import MyResponse
from blueprints.models import Group

bp = Blueprint('group', __name__, url_prefix='/group')

#获取阅读群数据
@bp.route('/data',methods=['GET'])
def getGroupData():
    arr=Group.query.all()
    data = []
    for item in arr:
        data.append(item.to_json())
    return MyResponse.success(data)

#新增阅读群组
@bp.route('/add',methods=['POST'])
def addGroup():
    result=request.json
    name=result['name']
    qrcode=result['qrcode']
    status=result['status']
    group=Group(name=name,qrcode=qrcode,status=status)
    db.session.add(group)
    db.session.commit()
    return MyResponse.success(True)

#编辑阅读群组
@bp.route('/edit',methods=['POST'])
def editGroup():
    result=request.json
    name=result['name']
    qrcode=result['qrcode']
    status = result['status']
    id=result['id']
    data=Group.query.filter_by(id=id).first()
    data.name=name
    data.qrcode=qrcode
    data.status=status
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)
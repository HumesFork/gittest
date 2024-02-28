from flask import Blueprint, request
from exts import db
from response import MyResponse
from blueprints.models import Authority

bp = Blueprint('authority', __name__, url_prefix='/authority')

#新增角色
@bp.route('/add',methods=['POST'])
def addRole():
    result=request.json
    name=result['name']
    sign=result['sign']
    account=result['account']
    password=result['password']
    add=result['add']
    edit=result['edit']
    delete=result['delete']
    role=Authority(name=name,sign=sign,account=account,password=password,add=add,edit=edit,delete=delete)
    db.session.add(role)
    db.session.commit()
    return MyResponse.success(True)

#修改角色
@bp.route('/edit',methods=['POST'])
def editRole():
    result=request.json
    name = result['name']
    sign = result['sign']
    account = result['account']
    password = result['password']
    id=result['id']
    add = result['add']
    edit = result['edit']
    delete = result['delete']
    role= Authority.query.filter_by(id=id).first()
    if(role!=None):
        role.name=name
        role.account=account
        role.password=password
        role.add=add
        role.edit=edit
        role.delete=delete
        db.session.add(role)
        db.session.commit()
        return MyResponse.success(True)
    else:
        return MyResponse.fail('没有此用户')

#获取所有角色数据
@bp.route('/allData',methods=['GET'])
def getData():
    arr = Authority.query.all()
    data = []
    for item in arr:
        data.append(item.to_json())
    return MyResponse.success(data)

#删除角色
@bp.route('/del',methods=['POST'])
def delRole():
    result=request.json
    id=result['id']
    data = Authority.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return MyResponse.success(True)

#后台管理账号登陆
@bp.route('/login', methods=['POST'])
def login():
    result = request.json
    name = result['name']
    password = result['password']
    role=Authority.query.filter_by(account=name,password=password).first()
    if (role!=None):
        return MyResponse.success(role.to_json())
    else:
        return MyResponse.success(False)
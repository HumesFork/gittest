from flask import Blueprint, request
from exts import db
from response import MyResponse
from blueprints.models import RecommendBook,RecoomendRule,Reply,User

bp = Blueprint('recommend', __name__, url_prefix='/recommend')

#荐书
@bp.route('/book', methods=['POST'])
def recommend():
    result=request.json;
    name=result['name']
    author=result['author']
    content=result['content']
    date = result['date']
    openid=request.headers.get('token')

    if(len(name)>24 or len(author)>24 or len(content)>400):
        return MyResponse.fail('推荐内容长度过长,请将荐书内容控制在400字以内')
    else:
        recommendBook=RecommendBook(name=name,author=author,content=content,openid=openid,date=date)
        db.session.add(recommendBook);
        db.session.commit()
        return MyResponse.success(True)

#获取全部荐书数据
@bp.route('/allData',methods=['GET'])
def getAllData():
    arr=RecommendBook.query.all()
    data = []
    for item in arr:
        openid=item.openid
        user=User.query.filter_by(openid=openid).first()
        obj=item.to_json()
        if(user!=None):
            obj['user']=user.to_json()
        data.append(obj)
    return MyResponse.success(data)


#根据openid获取荐书数据
@bp.route('/dataByOpenid',methods=['POST'])
def getDataByOpenid():
    openid=request.headers.get('token')
    arr=RecommendBook.query.filter_by(openid=openid)
    data=[]
    for item in arr:
        data.append(item.to_json())
    return MyResponse.success(data)



#删除荐书数据
@bp.route('/delData',methods=['DELETE'])
def delData():
    result=request.json
    id=result['id']
    data=RecommendBook.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return MyResponse.success(True)


#新增/编辑荐书回复
@bp.route('/manageReply',methods=['POST','PUT'])
def manageReply():
    result=request.json
    content=result['content']
    method = request.method
    if (method == 'POST'):
        data = Reply.query.all()
        if (len(data) == 0):
            reply =Reply(content=content)
            db.session.add(reply)
            db.session.commit()
            db.session.flush()
            return MyResponse.success({"id": reply.id})
        else:
            return MyResponse.fail('不能重复添加规则')
    elif (method == 'PUT'):
        id = result['id']
        data = Reply.query.filter_by(id=id).first()
        data.content = content
        db.session.add(data)
        db.session.commit()
        return MyResponse.success({"id": data.id})

#推荐书成功后的回复
@bp.route('/reply',methods=['GET'])
def getReply():
    data = Reply.query.first()
    if (data == None):
        return MyResponse.success({"content": None})
    else:
        return MyResponse.success(data.to_json())

#新增/修改荐书规则
@bp.route('/manageRule',methods=['POST','PUT'])
def manageRule():
    result=request.json
    content=result['content']

    method=request.method
    if(method=='POST'):
        data=RecoomendRule.query.all()
        if(len(data)==0):
            rule=RecoomendRule(content=content)
            db.session.add(rule)
            db.session.commit()
            db.session.flush()
            return MyResponse.success({"id":rule.id})
        else:
           return MyResponse.fail('不能重复添加规则')
    elif(method=='PUT'):
        id = result['id']
        data = RecoomendRule.query.filter_by(id=id).first()
        data.content=content
        db.session.add(data)
        db.session.commit()
        return MyResponse.success({"id":data.id})


#获取荐书规则
@bp.route('/rule',methods=['GET'])
def getRule():
    data=RecoomendRule.query.first()
    if(data==None):
        return MyResponse.success({"content":None})
    else:
        return MyResponse.success(data.to_json())

#推荐书海报
@bp.route('/poster',methods=['GET'])
def getPoster():
    data = {
        "url":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F201509%2F18%2F20150918123814_CUwrK.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1670905474&t=0ba8671352c1101f349eedfa08d47a7b"
    }
    return MyResponse.success(data)

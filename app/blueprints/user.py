from flask import Blueprint, request
from exts import db
from response import MyResponse
import requests
from blueprints.models import User,Book,UserBookList
import xlwt

appId="wx286987d21aeb176a"
appSecret="86fc04af11843f0248b43a5abb93b067"

bp = Blueprint('user', __name__, url_prefix='/user')


#获取openId
@bp.route('/getUnionid',methods=['POST'])
def getUnionId():
    result = request.json
    code=result['code']
    url="https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code" % (appId,appSecret,code)
    res=requests.get(url).json()

    if('errcode' in res):
        return MyResponse.fail()
    else:
        openid=res['openid']
        data = {
            "openid": openid,
            "register":False
        }
        user = User.query.filter_by(openid=openid).first()
        if(user==None):
            return MyResponse.success(data)
        else:
            return MyResponse.success(user.to_json())

#用户第一次注册时，储存用户基本信息
@bp.route('/saveData',methods=['POST'])
def saveData():
    result=request.json
    avatar=result['avatar']
    username=result['username']
    openid=result['openId']
    data=User(openid=openid, register=True,username=username,avatar=avatar,status='normal')
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)

#更新用户信息
@bp.route('/updateData',methods=['POST'])
def updateData():
    result=request.json
    print(result)
    openid = request.headers.get('token')
    avatar = result['avatar']
    username = result['username']
    phoneNumber=result['phoneNumber']
    data= User.query.filter_by(openid=openid).first()
    if(data!=None):
        data.avatar=avatar
        data.username=username
        data.phoneNumber=phoneNumber
        db.session.add(data)
        db.session.commit()
        return MyResponse.success(True)
    else:
        return MyResponse.fail('该用户不存在')


#获取所有用户信息
@bp.route('/allData',methods=['POST'])
def getAllData():
    result=request.json
    openid=result['openid']
    status=result['status']
    phoneNumber=result['phoneNumber']

    arr= []
    if(openid!=''):
        arr= User.query.filter_by(openid=openid).all()
    elif(phoneNumber!=''):
        arr= User.query.filter_by(phoneNumber=phoneNumber).all()

    elif(status!=''):
        arr = User.query.filter_by(status=status).all()
    else:
        arr=User.query.all()
    data = []
    for item in arr:
        data.append(item.to_json())
    return MyResponse.success(data)


#根据openid获取用户个人信息
@bp.route('/data',methods=['GET'])
def getUserData():
    token=request.headers.get('token')
    #拿着token也就是openid去数据库查询
    user=User.query.filter_by(openid=token).first()
    if(user==None):
        return MyResponse.fail('没有此用户')
    else:
       data = user.to_json()
       arr = UserBookList.query.filter_by(openid=token).all()
       books=[]
       for item in arr:
           book=Book.query.filter_by(isbn13=item.bookid).first()
           item=item.to_json()
           if(book!=None):
               item['title']=book.title
               item['author']=book.author
               item['url']=book.image
               books.append(item)
       data['books']=books
       return MyResponse.success(data)

#商务合作接口
@bp.route('/business',methods=['POST'])
def businessCooperate():
    result=request.json
    name=result['name']
    phoneNumber=result['phoneNumber']
    content=result['content']
    return MyResponse.success(True)

#提交读后感
@bp.route('/reading-feel',methods=['POST'])
def commit_reading_feel():
    token = request.headers.get('token')
    result = request.json
    bookid= result['bookId']
    content= result['content']
    timestamp=result['timestamp']
    if(len(content)>400):
        return MyResponse.fail('内容过长')
    book=UserBookList.query.filter(UserBookList.bookid==bookid,UserBookList.openid==token).first()
    book.status='complete'
    book.comments=content
    book.timestamp=timestamp
    db.session.add(book)
    user=User.query.filter_by(openid=token).first()
    #暂定读完为4分
    user.points=4 if user.points==None else user.points+4
    db.session.add(user)
    db.session.commit()
    return MyResponse.success(True)

#放弃阅读
@bp.route('/giveup-reading',methods=['POST'])
def giveupReading():
    token = request.headers.get('token')
    result = request.json
    bookid= result['bookId']
    book=UserBookList.query.filter(UserBookList.bookid==bookid,UserBookList.openid==token).first()
    db.session.delete(book)
    db.session.commit()
    return MyResponse.success(True)

#重新阅读
@bp.route('/re-reading',methods=['POST'])
def reReading():
    token = request.headers.get('token')
    result = request.json
    bookid= result['bookId']
    book=UserBookList.query.filter(UserBookList.bookid==bookid,UserBookList.openid==token).first()
    book.status='reading'
    book.timestamp=None
    db.session.add(book)
    db.session.commit()
    return MyResponse.success(True)

#禁言用户
@bp.route('/disabled',methods=['POST'])
def disableUser():
    result=request.json
    openid=result['openid']
    status=result['status']
    user =User.query.filter_by(openid=openid).first()
    if(user==None):
        return MyResponse.fail('没有此用户')
    else:
        user.status=status
        db.session.add(user)
        db.session.commit()
        return MyResponse.success(True)

#设置用户vip时间段
@bp.route('/setVip',methods=['POST'])
def setVip():
    result=request.json
    date=result['date']
    openid=result['openid']
    dateStr=','.join(date)
    user=User.query.filter_by(openid=openid).first()
    if(user!=None):
        user.vip=dateStr
        db.session.add(user)
        db.session.commit()
        return MyResponse.success(True)
    else:
        return MyResponse.fail('该用户不存在')


#导出用户数据
@bp.route('/exportExcel',methods=['GET'])
def exportExcel():
    # xlwt 库将数据导入Excel并设置默认字符编码为ascii
    workbook = xlwt.Workbook(encoding='ascii')
    # 添加一个表 参数为表名
    worksheet = workbook.add_sheet('用户数据')
    arr = User.query.all()
    data = []
    rowNum=0
    for item in arr:
        colNum=0
        row=item.to_json()
        for key,value in row.items():
            worksheet.write(rowNum, colNum, value)
            colNum+=1
        rowNum+=1
    # 保存excel文件
    #workbook.save('excelTest.xls')
    return MyResponse.success(True)
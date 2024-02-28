
from flask import Blueprint, request
from exts import db
from response import MyResponse
from blueprints.models import Community,Mood,Poster,User,UserBookList


bp = Blueprint('community', __name__, url_prefix='/community')

#新增心情
@bp.route('/addMoods',methods=['POST'])
def addMoods():
    result=request.json
    name=result['name']
    url=result['url']
    status=result['status']
    data=Mood(name=name,url=url,status=status)
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)

#删除心情
@bp.route('/delMoods',methods=['POST'])
def delMoods():
    result = request.json
    id=result['id']
    data =Mood.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return MyResponse.success(True)

#修改心情
@bp.route('/editMoods',methods=['POST'])
def editMoods():
    result = request.json
    name = result['name']
    url = result['url']
    status = result['status']
    id = result['id']
    data = Mood.query.filter_by(id=id).first()
    data.name=name
    data.url=url
    data.status=status
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)


#获取心情
@bp.route('/mood',methods=['GET'])
def getMood():
    arr=Mood.query.all()
    data = []
    for item in arr:
        data.append(item.to_json())
    return MyResponse.success(data)

#新增打卡分享海报
@bp.route('/addPoster',methods=['POST'])
def addPoster():
    result=request.json
    name=result['name']
    url=result['url']
    status=result['status']
    data=Poster(name=name,url=url,status=status)
    db.session.add(data)
    db.session.commit()
    return MyResponse.success(True)

#修改海报
@bp.route('/editPoster',methods=['POST'])
def editPoster():
    result = request.json
    name = result['name']
    url = result['url']
    status = result['status']
    id = result['id']
    data = Poster.query.filter_by(id=id).first()
    if(data==None):
        return MyResponse.fail('删除数据不存在')
    else:
        if(status==True):
         db.session.query(Poster).filter(Poster.status == True).update({'status': False})
        else:
         pass
        data.name = name
        data.url = url
        data.status = status
        db.session.add(data)
        db.session.commit()
        return MyResponse.success(True)

#删除海报
@bp.route('delPoster',methods=['POST'])
def delPoster():
    result = request.json
    id = result['id']
    data = Poster.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return MyResponse.success(True)

#获取打卡分享海报全部数据
@bp.route('/allPoster',methods=['GET'])
def getAll():
    arr = Poster.query.all()
    data = []
    for item in arr:
        data.append(item.to_json())
    return MyResponse.success(data)

#小程序端获取打卡分享海报
@bp.route('/poster',methods=['GET'])
def getPoster():
    data=Poster.query.filter_by(status=True).first()
    if(data!=None):
      return MyResponse.success(data.to_json()['url'])
    else:
        return MyResponse.success('')

#用户打卡
@bp.route('/clockIn',methods=['POST'])
def clockIn():
    result=request.json
    username=result['username']
    content=result['content']
    date=result['date']
    duration=result['duration']
    bookName=result['bookName']
    bookid=result['bookId']
    mood=result['mood']
    avatar=result['avatar']
    url=result['url']
    moodName=result['moodName']
    openid=request.headers.get('token')
    if(len(content)>600 or len(bookName)>24 or openid==None):
        return MyResponse.fail('参数错误')
    else:
        userbook=UserBookList.query.filter(UserBookList.bookid==bookid,UserBookList.openid==openid).first()
        if(userbook==None):
            data=UserBookList(openid=openid,bookid=bookid,status='reading',duration=duration)
            db.session.add(data)
        else:
            if(userbook.status=='complete'):
                return MyResponse.fail('您已读完此书，请到我的书架点击重读')
            userbook.duration+=duration
            db.session.add(userbook)
        #进行积分计算,打卡暂定为1分
        user=User.query.filter_by(openid=openid).first()
        user.points=1 if user.points==None else user.points+1
        db.session.add(user)
        clockdata=Community(username=username,content=content,date=date,duration=duration,bookName=bookName,
                            bookid=bookid,mood=mood,avatar=avatar,openid=openid,moodName=moodName,url=url)
        db.session.add(clockdata)
        db.session.flush()
        db.session.commit()
        return MyResponse.success(clockdata.to_json())

#获取用户打卡历史记录
@bp.route('/history',methods=['POST'])
def getHistory():
    result=request.json
    year=result['year']
    month=result['month']
    openid=request.headers.get('token')
    #此处应根据时间段查询和用户openid，需要优化
    arr=Community.query.filter_by(openid=openid).order_by(Community.date.desc()).all()
    data=[]
    for item in arr:
        data.append(item.to_json())
    return MyResponse.success(data)


#根据Id获取打卡详情
@bp.route('/getById',methods=['GET'])
def getClockInById():
    id = request.args.get('id')
    data = Community.query.filter_by(id=id).first()
    if(data!=None):
        return MyResponse.success(data.to_json())
    else:
        return MyResponse.fail('未查询到该数据')



#获取社区数据
@bp.route('/data',methods=['POST'])
def getData():
    result=request.json
    currentPage=1 if result['currentPage']==None else result['currentPage']
    limit=20 if (result['limit']==None or result['limit']>100) else result['limit']
    searchContent=result['searchContent']
    if(searchContent!=None and searchContent!=""):
        res=Community.query.filter(Community.content.like("%" + searchContent + "%")
                                   ).offset(limit*(currentPage-1)).limit(limit).all()
        data = []
        for item in res:
            data.append(item.to_json())
        return MyResponse.success(data)

    if(type(currentPage)!=int or type(limit)!=int):
        return MyResponse.fail('参数错误')
    else:
        arr=Community.query.order_by(Community.date.desc()).offset(limit*(currentPage-1)).limit(limit).all()
        data = []
        for item in arr:
            data.append(item.to_json())
        return MyResponse.success(data)

#删除打卡数据
@bp.route('/delData',methods=['POST'])
def delData():
    result = request.json
    id = result['id']
    data = Community.query.filter_by(id=id).first()
    db.session.delete(data)
    db.session.commit()
    return MyResponse.success(True)


from flask import Blueprint, request
from exts import db
from response import MyResponse
from blueprints.models import Book,BookList

bp = Blueprint('mall', __name__, url_prefix='/mall')


# 获取书单数据
@bp.route('/booklist', methods=['GET'])
def booklist():
    arr=BookList.query.all()
    data=[]
    if(arr==None):
        return MyResponse.fail('暂无书单')
    else:
        for item in arr:
            books=[]
            for book in item.books:
                books.append(book.to_json())

            tmp=item.to_json()
            tmp['books']=books
            data.append(tmp)

        return MyResponse.success(data)

#新增书单
@bp.route('/booklist/add',methods=['POST'])
def addBooklist():
    result=request.json
    name=result['name']
    introduction=result['introduction']
    if(len(name)>24 or len(introduction)>200):
        return MyResponse.fail('参数错误')
    else:
        booklist=BookList(name=name,introduction=introduction)
        db.session.add(booklist)
        db.session.commit()
        return MyResponse.success(True)

# 获取全部图书
@bp.route('/books/all', methods=['GET'])
def bookAll():
    arr=Book.query.all()
    data=[]
    if(arr==None):
        return MyResponse.fail('暂无图书')
    else:
        for item in arr:
            data.append(item.to_json())

        return MyResponse.success(data)


# 获取单本图书详情
@bp.route('/books/<int:id>', methods=['GET'])
def getBookById(id):
   book=Book.query.filter_by(id=id).first()
   if(book==None):
       return MyResponse.fail('未查询到该书目')
   else:
       data = book.to_json()
       return MyResponse.success(data)


# banner数据
@bp.route('/banner', methods=['POST'])
def getBanner():
    data = [
        {
            "url": "https://th.bing.com/th/id/R.d4a90675f83625d6a932a81ce096c877?rik=usZ9rHnjABVFFQ&riu=http%3a%2f%2ftvax1.sinaimg.cn%2flarge%2f9afb97dagy1g3ny3ntpjmj21hc0u0e81.jpg&ehk=VNJR8cOH1Tdz61t8KhWWrZ2IjqT2i8cFyzQXhou6Dc4%3d&risl=&pid=ImgRaw&r=0",
            "sort": 7
        },
        {
            "url": "https://th.bing.com/th/id/R.0222bad3d2ccffe16bc5446e3f23bf90?rik=RQRsAZJ%2fL8vaAg&riu=http%3a%2f%2ftvax1.sinaimg.cn%2flarge%2f9afb97dagy1g3ny3v0jqoj21hc0u0gtf.jpg&ehk=hsc4%2b0%2fugpn9NvU2H59D8VAIY7kaPhozb1QHiZgPn4c%3d&risl=&pid=ImgRaw&r=0",
            "sort": 3
        }
    ]
    return MyResponse.success(data)

# 新增单本图书
@bp.route('/books/add', methods=['POST'])
def addBook():
    result = request.json;

    return MyResponse.success(True)


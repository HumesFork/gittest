from flask import Blueprint, request
from exts import db
from response import MyResponse
import requests
from sqlalchemy import or_
from blueprints.models import Book
from utils import Utils

bp = Blueprint('ali', __name__, url_prefix='/ali')

@bp.route('/getToken',methods=['GET'])
def getToken():
    return Utils.getSts()

#根据isbn查询图书数据
@bp.route('/getInfoByIsbn',methods=['POST'])
def getInfoByIsbn():
    result=request.json
    isbn=result['isbn']
    headers={
        "Authorization": "APPCODE 3613bc8aacff422cac42b7d2263df418"
    }
    url = "https://isbn.market.alicloudapi.com/ISBN?is_info=0&isbn=%s" % (isbn)
    arr=Book.query.filter(or_(Book.isbn10==isbn,Book.isbn13==isbn)).all()
    if(len(arr)==0):
        res = requests.get(url, headers=headers).json()
        print(res)
        if(res['error_code']!=0):
            return MyResponse.success(False)
        else:
            data=res['result']
            author=data['author']
            if (author == None):
                return MyResponse.fail('未查询到该书籍')
            pubdate=data['pubdate']
            binding=data['binding']
            pages=data['pages']
            image=data['images_medium']
            publisher=data['publisher']
            isbn10=data['isbn10']
            isbn13=data['isbn13']
            title=data['title']
            summary=data['summary']
            summary=summary[0:500] if len(summary)>500 else summary
            price=data['price']
            book=Book(author=author,pubdate=pubdate,binding=binding,pages=pages,image=image,publisher=publisher,
                      isbn10=isbn10,isbn13=isbn13,title=title,summary=summary,price=price)
            db.session.add(book)
            db.session.commit()
            db.session.flush()
            data=[]
            data.append(book.to_json())
            return MyResponse.success(data)
    else:
        data = []
        for item in arr:
            data.append(item.to_json())
        return MyResponse.success(data)

#接收上传图片
@bp.route('/uploadFile',methods=['POST'])
def uploadFile():
    result=request.json
    url=result['url']
    return MyResponse.success(True)
from exts import db

# 定义用户数据模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    username = db.Column(db.String(24))
    avatar = db.Column(db.String(100))
    phoneNumber = db.Column(db.String(11))
    openid=db.Column(db.String(40), unique=True)
    register=db.Column(db.Boolean)
    vip=db.Column(db.String(100))
    #用户是否被禁言
    status=db.Column(db.String(24))
    points=db.Column(db.Float)

    def to_json(self):
        return {
            "username":self.username,
            "avatar":self.avatar,
            "phoneNumber":self.phoneNumber,
            "openid":self.openid,
            "register":self.register,
            "status":self.status,
            "points":self.points,
            "vip":self.vip
        }

#用户正在读，读完的书籍和阅读时常模型
class UserBookList(db.Model):
    __tablename__ = 'user_booklist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    openid = db.Column(db.String(40))
    #用户关联这本书的状态[reading,complete]
    status=db.Column(db.String(24))
    bookid =db.Column(db.String(13))
    duration=db.Column(db.Float)
    comments=db.Column(db.String(400))
    timestamp=db.Column(db.BigInteger)

    def to_json(self):
        return {
            "openid": self.openid,
            "status": self.status,
            "bookid": self.bookid,
            "duration":self.duration,
            "comments":self.comments,
            "timestamp":self.timestamp
        }


#书单模型,书单和书是一对多关系
class BookList(db.Model):
    __tablename__ = 'booklist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column(db.String(24))
    introduction = db.Column(db.String(100))
    books=db.relationship('Book',backref='booklist')

    def to_json(self):
        return{
            "id":self.id,
            "name":self.name,
            "introduction":self.introduction,
            "books":self.books
        }

# 定义书数据模型
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    title = db.Column(db.String(24))
    price = db.Column(db.Float)
    author = db.Column(db.String(24))
    pubdate=db.Column(db.String(24))
    binding=db.Column(db.String(24))
    pages=db.Column(db.String(24))
    image=db.Column(db.String(200))
    publisher=db.Column(db.String(24))
    isbn10=db.Column(db.String(10))
    isbn13=db.Column(db.String(13))
    summary=db.Column(db.String(1000))
    likes = db.Column(db.Integer)
    booklist_id=db.Column(db.Integer,db.ForeignKey('booklist.id'))

    def to_json(self):
        return {
            "id":self.id,
            "title":self.title,
            "price":self.price,
            "author":self.author,
            "pubdate":self.pubdate,
            "binding":self.binding,
            "pages":self.pages,
            "image":self.image,
            "publisher":self.publisher,
            "isbn10":self.isbn10,
            "isbn13":self.isbn13,
            "summary":self.summary,
            "likes":self.likes,
            "booklist_id":self.booklist_id
        }

#荐书模型
class RecommendBook(db.Model):
    __tablename__ = 'recommend'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(24))
    author = db.Column(db.String(24))
    content = db.Column(db.String(400))
    openid=db.Column(db.String(30))
    date=db.Column(db.BigInteger)
    #status=db.Column(db.Boolean)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "author":self.author,
            "content":self.content,
            "openid":self.openid,
            "date":self.date
        }

#荐书规则模型
class RecoomendRule(db.Model):
    __tablename__ = 'recommend_rule'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200))

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content
        }

#回复管理数据模型
class Reply(db.Model):
    __tablename__ = 'recommend_reply'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300))

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content
        }



#群组模型
class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(24))
    qrcode=db.Column(db.String(100))
    status=db.Column(db.Boolean)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "qrcode":self.qrcode,
            "status":self.status
        }

#社区打卡模型
class Community(db.Model):
    __tablename__ = 'community'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    openid=db.Column(db.String(30))
    username = db.Column(db.String(24))
    content= db.Column(db.String(600))
    date=db.Column(db.BigInteger)
    duration=db.Column(db.Float)
    bookName=db.Column(db.String(24))
    bookid=db.Column(db.String(24))
    mood=db.Column(db.String(24))
    moodName=db.Column(db.String(10))
    avatar=db.Column(db.String(100))
    url=db.Column(db.String(100))

    def to_json(self):
        return {
            "id":self.id,
            "openid":self.openid,
            "username":self.username,
            "content":self.content,
            "date":self.date,
            "duration":self.duration,
            "bookName":self.bookName,
            "bookid":self.bookid,
            "mood":self.mood,
            "moodName":self.moodName,
            "avatar":self.avatar,
            "url":self.url
        }

#心情模型
class Mood(db.Model):
    __tablename__ = 'mood'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(24))
    url = db.Column(db.String(200))
    status=db.Column(db.Boolean)
    remarks=db.Column(db.String(100))
    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "url":self.url,
            "status":self.status
        }
#海报模型
class Poster(db.Model):
    __tablename__ = 'poster'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(24))
    url = db.Column(db.String(200))
    status = db.Column(db.Boolean)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "status": self.status
        }

#角色模型
class Authority(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(24))
    sign= db.Column(db.String(24),unique=True)
    account=db.Column(db.String(24))
    password= db.Column(db.String(64))
    add=db.Column(db.Boolean)
    edit=db.Column(db.Boolean)
    delete=db.Column(db.Boolean)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "sign": self.sign,
            "account": self.account,
            "password":self.password,
            "add":self.add,
            "edit":self.edit,
            "delete":self.delete
        }

#积分规则模型
class PointRule(db.Model):
    __tablename__ = 'point_rule'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(400))
    def to_json(self):
        return {
            "id": self.id,
            "content": self.content
        }
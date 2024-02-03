from exts import db

# 定义用户数据模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,index=True)
    username = db.Column(db.String(24))

    def to_json(self):
        return {
            "username":self.username,
            
        }
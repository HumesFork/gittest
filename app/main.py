

from flask import Flask,request
from flask import render_template #引入模板插件
import test
from exts import db
import re
#自己的模块
from response import MyResponse
from blueprints import userbp

app = Flask(__name__,template_folder = "./vue/dist", static_folder="./vue/dist",static_url_path="")
#设置数据库
app.config.from_object(test)
# 关闭动态追踪修改的警告信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app=app

#创建数据库表
with app.app_context():
    db.create_all()

#全局错误处理
@app.errorhandler(Exception)
def error_handler(e):
    print(e)
    return MyResponse.fail('服务器内部错误,请联系相关人员')

#防止sql注入攻击
@app.before_request
def before_request():
    print(request.method)
    #假设是post请求，data为传入的请求参数
    if(request.method=='POST'):
        data =request.json
        for v in data.values():
            v= str(v).lower()
            pattern = r"\b(and|like|exec|insert|select|drop|grant|alter|delete|update|count|chr|mid|master|truncate|char|delclare|or)\b|(\*|;)"
            r = re.search(pattern,v)
            if r:
                return '请输入规范的参数！'
    # 假设是get请求，data为传入的请求参数
    if(request.method=='GET'):
        data = request.headers.get('token')
        v = str(data).lower()
        pattern = r"\b(and|like|exec|insert|select|drop|grant|alter|delete|update|count|chr|mid|master|truncate|char|delclare|or)\b|(\*|;)"
        r = re.search(pattern, v)
        if r:
            return '请输入规范的参数！'
    # 假设是get请求，data为传入的请求参数
    if (request.method == 'GET'):
        data = request.args
        for v in data.values():
            v = str(v).lower()
            pattern = r"\b(and|like|exec|insert|select|drop|grant|alter|delete|update|count|chr|mid|master|truncate|char|delclare|or)\b|(\*|;)"
            r = re.search(pattern, v)
            if r:
                return '请输入规范的参数！'


app.register_blueprint(userbp)

@app.route('/')
def index():
    #使用模板插件，引入index.html。此处会自动Flask模板文件目录寻找index.html文件。
   return render_template('index.html',name='index') 

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=80)
# 开发数据库的配置变量
# HOSTNAME = 'sh-cynosdbmysql-grp-6a7exflc.sql.tencentcdb.com'
# PORT = '23560'
# DATABASE = 'first'
# USERNAME = 'root'
# PASSWORD = 'ROOT123456&'
# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# SQLALCHEMY_DATABASE_URI = DB_URI
# SQLALCHEMY_TRACK_MODIFICATIONS=True

# 线上数据库的配置变量
HOSTNAME = '10.24.101.28'
PORT = '3306'
DATABASE = 'first'
USERNAME = 'root'
PASSWORD = 'ROOT123456&'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=True
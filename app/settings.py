import os


class Config(object):
    SECRET_KEY = 'super secret key'  # 這個是配置一個密鑰（使用session就要配置密鑰）
    SESSION_TYPE = 'redis'  # 這個是配置session存儲在哪
    PERMANENT_SESSION_LIFETIME = 60  # 這個是配置session的存活時間
    DATABASE_URI = {
        'dialect': 'mysql',  # 数据库
        'driver': 'pymysql',  # 驱动
        'username': 'mhh123',
        'password': 'mhh123',
        'host': '127.0.0.1',
        'port': 3306,
        'databases': 'my_flask_project'  # 数据库名
    }
    # 'SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mhh123:mhh123@127.0.0.1:3306/my_flask'
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
        DATABASE_URI['dialect'], DATABASE_URI['driver'],
        DATABASE_URI['username'], DATABASE_URI['password'],
        DATABASE_URI['host'], DATABASE_URI['port'],
        DATABASE_URI['databases']
    )

    DEBUG = False
    TESTING = False


class Develop(Config):
    DEBUG = True


class Test(Config):
    TESTING = True


class Product(Config):
    DEBUG = False
    TESTING = False


env = {
    'develop': Develop,
    'test': Test,
    'product': Product
}
UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
FC_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
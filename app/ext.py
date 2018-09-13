from flask_cache import Cache
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
cache = FlaskRedis()
db = SQLAlchemy()


def init_ext(app):

    Session(app=app)
    # with app.app_context():
    db.init_app(app)
    cache.init_app(app=app)
    migrate = Migrate(app=app, db=db)  ## 用来绑定app和db到flask_migrate的

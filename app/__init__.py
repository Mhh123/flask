# encoding:utf-8
from app.settings import env
from app.ext import init_ext
from app.home.views import home_blueprint
from app.admin.views import admin_blueprint



from flask import Flask


def create_app(param):
    app = Flask(__name__)
    app.config.from_object(env.get(param))  # 建议把配置项放在前面；避免有时候放后面，配置项不起效
    init_ext(app)

    app.register_blueprint(blueprint=home_blueprint)
    app.register_blueprint(blueprint=admin_blueprint)
    return app

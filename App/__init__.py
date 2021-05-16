from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import envs
from App.utils.middle_ware import load_middleware


def creaate_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    # 初始化插件
    init_ext(app)

    #  路由
    # app.register_blueprint(blueprint=my_blue)


    # 注册中间件
    load_middleware(app)

    # 注册api
    init_api(app)
    return app
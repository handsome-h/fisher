from flask import Flask


def create_app():
    app = Flask(__name__)
    # 读取配置文件（配置变量名要大写），名称可以自定义。这种方式导入，要求键名为大写
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

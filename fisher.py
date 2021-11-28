from flask import Flask, make_response, jsonify

app = Flask(__name__)
# 读取配置文件（配置变量名要大写），名称可以自定义。这种方式导入，要求键名为大写
app.config.from_object('config')


# 注解、装饰器，这种路由方式，优雅，但不够灵活。底层源码还是去调用的app.add_url_rule('/hello', view_func=hello)
@app.route('/hello')
def hello():
    """Controller
    视图函数，代码不宜过长
    """
    headers = {
        'content-type': 'text/html',
        # 'content-type': 'application/json',
    }
    response = make_response("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        图片
    </body>
    </html>
    """)
    response.headers = headers
    return response
    # 当返回一个元组的时候，flask内部会封装为一个response对象
    # return './zzy.html', 200, headers
    return 'Hello, world'


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    图书搜索接口
    :param q: 搜索关键词
    :param page: 页码
    :return:
    """
    # 发送http请求
    # 格式化结果
    # jsonify(result)
    return q, page


# 同样可以注册路由
# app.add_url_rule('/hello', view_func=hello)


if __name__ == '__main__':
    # 生产环境下，不会直接用flask这个框架的服务来直接启动(python fisher.py)，而是 nginx+uwsgi 这种方式
    # app.run(debug=app.config['DEBUG'])
    # 外部访问，可修改端口
    # app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

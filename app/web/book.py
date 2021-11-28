from flask import make_response, Blueprint
from yushu_book import YuShuBook

# 蓝图（蓝本），blueprint
# 蓝图和flask核心对象app的接口几乎一样，但不能认为蓝图就是app
web = Blueprint('web', __name__)


# 注解、装饰器，这种路由方式，优雅，但不够灵活。底层源码还是去调用的app.add_url_rule('/hello', view_func=hello)
@web.route('/hello')
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


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    图书搜索接口
    :param q: 搜索关键词
    :param page: 页码
    :return:
    """
    # 发送http请求
    YuShuBook.search_by_keywords(q)
    # 格式化结果
    # jsonify(result)
    return q, page

# 同样可以注册路由
# app.add_url_rule('/hello', view_func=hello)

from flask import make_response, request

from . import web
from app.forms.book import SearchForm
from yushu_book import YuShuBook


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

@web.route('/book/search2')
def search2():
    """
    图书搜索接口，通过request获取查询参数
    """
    # request是一个代理模式，需要有上下文才能使用，直接使用request是没有东西的
    # q = request.args.get('q')
    # print(q)

    # 验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        return q
    else:
        return form.errors

from app import create_app
# 主启动流程
app = create_app()


if __name__ == '__main__':
    # 生产环境下，不会直接用flask这个框架的服务来直接启动(python fisher.py)，而是 nginx+uwsgi 这种方式
    # app.run(debug=app.config['DEBUG'])
    # 外部访问，可修改端口
    # app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

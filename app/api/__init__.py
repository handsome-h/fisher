# 蓝图（蓝本），blueprint
# 蓝图和flask核心对象app的接口几乎一样，但不能认为蓝图就是app
from flask import Blueprint

web = Blueprint('api', __name__)

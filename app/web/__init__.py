# 蓝图（蓝本），blueprint
# 蓝图和flask核心对象app的接口几乎一样，但不能认为蓝图就是app
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user

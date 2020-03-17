# -*- coding:utf-8 -*-

'''
@author: eric
@file: __init__.py
@time: 2020/3/17 14:20
'''

from flask import Blueprint

#两个必要参数'web'蓝图名字;'__name__'蓝图所在的模块或者包，一般为'__name__'变量
web = Blueprint("web",__name__)

#下面两个模块应该在蓝图下面，是为了防止循环导入
from app.web import book
from app.web import user

# -*- coding:utf-8 -*-

'''
@author: eric
@file: __init__.py
@time: 2020/3/17 14:20
'''

from flask import Flask

def create_app():
    app = Flask(__name__)
    # fishWeb实例导入配置文件，接收模块的路径
    app.config.from_object('config')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
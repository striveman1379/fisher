# -*- coding:utf-8 -*-

'''
@author: eric
@file: fisher.py
@time: 2020/3/15 10:39
'''

from flask import Flask
# from config import DEBUG,PORT
from app.web import book


fishWeb = Flask(__name__)
#fishWeb实例导入配置文件，接收模块的路径
fishWeb.config.from_object('config')

@fishWeb.route('/')
def index():
    return "this is my page"

@fishWeb.route('/hello')
def hello():
    #status code 200.404.301
    #content-type http headers
    #content-type的默认值为text/html，会指导浏览器把<html></html>当做html格式的内容来解析
    #视图函数中，返回的都是response对象
    headers = {
        'content-type':"application/json",
        'location':'http://www.bing.com'
    }
    return '<html></html>',301,headers

#使用基于类的试图（即插视图），用add_url_rule 类似于django
# fishWeb.add_url_rule('/hello', view_func=hello)

#加上if __name__ ,可以保证在生产环境下，不会启动flask自带的web服务器
if __name__ == '__main__':
    # fishWeb.run(host='0.0.0.0', port=PORT, debug=DEBUG)
    #生产环境下部署服务，通常用nginx+uwsgi，nginx接收前端请教（返回静态页面），uwsgi接收动态请求
    #生产环境下，flask项目的启动不是用python fisher.py的手动输入的形式来执行，而是由uwsgi加载fisher.py模块来启动
    #生产环境下，fisher.py文件不再是入口文件，而是uwsgi加载的模块文件
    #生产环境下，app.run()不会执行
    fishWeb.run(host='0.0.0.0', port=86, debug=fishWeb.config['DEBUG'])


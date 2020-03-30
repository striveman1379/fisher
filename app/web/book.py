# -*- coding:utf-8 -*-

'''
@author: eric
@file: book.py
@time: 2020/3/16 16:39
'''

from flask import Flask,jsonify,request
# from config import DEBUG,PORT
from helper import is_isbn_or_key
from yushu_book import YuShuBook

from . import web
from app.forms.book import SearchForm


#蓝图中的视图函数的名字不能和蓝图对象的名字一样！！！即下面的函数名不能为web
#<>尖括号中的内容为参数
@web.route('/book/search')
def search():
    """
    搜索中不做关键组区分
        q：普通关键字   isbn搜索
        isbn13 13个0-9的数字组成
        isbn10 10个0-9数字组成，含有一些 “-”
        page
        ？q=金庸&page=1
        request 获取几乎全部的HTTP的请求信息，包括查询参数  POST参数  remote  IP等
    :return:
    """

    #通过request来获取查询参数(？q=金庸&page=1)

    # q至少要有一个字符，长度也应该有限制
    # q = request.args["q"]
    #页数必须为正整数，也要有一个最大值限制
    # page = request.args["page"]

    # 验证层
    form = SearchForm(request.args)
    #调用form的validate来验证
    if form.validate():     #验证为true时
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        #dict序列化
        return jsonify(result)  #等同于下行代码
        # return json.dumps(result),200,{'content-type':'application/json'}
    else:
        return jsonify({"msg":"参数校验失败"})
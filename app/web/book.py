# -*- coding:utf-8 -*-

'''
@author: eric
@file: book.py
@time: 2020/3/16 16:39
'''

from flask import Flask,jsonify
# from config import DEBUG,PORT
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from fisher import fishWeb

#<>尖括号中的内容为参数
@fishWeb.route('/book/search/<q>/<page>')
def search(q,page):
    """
    搜索中不做关键组区分
        q：普通关键字   isbn搜索
        isbn13 13个0-9的数字组成
        isbn10 10个0-9数字组成，含有一些 “-”
        page

    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    #dict序列化
    return jsonify(result)  #等同于下行代码
    # return json.dumps(result),200,{'content-type':'application/json'}

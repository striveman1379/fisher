# -*- coding:utf-8 -*-

'''
@author: eric
@file: yushu_book.py
@time: 2020/3/16 15:47
'''
from http_fish import HTTP

class YuShuBook:

    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls,keyword,count = 15,start=0):
        url = cls.isbn_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result

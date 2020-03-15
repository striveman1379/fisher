# -*- coding:utf-8 -*-

'''
@author: eric
@file: helper.py
@time: 2020/3/15 19:06
'''


def is_isbn_or_key(word):
    """
    :param word: word为搜索框中输入的内容，判断是书名，作者，还是isbn编号
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"

    short_word = word.replace("-", "")
    if "-" in word and short_word == 10 and short_word.isdigit():
        isbn_or_key = "isbn"
    return isbn_or_key

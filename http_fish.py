# -*- coding:utf-8 -*-

'''
@author: eric
@file: http.py
@time: 2020/3/16 11:02
'''

#发送http请求，两个库，urllib和requests

import requests

class HTTP:
    @staticmethod
    def get(url, return_json = True):
        r = requests.get(url)
        #restful风格的api一般返回json格式的数据
        #return_json参数用来控制返回的数据格式，看需求返回json格式数据，或是文本格式
        #可以根据状态码来返回结果
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if return_json:
        #     return r.json()
        # else:
        #     return r.text






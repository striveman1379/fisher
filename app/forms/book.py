# -*- coding:utf-8 -*-

'''
@author: eric
@file: book.py
@time: 2020/3/27 17:36
'''

from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange

class SearchForm(Form):
    q = StringField(validators=[Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)

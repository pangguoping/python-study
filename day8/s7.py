#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
#创建有序字典：
"""


class MyDict(dict):
    def __init__(self):
        self.li = []
        super(MyDict,self).__init__()
    def __setitem__(self, key, value):
        self.li.append(key)
        super(MyDict,self).__setitem__(key,value)
    def __str__(self):
        temp_list = []
        for key in self.li:
            value = self.get(key)
            temp_list.append("'%s':%s" %(key,value))
            #print(temp_list)
        temp_str = "{" + ",".join(temp_list) + "}"
        return temp_str

obj = MyDict()
obj['k1'] = 123
obj['k2'] = 456
print(obj)
"""
#类的单例模式
"""

class Foo:
    instance = None
    def __init__(self,name):
        self.name = name

    @classmethod
    def get_instance(cls):
        #cls 类名
        if cls.instance:
            return cls.instance
        else:
            obj = cls('google')
            cls.instance = obj
            return obj
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
"""

#异常处理
while True:
    num1 = input('num1:')
    num2 = input('num2:')
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2

    except Exception as ex:
        print(ex)


class yichException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise yichException('我的异常')
except yichException,e:
    print e











#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

#公共字段
'''


class Foo:
    def __init__(self,name):
        self.name = name  #公共的
    def f1(self):
        print(self.name)


obj = Foo('alex')
print(obj.name)
obj.f1()

'''

#私有字段
class Foo:
    def __init__(self,name):
        self.__name = name  #私有的
    def f1(self):
        print(self.__name)


obj = Foo('alex')
#print(obj.__name)
obj.f1()

#私有字段
class Foo:
    __cc = "123"
    def __init__(self,name):
        self.__name = name
    def f1(self):
        print(self.__name)
    @staticmethod
    def f3():
        print(Foo.__cc)

Foo.f3()
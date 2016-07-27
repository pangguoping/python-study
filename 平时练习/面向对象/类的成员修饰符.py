#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
'''

class Foo:
    def __init__(self,name):
        self.__name = name
    def f1(self):
        print(self.__name)   #self.name 在类的内部访问

obj = Foo('baidu')
print(obj.__name)  #self.__name只能在类的内部访问
#obj.f1()

'''
class Foo:
    __cc = "123"  #创建私有静态字段
    def __init__(self):
        pass
    @staticmethod
    def f3():
        print(Foo.__cc)

Foo.f3()  #使用类访问，也可以使用实例对象访问
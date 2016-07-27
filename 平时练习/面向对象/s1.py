#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping  4008167189
#构造方法
class SQLHelper:
    def __init__(self,a1,a2,a3): #此时的self就是obj1。哪个对象执行方法，self就是谁
        print('自动执行init')
        self.hhost = a1
        self.uusername = a2
        self.pwd = a3
        print(self.hhost)
        print(self)
    def fetch(self,sql):
        pass
    def create(self,sql):
        pass
    def remove(self,nid):
        pass
    def modify(self,name):
        pass
obj1 = SQLHelper('WWw.BAIDU.COM','alex','123')   #类名后面加()，自动执行类中的def  __init__()构造方法
##################################
#类的封装
'''

class Person:
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money
    def shopping(self):
        self.money = self.money - 2
        print(self.money)

bao = Person('庞国平',73,10)
bao.shopping()
#可以封装对象
class c1:
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj
class c2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name)

c2_obj = c2('aa',11)
c1_obj = c1("baidu",c2_obj)
print(c1_obj.obj.age)

'''
#对象嵌套封装
class c1:
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj
class c2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name)
class c3:
    def __init__(self,a1):
        self.money = 123
        self.aaa = a1

c2_obj = c2('c2_name',11)
#c2_obj是c2类型
#name = "aa"
c1_obj = c1("baidu",c2_obj)
#c1_obj 是c1类型
#name = "baidu"
#obj = c2_obj
c3_obj = c3(c1_obj)
print(c3_obj.aaa)
#使用c3_obj执行show方法:  c3_obj.aa.obj.show()
print(c3_obj.aaa.obj.show())
#使用c3_obj找到c2中的name,使用c3_obj.aaa.obj.name
print(c3_obj.aaa.obj.name)
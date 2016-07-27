#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
'''


import tarfile
#压缩
tar = tarfile.open('your.tar','w')
tar.add('ooo.xml',arcname='ooo.xml')
tar.close()
#解压全部文件
tar = tarfile.open('your.tar','r')
tar.extractall()
tar.close()
#解压指定文件
for item in tar.getmembers():
    print(item,type(item))
obj = tar.getmember('ooo.xml')
tar.extract(obj)
tar.close()
'''
'''

class SQLHelper:
    def fetch(self,sql):
        print(sql)
        print(self.hhost)
        print(self.uusername)
        print(self.pwd)

    def create(self,sql):
        pass
    def remove(self,sql):
        pass
    def modify(self,sql):
        pass

obj = SQLHelper()
obj.hhost = "c1.host.com"
obj.uusername = "alex"
obj.pwd = "123"

obj.fetch("select * from A")
'''
'''

class SQLHelper:
    def __init__(self,a1,a2,a3):
        print('自动执行init')
        self.hhost = a1
        self.uusername = a2
        self.pwd = a3
        print(self.hhost)
    def fetch(self,sql):
        pass
    def create(self,sql):
        pass
    def remove(self,nid):
        pass
    def modify(self,name):
        pass
obj1 = SQLHelper('WWw.BAIDU.COM','alex','123')
obj2 = SQLHelper('alyu.mysql.com','alex','1233')
'''
'''

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
c1_obj = c1('alex',c2_obj)
print(c1_obj.obj)
print(c1_obj.obj.age)
'''
'''

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

c2_obj = c2('aa',11)
c1_obj = c1('alex',c2_obj)
c3_obj = c3(c1_obj)
print(c3_obj.aaa)
print(c3_obj.aaa.obj.name)
print(c3_obj.aaa.obj.age)
print(c3_obj.aaa.obj.show())
c3_obj.aaa.obj.show()
'''
class F1:
    def show(self):
        print('show')
    def foo(self):
        print(self.name)
class F2(F1):
    def __init__(self,name):
        self.name = name
    def bar(self):
        print('bar')
    def show(self):
        print('F2.show')
obj = F2('alex')
obj.foo()





















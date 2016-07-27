#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
'''


class Foo:
    #构造方法
    def __init__(self,name,age):
        pass
        self.name = name
        self.age = age
    #构造方法
    # def __del__(self):
    #     pass
    def __call__(self):
        print('call')
    def __str__(self):
        return "%s - %d" %(self.name,self.age)

# obj = Foo()
# obj()
# Foo()()

#p = Foo()
obj1 = Foo('alex',73)
obj2 = Foo('eric',84)
print(obj1)
ret = str(obj1)
print(ret)
#获取对象中封装的数据
ret = obj1.__dict__
print(ret)
'''
class Foo:
    #构造方法
    def __init__(self,name,age):
        pass
        self.name = name
        self.age = age
    def __getitem__(self, item):
        print(item.start)
        print(item.stop)
        print(item.step)
        print(type(item),item)

    def __setitem__(self, key, value):
        print(type(key),type(value))
        print(key.start)
        print(key.stop)
        #print(key.step)

    def __delitem__(self, key):
        print(type(key))
        print(key.start)
        print(key.stop)
        print(key.step)


obj = Foo('alex',73)
# ret = obj['ab']
# print(ret)
# obj['k1'] = 111
# del obj['k1']
ret2 = obj[1:4:2]
#obj[1:4] = [11,22,33,44]
#del obj[1:4]
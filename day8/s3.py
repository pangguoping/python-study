#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
#静态字段，普通字段
'''


class Foo:
    # 字段（静态字段）,保存在类里
    CC = 123
    def __init__(self):
        #字段（普通字段） 保存在对象里面
        self.name = 'alex'
    def show(self):
        print(self.name)


class Province:
    country = "中国"

    def __init__(self,name):
        self.name = name
#一般情况：自己访问自己字段
#规则：
# 普通字段只能使用对象访问
# 静态字段用类访问（万不得已的时候可以使用对象访问）


hb = Province('河北')
print(hb.name)
#访问静态字段
print(Province.country)
print(hb.country)

'''
'''

class Province:
    country = "中国"

    def __init__(self,name):
        self.name = name

    def show(self):   #普通方法，由对象去调用执行（方法属于类）
        print(self.name)

    @staticmethod
    def f1(arg1,arg2):
        #静态方法,由类调用执行
        print(arg1,arg2)
    @classmethod
    def f2(cls):    #cls 是类名
        print(cls)

obj = Province("河北")
obj.show()
#访问静态方法
Province.f1(11,22)
Province.f2()
'''

class Pager:
    def __init__(self,all_count):
        self.all_count = all_count
    def f1(self):
        return 123
    def f2(self,value):
        self.value = value
        print(self.value)
    def f3(self):
        pass

    foo = property(fget=f1,fset=f2,fdel=f3)
p = Pager(101)
#获取属性的值，默认会调用fget
result = p.foo
print(result)

#修改属性的值,默认会调用fset
p.foo = "alex"

# 删除属性的值,默认会调用fdel
del p.foo


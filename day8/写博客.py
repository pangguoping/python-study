#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
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

class Pager:
    def __init__(self,all_count):
        self.all_count = all_count
    @property
    def all_pager(self):
        a1,a2 = divmod(self.all_count,10)
        if a2 == 0:
            return a1
        else:
            return a1+1
    @all_pager.setter
    def all_pager(self,value):
        print(value)
    @all_pager.deleter
    def all_pager(self):
        print('del all_pager')


p = Pager(101)
# p.all_pager = 111
# ret = p.all_pager
# print(ret)
# p.all_count
# result = p.all_pager
# print(result)
del p.all_pager

# a1,a2 = divmod(200,10)
# print(a1,a2)
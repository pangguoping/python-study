#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
# li = list([11,22,33,44])
# for item in li:
#     print(item)
"""


class Foo:

    def __iter__(self):
        return iter([11,22,33,44])

obj = Foo()
for item in obj:
    print(item)

"""
class C1:
    def f1(self):
        print('c1.f1')
        return 123
class C2(C1):
    def f1(self):
        #主动执行父类的f1方法
        ret = super(C2,self).f1()
        print('c2.f1')
        return ret
obj = C2()
obj.f1()


#!/usr/bin/env  python
# -*- coding:utf-8 -*-
'''
def outer(func):
    def inner():
        print('log')
        return func()
    return inner()
@outer
def f1():
    print("F1")
@outer
def f2():
    print("F2")
@outer
def f100():
    print("F100")

'''
'''
def outer(func):
    def inner():
        print('before')
        func()
        print('after')
    return inner

@outer
def f1():
    print("F1")

f1()
'''
'''
def outer(func):
    def inner(*args,**kwargs):
        print('before')
        r = func(*args,**kwargs)
        print('after')
        return r
    return inner

@outer
def f1(arg):
    print(arg)
    print("F1")
    return "爱死你"

@outer
def f2(a1,a2):
    print("F2")
    return a1 + a2

@outer
def f3():
    print("F3")

'''
'''
def outer(func):
    # def innter():
    #     print('log')
    #     ret = func()
    #     print('after')
    #     return ret
    # return innter
    return "132"
'''
def outer(func):
    def inner(*args,**kwargs):
        print('before')
        r = func(*args,**kwargs)
        print('after')
        return r
    return inner

@outer
def f1(arg):
    print("f1函数的参数：%s" %arg)
    return "好好学习"

@outer
def f2(a1,a2):
    print("f2函数的第一个参数：%s, 第二个参数：%s"  %(a1,a2))
    return "天天向上"
ret1 = f1("F1")
print("f1函数返回值：" ,ret1)
ret2 = f2("a","b")
print("f1函数返回值：" ,ret2)


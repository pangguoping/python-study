#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
# import commons
# # obj = __import__("commons")
# # obj.login()
# import sys,os
# print(sys.path)
# def run():
#     inp = input('输入')
#     #利用字符串的形式去对象（模块）中操作（寻找/检查）成员，反射
#     # delattr()
#     # setattr()
#     if hasattr(commons,inp):
#         func = getattr(commons,inp)
#         func()
#     else:
#         print('404')
#
# if __name__ == '__main__':
#     run()

def run():
    inp = input('请输入url:')
    m,f = inp.split('/')
    obj = __import__(m)
    if hasattr(obj,f):
        func = getattr(obj,f)
        func()
    else:
        print('404')
if __name__ == '__main__':
    run()

obj = __import__("commons")
obj.login()
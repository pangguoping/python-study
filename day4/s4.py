#!/usr/bin/env  python
# -*- coding:utf-8 -*-
'''
def f1():
    print(123)

def f1():
    print(456)
f1()

'''



def f1():
    print('123')
def f2(xx):
    xx()

f2(f1)
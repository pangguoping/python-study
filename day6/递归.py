#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

def func(num):
    print(num)
    if num == 1:
        return 1


    return num * func(num - 1)

x = func(7)
print(x)
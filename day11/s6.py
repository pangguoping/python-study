#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

#条件（Condition）

#使得线程等待，只有满足某条件时，才释放n个线程
import threading

def condition():
    ret = False
    r = input('>>>')
    if r == 'true':
        ret = True
    else:
        ret = False
    return ret


def func(i,con):
    print(i)
    con.acquire()
    con.wait_for(condition)
    print(i+100)
    con.release()

c = threading.Condition()
for i in range(10):
    t = threading.Thread(target=func, args=(i,c,))
    t.start()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
#人工输入放过去的数量
import threading
def func(i,con):
    print(i)
    con.acquire()
    con.wait()
    print(i+100)
    con.release()

c = threading.Condition()
for i in range(10):
    t = threading.Thread(target=func, args=(i,c,))
    t.start()

while True:
    inp = input('>>>')
    if inp == 'q':
        break
    c.acquire()
    c.notify(int(inp))
    c.release()
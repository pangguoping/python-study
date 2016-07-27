#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
'''
#1、threading.Lock()
import threading
import time
NUM =10

def func(l):
    global NUM
    l.acquire()
    NUM -= 1
    time.sleep(2)
    print(NUM)

    l.release()
lock = threading.Lock()

for i in range(10):
    t = threading.Thread(target=func,args=(lock,))
    t.start()

'''
'''

#2、threading.RLock()
import threading
import time
NUM =10

def func(l):
    global NUM
    l.acquire()
    NUM -= 1
    time.sleep(2)
    print(NUM)

    l.release()
lock = threading.RLock()

for i in range(10):
    t = threading.Thread(target=func,args=(lock,))
    t.start()


'''

#3、信号量,每次放过去5个
import threading
import time
NUM = 10
def func(i,l):
    global NUM
    #上锁
    l.acquire()
    NUM -= 1
    time.sleep(2)
    print(NUM,i)

    #开锁
    l.release()
lock = threading.BoundedSemaphore(5)
for i in range(30):
    t = threading.Thread(target=func,args=(i,lock))
    t.start()


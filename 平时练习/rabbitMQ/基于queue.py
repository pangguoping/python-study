#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import queue
import threading
message = queue.Queue(10)
def producer(i):
    '''厨师,生产包子放入队列'''
    while True:
        msg = message.put(i)
        print(msg)

def consumer(i):
    '''消费者,从队列中取包子吃'''
    while True:
        msg = message.get()
        print(msg)

for i in range(12): #厨师的线程包子
    t = threading.Thread(target=producer, args=(i,))
    t.start()
for i in range(10): #消费者的线程吃包子
    t = threading.Thread(target=consumer, args=(i,))
    t.start()
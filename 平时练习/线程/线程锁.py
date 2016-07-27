#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
'''


import threading
import time

NUM = 0
class MyThread(threading.Thread):
    def run(self):
        global NUM
        NUM += 1
        time.sleep(0.5)
        msg = self.name + ' set num to ' + str(NUM)
        print(msg)
if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
'''
'''
#互斥锁
import threading
import time

NUM = 0
class MyThread(threading.Thread):
    def run(self,l):
        #加锁
        l.acquire()
        global NUM
        NUM += 1
        time.sleep(0.5)
        msg = self.name + ' set num to ' + str(NUM)
        #解锁
        l.release()
        print(msg)
if __name__ == '__main__':
    lock = threading.Lock()
    for i in range(5):
        t = MyThread()
        t.run(lock)
'''
'''
#信号量
import threading
import time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread: %s' %n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5) #最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()
'''
'''
#条件
import threading
import time

class Producer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count > 1000:
                    con.wait()
                else:
                    count = count+100
                    msg = self.name+' produce 100, count=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 100:
                    con.wait()
                else:
                    count = count-3
                    msg = self.name+' consume 3, count='+str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(1)

count = 500
con = threading.Condition()

def test():
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
if __name__ == '__main__':
    test()

'''

'''
import threading

def condition():
    ret = False
    r = input(">>> ")
    if r == 'true':
        ret = True
    else:
        pass
    return ret


def func(i, con):
    print(i)
    con.acquire()  # con.acquire和con.wait 必须配合使用，表示在这里等待
    con.wait_for(condition)
    print(i+100)
    con.release()

c = threading.Condition()
for i in range(10):
    t = threading.Thread(target=func, args=(i, c,))
    t.start()

'''
import threading

def func(i, e):
    print(i)
    e.wait() # 表示在这里检测信号。如果检测到为红灯，则停止。如果为绿灯，则放行
    print(i+100)

event = threading.Event()

for i in range(10):
    t = threading.Thread(target=func, args=(i,event))
    t.start()

event.clear() # 全部都停止，设置为红灯

inp = input(">>> ")
if inp == "1":
    event.set()  # 表示放行，设置为绿灯
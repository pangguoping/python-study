#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

#第一种方法创建线程
import threading
def f1(arg):
    print(arg)
t = threading.Thread(target=f1,args=(123,))
t.start()
#什么时候去执行f1方法? 是在执行t.run()方法时执行f1()方法。t.run()不用我们去执行,代码自动执行
#第二种方法:
'''
import threading
class MyThread(threading.Thread):
    def __init__(self,func,args):
        self.func = func
        self.args = args
        super(MyThread,self).__init__()  #执行父类的构造方法

    def run(self):
        self.func(self.args)

def f2(arg):
    print(arg)

obj = MyThread(f2,123)
obj.start()
'''





















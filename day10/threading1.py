#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import threading
def f1(i):
    print(i)

t1 = threading.Thread(target=f1,args=(1,))
t1.setDaemon(True)  #true，表示主线程不等次子线程
t1.start()  #不代表当前线程会被立即执行
t1.join()   #表示主线程到此，等待。。。 直到子线程执行完毕，可以加参数，表示主线程在此最多等几秒
print('end')
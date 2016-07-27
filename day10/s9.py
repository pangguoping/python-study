#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

#如何创建线程

#单进程、单线程的应用程序
import time
def f1(arg):
    time.sleep(5)
    print(arg)

import threading
t = threading.Thread(target=f1,args=(123,))
t.setDaemon(True)  #True,表示主线程不等此子线程
t.start()  #不代表当前线程会被立即执行
t.join(2)  #表示主线程到此,等待。。。直到子线程执行完成
          #参数,表示主线程在此最多等待n秒
print('end')
print('end')
print('end')
print('end')











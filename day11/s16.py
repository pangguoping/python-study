#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
'''

from multiprocessing import Pool
import time
def f1(arg):
    time.sleep(1)
    print(arg)
if __name__ == '__main__':
    pool = Pool(5)

    for i in range(30):
        #pool.apply(func=f1,args=(i,))  #每次执行一个任务
        pool.apply_async(func=f1,args=(i,))  #每次执行5个任务
    pool.close()    #所有的任务执行完毕
    time.sleep(1)
    pool.join()

'''
from multiprocessing import Pool
import time
def f1(arg):
    time.sleep(1)
    print(arg)
if __name__ == '__main__':
    pool = Pool(5)

    for i in range(30):
        pool.apply_async(func=f1,args=(i,))  #每次执行5个任务

    time.sleep(1)
    pool.terminate() #当前已经在执行的任务执行完毕
    pool.join()
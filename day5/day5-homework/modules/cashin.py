#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import time
#cash in function
from modules.logger import log_write
def cash_in(n,m):
    print("Hello %s,your account have %d RMB now." %(n,m))
    cash = int(input("Please input how much money you want to save in :"))
    m = m + cash
    log_write(n,'cash',cash,0)
    return m
# def cashin_file_write(user,cashin):
#     tran_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#     spath = "record_tran.txt"
#     f = open(spath,'a')
#     f.write('%s|%s|cashin|%d|0 \n' %(user,tran_time,cashin))
#     f.close()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import time
def log_write(user,name,price,fee):
    tran_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    spath = "../modules/record_tran.txt"
    f = open(spath,'a')
    f.write("%s|%s|%s|%d|%d  \n"  %(user,tran_time,name,price,fee))
    f.close()

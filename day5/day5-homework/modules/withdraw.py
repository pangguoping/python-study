#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import time
from modules.logger import log_write
def with_draw(user,m):
    print('Hello %s,You account have %d RMB.' %(user,m))
    print('Attention: There are 5% fee per withdraw !')
    draw = int(input('Please input how much money you want to with draw:'))
    m = m - draw * 1.05
    shouxufei = withdraw * 0.05
    withdraw_file_write(user,draw,shouxufei)
    return m

# def withdraw_file_write(user,withdraw):
#     shouxufei = withdraw * 0.05
#     tran_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     spath = "record_tran.txt"
#     f = open(spath,'a')
#     f.write("%s|%s|withdraw|%d|%d  \n" %(user,tran_time,withdraw,shouxufei))
#     f.close()



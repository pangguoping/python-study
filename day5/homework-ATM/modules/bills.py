#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import os
import sys
from conf import setting
#账单查询
def bills(card_num):

    time = input('请输入查询的时间(格式：yyyy_m_dd):')
    log_file = os.path.join(setting.USER_DIR_FOLDER, card_num,'record',time)
    if os.path.exists(log_file):
        match_yes = 0
        with open(log_file,'r',encoding='utf-8') as f:
            for line in f:
                    print(line)
                    match_yes = 1
        if match_yes == 0:
            print('没有查询月份账单')
    else:
        print('没有查询月份账单')
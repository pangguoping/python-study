#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import json
import os
from conf import setting
from modules.write_log import write_record
#还款函数
def repay(card_num,**userinfo):
    qiankuan = userinfo['credit'] - userinfo['balance']
    print('现在还欠：',qiankuan)
    fee = int(input("请输入还款金额："))
    if fee <= qiankuan:
        userinfo['balance'] += fee
        balance = userinfo['balance']
        #log(card_num,'信用卡还款',+fee,balance,**userinfo)
        json.dump(userinfo,
                  open(os.path.join(setting.USER_DIR_FOLDER, card_num, "basic_info.json"), 'w', encoding='utf-8'))
        write_record('%s - 信用卡账户还款：%f；本月额度：%f' % ("还款", fee, balance), card_num)

        print('你成功还款%d，当前可用额度%s' %(fee,balance))
    else:
        print('输入还款金额错误')

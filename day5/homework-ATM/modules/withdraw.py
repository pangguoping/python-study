#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import json
import os
import time
from conf import setting
from modules.write_log import write_record

def withdraw(card_num,**userinfo):
    fee = int(input('请输入提现金额：'))
    if fee % 100 == 0 and int(fee*1.05) <= userinfo['balance']:
        charge = fee * 0.05
        balance = userinfo['balance'] - fee - charge #计算balance
        userinfo['balance'] =  balance  #修改原数据
        json.dump(userinfo,
                  open(os.path.join(setting.USER_DIR_FOLDER, card_num, "basic_info.json"), 'w', encoding='utf-8'))
        write_record('%s - 信用卡账户取现：%f；手续费：%f' % ("提现", fee, charge),card_num)
        print('你成功取现%d，收取手续费%s，剩余额度%s' %(fee,charge,balance))
    else:
        print('输入金额有误,超过了个人信用额度！')

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import json
import os
from conf import setting
from modules.write_log import write_record

def calculate(price,**userinfo):
    new_balance = userinfo['balance'] - price
    userinfo['balance'] = new_balance
    card_num = userinfo['card']
    json.dump(userinfo,
              open(os.path.join(setting.USER_DIR_FOLDER, card_num, "basic_info.json"), 'w', encoding='utf-8'))
    write_record('%s - 信用卡账户消费：%f；本月额度：%f' % ("购物", price, userinfo['balance']), card_num)

    return userinfo['balance']

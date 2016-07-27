#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import os
import json
import sys

from modules import commons
from modules import withdraw as modules_withdraw
from modules import bills   as modules_bills
from modules import menu   as modules_menu
from modules import repay  as modules_repay
from modules import shopping  as modules_shopping

from conf import setting
def load_userinfo(card_num):
    userinfo = json.load(
        open(os.path.join(setting.USER_DIR_FOLDER, card_num, 'basic_info.json'), 'r', encoding='utf-8'))
    return userinfo

while True:
    card_num = input("\033[31;1m请输入信用卡号：\033[0m")
    i = 1

    while os.path.exists(os.path.join(setting.USER_DIR_FOLDER, card_num)):
        # userinfo = json.load(
        #     open(os.path.join(setting.USER_DIR_FOLDER, card_num, 'basic_info.json'), 'r', encoding='utf-8'))
        userinfo = load_userinfo(card_num)
        passwd = input("\033[31;1m请输入密码：\033[0m")

        #确认密码正确，并且账号没有被锁定
        while commons.md5(passwd) == userinfo['password'] and userinfo['status'] == 0:
            i = 1
            print(' 欢迎进入oldboy系统 '.center(40,'#'),'\n请输入您的操作:')
            choice = int(input('1，提现\n2，还款\n3，账单查询\n4，额度查询\n5,购物商城\n6,退出\n'))
            if choice == 1:
                modules_withdraw.withdraw(card_num,**userinfo)
            elif choice == 2:
                modules_repay.repay(card_num,**userinfo)
            elif choice == 3:
                modules_bills.bills(card_num)
            elif choice == 4:
                # userinfo = json.load(
                #     open(os.path.join(setting.USER_DIR_FOLDER, card_num, 'basic_info.json'), 'r', encoding='utf-8'))
                userinfo = load_userinfo(card_num)
                print('总额度：',userinfo['credit'],'当前额度',userinfo['balance'])
            elif choice == 5:
                userinfo = load_userinfo(card_num)
                modules_shopping.shopping(card_num,**userinfo)
            elif choice == 6:
                print('退出程序')
                sys.exit()
        else:
            i = i + 1
            print('密码错误,或者被锁定！')
            if i == 4:
                break
    else:
        print('没有这个账号！')
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys,os
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
# sys.path.append(base_dir)
#
# print(sys.path)
from modules.shopping import show_shopping_list
#from moprintlist import print_list
from modules.printlist import print_list
from modules.withdraw import with_draw
from modules.cashin import cash_in


def menu_show(n,mo):
    print('Welcom %s, This is The ATM system:' %n)
    print('Select what you want to do:')
    print('1.Shopping:\n 2.提现:\n 3.还款\n 4.打印记录:\n 5.退出')
    user_input = int(input("请输入您的选择 0 ~ 5："))
    global CURRENT_USER
    CURRENT_USER = n
    mo = menu_select(user_input,mo)
    return mo
def menu_select(choose,money):
    if choose == 1:
        money = show_shopping_list(CURRENT_USER,money)
    if choose == 2:
        money = with_draw(CURRENT_USER,money)
    if choose == 3:
        money = cash_in(CURRENT_USER,money)
    if choose == 4:
        print_list(CURRENT_USER)
    if choose == 5:
        print('\033[1;33;40mThank you for using ATM, Good bye!\033[0m')
        sys.exit()
    return money

#menu_show('user1',15000)
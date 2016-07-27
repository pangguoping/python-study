#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import sys
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from modules.menu import menu_show

while True:
    user = input("\033[1;32;40mPlease input your name:\033[0m")
    with open('../db/user_list', 'r', encoding='utf-8') as f:
        for line in f:
            n = line.split()[0]
            p = line.split()[1]
            if user == n:
                while True:
                    password = input('\033[1;32;40mPlease input your password:\033[0m')
                    if password != p:
                        print("\033[1;31;40mThe password is incorrect\033[0m")
                        continue
                    else:
                        print("\033[1;32;40myes let you in.\033[0m")
                        global MONEY
                        money_total = 15000
                        while True:
                            print('You total Money is :' ,money_total)
                            money_total = menu_show(user,money_total)
            else:
                print("\033[1;31;40mThe user is not vaild, please re-input:\033[0m")
                continue







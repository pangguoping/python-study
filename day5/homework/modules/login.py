#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import pickle
from conf import setting
#from conf.setting import init
setting.init()
file_p_name = '../db/account.pickle'
file_a_name = '../db/account'
with open(file_p_name,'rb') as f:
    userinfo = pickle.load(f)
    print(userinfo)
    #print(userinfo['1001']['pw'],type(userinfo['1001']['pw']))
    # f.close()
while True:
    user = input("\033[31;1m请输入用户名：\033[0m")
    i = 1
    while userinfo.get(user):
        #passwd = input(getpass.getpass("\33[1;32;40m请输入密码：\33[0m"))
        passwd = int(input("\033[31;1m请输入密码：\033[0m"))
        print(passwd)
        while passwd == userinfo[user]['pw']:
            i = 1
            print('欢迎进入系统，请选择操作：')
            choice = int(input('1，提现\t2，还款\t3，账单查询\t4，额度查询\t5退出\n'))
            if choice == 1:
                withdraw(user,**userinfo)
            elif choice == 2:
                repay(user,**userinfo)
            elif choice == 3:
                bills(user)
            elif choice == 4:
                print('总额度：',userinfo[user]['money'],'当前额度',userinfo[user]['balance'])
            elif choice == 5:
                sys.exit()
        else:
            i = i + 1
            print('密码错误！')
            if i == 4:
                break
    else:
        print('没有这个账号！')

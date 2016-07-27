#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys,pickle,getpass,time
#日志函数
def log(user,describe,fee,balance,**userinfo):
    time1 = time.strftime("%Y-%m-%d %X",time.localtime())
    f = open('account.log','a',encoding='utf-8')
    f.write("%s %s %s $%s $%s\n" %(time1,user,describe,fee,balance))
    f.close()
    f1 = open('account.pickle','wb')
    pickle.dump(userinfo,f1)
    f1.close()

#提现函数
def withdraw(user,**userinfo):
    fee = int(input('请输入提现金额：'))
    if fee % 100 == 0 and int(fee*1.05) <= userinfo[user]['balance']:
        charge = fee * 0.05
        balance = userinfo[user]['balance'] - fee - charge #计算balance
        userinfo[user]['balance'] =  balance  #修改原数据
        log(user,'取现(手续费%d)' %charge,fee,balance,**userinfo)
        print('你成功取现%d，收取手续费%s，剩余额度%s' %(fee,charge,balance))
    else:
        print('输入金额有误,超过了个人信用额度！')
#还款函数
def repay(user,**userinfo):
    fee = int(input("请输入还款金额："))
    userinfo[user]['balance'] += fee
    balance = userinfo[user]['balance']
    log(user,'信用卡还款',+fee,balance,**userinfo)
    print('你成功还款%d，当前可用额度%s' %(fee,balance))
#账单查询
def bills(user):
    time = input('请输入查询的时间(格式：yyyy-mm):')
    match_yes = 0
    with open('account.log','r',encoding='utf-8') as f:
        for line in f:
            if user in line and time in line:
                print(line)
                match_yes = 1
    if match_yes == 0:
        print('没有查询月份账单')

with open('account.pickle','rb') as f:
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




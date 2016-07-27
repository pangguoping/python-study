#!/usr/bin/env  python
# -*- coding:utf-8 -*-
# auth :  pangguoping

user_file = open('user.txt','r') #保存用户名密码
message_dict = { }
#下面for循环是把用户名密码转换为字典
for i in user_file:
    line = i.strip()
    line_list = line.split()
    message_dict[line_list[0]] = line_list[1]
user_file.close()
counter = 0   #定义一个计数器
last_name = ""   #定义一个空变量，用于保存登录的用户名
while True:

    user_name = input("please input your name:")   #输入用户名
    user_passwd = input("please input your password:")  #输入密码

    black_file = open('black_user.txt', 'r')  # 用户黑名单
    line = black_file.read().split("\n")
    black_file.close()

    if user_name in line:   #判断用户是否在黑名单里
        print('your name is blackuser,please call administrator ！')
        break

    else:
        if user_name in message_dict.keys() and user_passwd == message_dict[user_name]:   #判断用户名密码是否正确
            print("Welcom to login !")
            break   #登录成功并退出
        elif user_name in message_dict.keys(): #判断账号是否在用户名单里
            if last_name == user_name:  #判断输入的账号和上次是否一样
                if counter < 2:   #判断输入是否小于3次
                    last_name = user_name  #把输入的账户赋值给last_name变量，用于判断是否为连续输入相同账户
                    print("Invalid username or  password !")
                    counter += 1  #计数器的值加一
                    print('times', counter)
                    continue

                else: #如果同一个账号连续输错3次，加入黑名单
                    add_black = open('black_user.txt', 'a')  #打开黑名单文件
                    add_black.write(user_name+'\n')   #把账号添加到黑名单
                    add_black.close()  #关闭文件
                    print("Sorry ,your name is clock !",user_name)
                    break

            else: #如果输入的不是上次的账户，
                last_name = user_name  #重新赋值
                counter = 0   #计数器重新开始
                print("Invalid username or  password !")
                counter += 1   #计数器的值加1
            print('times', counter)

        else:
                last_name = user_name  #重新赋值，保证和连续输入的账户相同
                counter = 0   #计数器归零
                print("Invalid username or  password !")











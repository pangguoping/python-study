#!/usr/bin/env  python
# -*- coding:utf-8 -*-

user = "alex"
passwd = "1234"

username = input("username：")
password = input("password：")
'''
if user == username:
    print("username is correct ....")
    if password == passwd:
        print("Welcom login...")
    else:
        print("password is error....")

else:
    print("用户不存在。。。")
'''
if user == username and password == passwd:
    print("Welcom login....")
else:
    print("Invalid username or password  ....")

#!/usr/bin/env  python
# -*- coding:utf-8 -*-
user = "test"
passwd = "1234"

username = input("username：")
password = input("password：")

if user == username and password == passwd:
    print("Welcom login....")
else:
    print("Invalid username or password  ....")

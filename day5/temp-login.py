#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:44850823@qq.com

USER_INFO = {}

def check_login(func):
    def inner(*args, **kwargs):
        if USER_INFO.get("is_login", None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print("请登录")
    return inner

def check_admin(func):
    def inner(*args, **kwargs):
        if USER_INFO.get("user_type", None) == 2:
            ret = func(*args, **kwargs)
            return ret
        else:
            print("请登录")
    return inner

@check_login
@check_admin
def index():
    print("index")


@check_login
def home():
    print("Home")


def login():
    user = input("username:")
    if user == 'admin':
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 2
    else:
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 1

def main():
    while True:
        inp = input("1. 登陆 2. 查看信息  3. 用户管理\n")
        if inp == "1":
            login()
        elif inp == "2":
            home()
        elif inp == "3":
            index()
        else:
            pass

main()

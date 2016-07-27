#!/usr/bin/env  python
# -*- coding:utf-8 -*-

USER_INFO = {}

def check_login(func):
    def inner(*args,**kwargs):
        if USER_INFO.get('is_login',None):
            ret = func(*args,**kwargs)
            return ret
        else:
            print("请登录")
    return inner
            

def check_admin(func):
    def inner(*args,**kwargs):
        if USER_INFO.get("user_type",None) == 2:
            ret = func(*args,**kwargs)
            return ret
        else:
            print("无权限查看")
    return inner

@check_login
@check_admin
def index():
    "管理员"
    print("index")

@check_login
def home():
    print("home")

def login():
    user_name = input('请输入用户名')
    if user_name == 'alex':
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 2
    else:
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 1


def main():
    while True:
        inp = input('1，登录，2，查看信息，3，管理员功能\n >>>')
        if inp == '1':
            login()
        elif inp == '2':
            home()
        elif inp == '3':
            index()
        else:
            pass

main()


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

USER_INFO = {}

def check_login(func):
    def inner(*args,**kwargs):
        if USER_INFO.get('is_login',None):
            ret = func(*args,**kwargs)
            return ret
        else:
            print('请登录')
    return inner

def check_admin(func):
    def inner(*args,**kwargs):
        if USER_INFO.get('user_type',None) == 2:
            ret = func(*args,**kwargs)
            return ret
        else:
            print('无权限查看')
    return inner
@check_login
@check_admin
def index():
    print('Index')

@check_login
def home():
    """
    普通用户的功能
    :return:
    """
    print('home')
def login():
    user = input('请输入用户名：')
    if user == 'admin':
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 2
    else:
        USER_INFO['is_login'] = True
        USER_INFO['user_type'] = 1
#主函数
def main():
    while True:
        inp = input('1,登录；2，查看信息；3，超级管理员管理\n >>>')
        if inp == '1':
            login()
        elif inp == '2':
            home()
        elif inp == '3':
            index()
        else:
            pass

main()


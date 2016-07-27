#!/usr/bin/env python
#_*_coding:utf-8_*_

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
    """管理员功能"""
    print('Index')

index()

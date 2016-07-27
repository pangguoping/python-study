#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import os
import json
from modules import commons
from conf import setting
import shutil


CURRENT_USER_INFO = {'is_authenticated':False,'current_user':None}

#初始化管理员
def init():
    """
    初始化管理员信息
    :return:
    """
    dic = {'username':'admin','password':commons.md5('123')}
    if not os.path.exists(os.path.join(setting.ADMIN_DIR_FOLDER, dic['username'])):
        #print('用户名不存在')
        os.makedirs(os.path.join(setting.ADMIN_DIR_FOLDER))
        json.dump(dic,open(os.path.join(setting.ADMIN_DIR_FOLDER,dic['username']),'w',encoding='utf-8'))
    else:
        pass



def create_user():
    """
    创建普通账户
    :return:
    """
    user_name = input('请输入用户姓名：')
    card_num = input('请输入用户信用卡号码：')
    pwd = input('设置密码：')
    credit = int(input('请输入信用卡额度：'))
    base_info = {'username': user_name,  # 用户名
                 'card': card_num,  # 信用卡号码
                 'password': commons.md5(pwd),  # 密码
                 'credit': credit,  # 信用卡额度
                 'balance': credit,  # 本月可用额度
                 'status': 0  # 0 = normal,1 = locked,2 = disabled
                 }
    #创建目录
    if not os.path.exists(os.path.join(setting.USER_DIR_FOLDER,card_num)):
        os.makedirs(os.path.join(setting.USER_DIR_FOLDER, card_num, 'record'))
        json.dump(base_info,
                  open(os.path.join(setting.USER_DIR_FOLDER, card_num, "basic_info.json"), 'w', encoding='utf-8'))
        print('信用卡号为：%s,的用户已经创建成功！' %card_num)
        main()
    else:
        print('该用户已经存在，请更换其他信用卡号！谢谢')
        main()


def remove_user():
    """
    删除用户，即删除用户信息的目录
    :return:
    """
    card_num = input('请输入用户的信用卡号：')
    if os.path.exists(os.path.join(setting.USER_DIR_FOLDER, card_num)):
        shutil.rmtree(os.path.join(setting.USER_DIR_FOLDER,card_num))
        print('信用卡号为：%s,已经被删除，信息不可恢复！' %card_num)
        main()
    else:
        print('该信用卡号不存在，请确认后输入！')
        main()


def locked_user():
    """
    锁住用户
    :return:
    """
    card_num = input('请输入用户的信用卡号：')
    # 判断用户目录是否存在
    if os.path.exists(os.path.join(setting.USER_DIR_FOLDER, card_num)):
        user_dict = json.load(
            open(os.path.join(setting.USER_DIR_FOLDER, card_num, 'basic_info.json'), 'r', encoding='utf-8'))

        user_dict['status'] = 1
        json.dump(user_dict,
                  open(os.path.join(setting.USER_DIR_FOLDER, card_num, "basic_info.json"), 'w', encoding='utf-8'))
        print('信用卡号：%s 的用户已经被冻结！' %card_num)
        main()
    else:
        print('输入的信用卡号不存在，请确认！')
        main()

def search():
    """
    搜索用户
    :return:
    """
    card_num = input('请输入用户的信用卡号：')
    #判断用户目录是否存在
    if os.path.exists(os.path.join(setting.USER_DIR_FOLDER, card_num)):
        user_dict = json.load(open(os.path.join(setting.USER_DIR_FOLDER, card_num,'basic_info.json'), 'r', encoding='utf-8'))
        print(' 用户名：%s\n 信用卡号: %s\n 信用额度: %d\n 本月可用额度: %d\n'
              %(user_dict['username'],user_dict['card'],user_dict['credit'],user_dict['balance']))
        main()
    else:
        print('输入的卡号不存在，请重新输入。谢谢')
        search()



def main():
    menu = """
    1、创建账户：
    2、删除账户：
    3、冻结账户：
    4、查询账户：
    5、退出程序：
    """
    print(menu)
    menu_dic = {
        '1': create_user,
        '2': remove_user,
        '3': locked_user,
        '4': search,
        '5': logout,
    }
    while True:
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            print("选项不存在")


def login():
    """
    用户登录
    :return:
    """
    while True:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if not os.path.exists(os.path.join(setting.ADMIN_DIR_FOLDER,username)):
            print('用户名不存在')
        else:
            user_dict = json.load(open(os.path.join(setting.ADMIN_DIR_FOLDER,username),'r',encoding='utf-8'))
            if username == user_dict['username'] and commons.md5(password) == user_dict['password']:
                CURRENT_USER_INFO['is_authenticated'] = True
                CURRENT_USER_INFO['current_user'] = username
                return True
            else:
                print('密码错误')
def logout():
    """
    退出程序
    :return:
    """
    os._exit(0)
def run():
    init()
    result = login()
    if result:
        main()

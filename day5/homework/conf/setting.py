#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import pickle
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ADMIN_DIR_FOLDER = os.path.join(BASE_DIR, 'db', 'admin')

USER_DIR_FOLDER = os.path.join(BASE_DIR, 'db', 'userinfo')

file_p_name = '../db/account.pickle'
file_a_name = '../db/account'

def init():
    account = {'user1':{'name':'user1','pw':123,'money':15000,'balance':15000},
               'user2': {'name': 'user2', 'pw': 123, 'money': 15000, 'balance': 15000}}

    f = open(file_p_name,'wb')
    pickle.dump(account,f)
    f.close()

    with open(file_p_name,'rb') as f:
        dic = pickle.load(f)
        f.close()
 #   print(dic)
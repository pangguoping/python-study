#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import pickle
account = {'user1':{'name':'user1','pw':123,'money':15000,'balance':15000},
           'user2': {'name': 'user2', 'pw': 123, 'money': 15000, 'balance': 15000}}
f = open('account.pickle','wb')
pickle.dump(account,f)
f.close()

with open('account.pickle','rb') as f:
    dic = pickle.load(f)
    f.close()
print(dic)

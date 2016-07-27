#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import requests

'''


import json
dic =  {'k1':'v1'}

#将python基本数据类型转换成字符串形式
result = json.dumps(dic)
print(result,type(result))

s1 = '{"k1":123}'
#将python字符串形式转换成基本数据类型
dic = json.loads(s1)
print(dic,type(dic))
'''

"""
import requests
import json
response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
response.encoding = 'utf-8'

dic = json.loads(response.text)
print(type(dic))
print(dic)
"""
"""
import json
r = json.dumps([11,22,33])
print(r,type(r))
li = '["alex","eric"]'
#li = "['alex','eric']"
ret = json.loads(li)
print(ret,type(ret))
"""
'''


import json
li = [11,22,33]
json.dump(li,open('db1','w'))
with as
li2 = json.load(open('db1','r'))
print(li,type(li))
'''
#json/pickle
#json更加适合跨语言，字符串，基本数据类型
#pickle ,python 复杂类型的序列化，仅适用于python



#pickle dumps和lloads
# import pickle
# li = [11,22,33]
# r = pickle.dumps(li)
# #print(r)
# result = pickle.loads(r)
# print(result)
'''


# #dump 和 load
import pickle
li = [11,22,33]
pickle.dump(li,open('db2','wb'))
result = pickle.load(open('db2','rb'))
print(result)
'''
'''

import json
li = [11,22,33]
json.dump(li,open('db1','w'))
#从文件中读出
with  open('db1','r') as file:
    for i in file:
        print(i)

import json
li2 = json.load(open('db1','r'))
print(li,type(li))
'''
import random
print(random.randrange(1,10))
print(random.randint(1,2))
print(random.random())
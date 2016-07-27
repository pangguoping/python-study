#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
# print(__file__)  #当前py文件所在的路径
# from bin import admin
#
# print(admin.__package__)
import re
# #r = r"\d{3,4}-?\d{8}"
# p_tel = re.compile(r'csvt')
# print(p_tel.findall('csvtsdfsdf'))
#
# #print(re.findall(r,'010--12345678'))
ori = r"(\([^()]+\))"
r = re.split(ori,"8*12+(6-(5*6-2)/77+2)*3",1)
print(r)


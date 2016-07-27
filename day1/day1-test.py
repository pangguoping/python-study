#!/usr/bin/env  python
# -*- coding:utf-8 -*-

user_file = open('user.txt','r') #保存用户名密码
message_dict = { }
#下面for循环是把用户名密码转换为字典
for i in user_file:
    line = i.strip()
    print(line)
    line_list = line.split()
    print(line_list)
    message_dict[line_list[0]] = line_list[1]
user_file.close()
counter = 0   #定义一个计数器
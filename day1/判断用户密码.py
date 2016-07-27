#!/usr/bin/env  python
# -*- coding:utf-8 -*-
message_dict = { }
user_file = open('user.txt','r')
f=open('black_user.txt','r')

user_name = input("please input your name:")
user_passwd = input("please input your password:")
while True:

    line = f.readline()
    if user_name in line:
        print('your name is blackuser,please call administrator')
        print(user_name)
        break
    else:

f.close()

for i in user_file:
    line = i.strip()
    line_list = line.split()
    message_dict[line_list[0]] = line_list[1]

user_file.close()
print(message_dict)
while True:
    user_name = input("please input your name:")
    user_passwd = input("please input your password:")
    if user_name in message_dict.keys() and  user_passwd ==  message_dict[user_name]:
        print("Welcom to login !")
        break
    else:
        print("Invalid username or  password")
    print(user_passwd)







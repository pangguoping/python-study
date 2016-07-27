#!/usr/bin/env  python
# -*- coding:utf-8 -*-
#1.字符串去除空格  .strip()
"""
username = input("user:")
if username.strip() == 'alex':
    print("welcom")
"""
#2.字符串分隔
names = "alex,jack,rain"
name2 = names.split(",")  #split()默认是以空格
print("2:%s" %name2)
name3 = names.split()
print("3:%s" %name3)

#3合成一个字符串
print("|".join(name2))

#4.判断是否有空格
name ="Alex Li"
print('' in name)
#
name3 = "alex li"
print("4:%s" %name.capitalize())

#6.字符串分片
name="alex li"
print(name[2:4])

#7.-----
name='alex'
print(name.center(40,'-'))

#8.字符串查找
name="alex li"
print(name.find('sdfs'))
print(name.find('alex'))

#9.判断是否为数字
age = input("your age:")
if age.isdigit():
    age = int(age)
else:
    print("invalid data type")

#10.是否包含阿拉伯字符（数字字母）（有为真，否则为False），即是否包含特殊字符(有为False,否则为True)
name='alex#sdf'
print(name.isalnum())

#11.判断是否以什么结尾
name='alex3sdf'
print(name.endswith('sdf'))

#11.是否以什么开始
name='alex3sdf'
print(name.startswith('alex'))

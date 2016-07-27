#!/usr/bin/env  python
# -*- coding:utf-8 -*-
'''
user_name_input = input("input your name:")
user_age_input = input("input your age:")
user_work_input = input("input your work:")

print("user input msg:",user_name_input,user_age_input,user_work_input)
'''

name = input("input your name:")
age = int(input("input your age:"))
job = input("input your job:")

msg ='''
infornation of user %s:
Name: %s
Age: %d
Job: %s
''' %(name,name,age,job)

print(msg)




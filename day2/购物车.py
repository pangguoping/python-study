#!/usr/bin/env  python
# -*- coding:utf-8 -*-

salary = input("Input Your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type....")
welcome_msg = 'Welcome to Alex Shopping mall'.center(50,'-')
print(welcome_msg)
exit_flag = False
product_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi2',19.9),]
print(product_list)


for product_item in product_list:
    p_name,p_price = product_item
    print(product_item)
   # print(p_name,p_price)

'''
for item in enumerate(product_list):
    index = item[0]
    p_name = item[1][0]
    p_price = item[1][1]
    print(index,p_name,p_price)
'''


product_list2 = ['A,a','B,b','C,c','D,c']
for i in product_list2:
    p_name1,p_prce1 = i[0],i[2]
    print(p_name1,p_prce1)


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
salary = input('input your salary')
if salary.isdigit():
    salary = int(salary)
else:
    exit('Invaild data type....')
welcome_msg = 'Welcome to Alex  Shopping mall'.center(50,'-')
print(welcome_msg)

exit_flag = False
product_list = [
    ('Iphone',58888),
    ('Mac Air',8888),
    ('Mac Pro',9000),
    ('Xiao Mi',19.9),
    ('Bike',700),
]
p_oo = product_list[3]
#print(p_oo)
#print(p_oo[0],p_oo[1])
shop_car = []
while exit_flag is not True:
    print('product list'.center(50,'-'))
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_name,p_price)
    user_choice = input('[q=quit,c=check]What do you want to buy?:')
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary:
                shop_car.append(p_item)
                salary -= p_item[1]
                print('Added %s into shop car ,you current balance is %d' %(p_item,salary))
            else:
                print('Your balance is %s,cannot afford this..' %salary)
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print('purchased products as below'.center(40,'*'))
            for item in shop_car:
                print(item)
            print('END'.center(40,'*'))
            print('Your balance is %s' %salary)
            print('Bye')
        if user_choice == 'c' or user_choice == 'check':
            print('purchased products as below'.center(40,'*'))
            for item in shop_car:
                print(item)
            print('END'.center(40,'*'))
            print('Your balance is \033[41;1m[%s]\033[0m' % salary)
#!/usr/bin/env  python
# -*- coding:utf-8 -*-



'''
list1 = ['A,a','B,b','C,c','D,c']
for i in list1:
    p1,p2 = i[0],i[2]
    print(p1,p2)
'''


'''
list1 = ['A,a','B,b','C,c','D,c']
for i in list1:
    p1,p2,p3 = i[0],i[1],i[2]
    print(p1,p2,p3)

'''
'''
product_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi2',19.9),]

for item in enumerate(product_list):
    index = item[0]
    p_name = item[1][0]
    p_price = item[1][1]
    print(index,p_name,p_price)

'''
'''
product_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi2',19.9),]
print(product_list)

for product_item in product_list:
    p_name,p_price = product_item
    print(product_item)
    print(p_name,p_price)

'''


name='AAAA'
print(name.center(40,'-'))
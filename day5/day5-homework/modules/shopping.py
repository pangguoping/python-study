#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys
import time
from modules.logger import log_write

def show_shopping_list(n,m):
    #read the file to a dictionary
    goods_dict={}
    goods = open('../db/goods_list','r+')
    for line in goods:

        key = line.split()[0]
        value = line.split()[1]+' '+line.split()[2]
        goods_dict[key] =  value
       # print(goods_dict[key][2])
        print(key,value)

    print("The current user is %s" %n)
    #print(list(goods_dict))
    buy_number = input('Please select which one you want to buy:')
    goods_name = goods_dict[buy_number].split()[0]
    goods_value = int(goods_dict[buy_number].split()[1])
    print(goods_value)
    if int(m) >= goods_value:
        log_write(n,goods_name,goods_value,0)
        m = calculate(int(m), goods_value)
    else:
        print('超过信用额度')

    return m

def calculate(qian,pri):
    new_qian = qian - pri
    return new_qian
# def shopping_file_write(user,name,price,fee):
#     tran_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     spath = "../modules/record_tran.txt"
#     f = open(spath,'a')
#     f.write("%s|%s|%s|%d|%d  \n"  %(user,tran_time,name,price,fee))
#     f.close()


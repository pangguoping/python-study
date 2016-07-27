#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
from modules.calculate import calculate
def shopping(card_num,**userinfo):
    #read the file to a dictionary
    # userinfo = json.load(
    #     open(os.path.join(setting.USER_DIR_FOLDER, card_num, 'basic_info.json'), 'r', encoding='utf-8'))
    goods_dict={}
    goods = open('../db/goods_list','r+')
    for line in goods:

        key = line.split()[0]
        value = line.split()[1]+' '+line.split()[2]
        goods_dict[key] =  value
       # print(goods_dict[key][2])
        print(key,value)

    print("当前用户 %s" %card_num)
    print("本月额度：%s" %userinfo['balance'])
    #print(list(goods_dict))
    buy_number = input('请选择您要买的商品编号:')
    goods_name = goods_dict[buy_number].split()[0]
    goods_value = int(goods_dict[buy_number].split()[1])
    #print(goods_value)
    if int(userinfo['balance']) >= goods_value:
        #log_write(n,goods_name,goods_value,0)
        m = calculate(goods_value,**userinfo)
    else:
        print('\033[31;1m超过信用额度\033[0m')

   # return m


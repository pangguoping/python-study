#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys
products = []  #存储商品
prices = []    #存储商品价格
shop_list = []  #存储购买的商品
shop_count = []  #存储购买物品，计算同一物品购买数量
with open('shop.txt','r',encoding='utf-8')  as f:
    for line in f:
        #print(line,type(line)) #line为字符串类型
        new_line = line.split()  #通过指定分隔符对字符串进行切片
        products.append(new_line[0])
        prices.append(int(new_line[1]))  #默认str类型
salary = int(input('请输入你的工资：'))
while True:
    print('商品列表'.center(40,'-'))
    #print(len(products))
    for p in products:
        print(products.index(p),p,prices[products.index(p)])

        #print(products.index(p))
    choice = input('请选择你购买的商品：')
    f_choice = choice.strip()  #移除字符串头尾指定的字符（默认为空格）
    if f_choice in products:
        price = prices[products.index(f_choice)]
        #print(price)
        if salary >= price:
            shop_list.append(f_choice)
            print(f_choice,price,"已经添加到购物车中！")
            salary = salary - price
            print('您的余额为：',salary)
            if f_choice not in shop_count:
                shop_count.append(f_choice)
        else:
            if salary < min(prices):
                print('屌丝，余额不足。一共购买了这些商品：')
                for p in shop_count:
                    print(p,shop_list.count(p))
                sys.exit()  #程序退出
            else:
                print('对不起，您的余额：%d ,无法支付%s,请购买其他商品' %(salary,f_choice))
    else:
        print('您选择的商品，不在商品列表中，请重新选择')






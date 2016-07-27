#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
def print_list(n):
    print('Hello %s,Here is your bill:' %n)
    print("Account|Date|Goods|Price|Fee")
    spath1 = "../modules/record_tran.txt"
    f1 = open(spath1,'r')
    for line in f1.readlines():
        if line.split('|')[0] == n:
            print(line)


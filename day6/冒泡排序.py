#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

list1 = [11,22,44,33,7,3,55]
for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i] > list1[i+1]:
            temp = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = temp
print(list1)


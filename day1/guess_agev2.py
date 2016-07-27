#!/usr/bin/env  python
# -*- coding:utf-8 -*-
age = 22
for i in range(10):
    guess_age = int(input("input your guess age:"))
    if guess_age == age:
        print("gongxi")
        break
    elif guess_age > age:
        print("think smaller...")
    else:
        print("think big...")

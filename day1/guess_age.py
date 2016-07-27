#!/usr/bin/env  python
# -*- coding:utf-8 -*-

age = 22
guess_age = int(input("input your guess age:"))

if guess_age == age:
    print("gongxi")
elif guess_age > age:
    print("think smaller...")
else:
    print("think big...")

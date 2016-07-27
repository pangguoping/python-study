#!/usr/bin/env  python
# -*- coding:utf-8 -*-
age = 22
counter = 0
for i in range(10):
    print('-->counter:',counter)
    if counter <3:
        guess_age = int(input("input your guess age:"))
        if guess_age == age:
            print("gongxi")
            break
        elif guess_age > age:
            print("think smaller...")
        else:
            print("think big...")
    else:
        continue_confirm = input("do you want to coutinue because you are stupid:")
        if continue_confirm == 'y':
            counter = 0
            continue
        else:
            print("bye")
            break
    counter += 1
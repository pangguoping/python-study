#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
if 1 == 1:
    name = 'alex'
print(name)
for i in range(10):
    name = i
print(name)


def func():
    name = 'alex'
func()
print(name)

'''

'''


name = 'alex'
def f1():
    name = 'kk'
    print(name)

f1()

# python的作用域:从内向外找,找不到就报错
name = 'alex'
def f1():
    print(name)

def f2():
    name = 'eric'
    f1()
f2()
##out: alex

#在函数未执行之前,作用域已经确定了

name = 'alex'
def f1():
    print(name)

def f2():
    name = 'eric'
    return f1
ret = f2()
ret()
#输出: alex

li = [x+100 for x in range(10)]
print(li)
li = [x+100 for x in range(10) if x > 6]
print(li)

def func():
    for x in range(10):
        #print(1)
        pass
    return x

func()

li = [lambda :x for x in range(10)]
r = li[0]()
print(r)
print(li)

li = []
for x in range(10):
    def f1():
        return x
    li.append(f1)
#li是列表,内部元素是相同功能的函数
print(li)
print(li[0]())
'''

# li = []
# for i in range(10):
#     def f1(x=i):
#         return x
#     li.append(i+1)
#     #li是列表,内部元素是相同功能的函数
# print(li)
# print(li[2]())










#!/usr/bin/env  python
# -*- coding:utf-8 -*-
'''
li = [11,22,33,44]
def f1(arg):
    arg.append(55)
li=f1(li)
print(li)

'''

####################
# def f1():
#     pass
# print(callable(f1))
######################
#####################
# r = chr(65)
# print(r)
#
# n = ord("A")
# print(n)
###################
'''
import random
#1 = < i <5
num = random.randrange(1,5)
print(num)
'''


############
# import random
# li = []
# for i in range(6):
#     temp = random.randrange(65,91)
#     c = chr(temp)
#     li.append(c)
# result = "".join(li)
# print(result)

##############
'''
import random
li = []
for i in range(6):
    if i == 2 or i == 4:
        num = random.randrange(0,10)
        li.append(str(num))
    else:
        temp = random.randrange(65,91)
        c = chr(temp)
        li.append(c)
result = "".join(li)
print(result)
'''

'''
a = "abcdef"
b = "X".join(a)
print(b)
'''


'''
import random
li = []
for i in range(6):
    r = random.randrange(0,5)
    if r == 2 or r == 4:
        num = random.randrange(0,10)
        li.append(str(num))
    else:
        temp = random.randrange(65,91)
        c = chr(temp)
        li.append(c)
result = "".join(li)
print(result)
'''
'''
import random
li = []
for i in range(6):
    r = random.randrange(0,5)
    if i == r:
        num = random.randrange(0,10)
        li.append(str(num))
    else:
        temp = random.randrange(65,91)
        c = chr(temp)
        li.append(c)
result = "".join(li)
print(result)

'''

#compile 将字符串编译成python代码转换为代码
#
#exec()  #执行，没有返回值，即没有结果。可以接收代码或者是字符串都可以执行。即如果有接收到的是python代码，那么就会直接执行。如果接收到的是字符串，那么exec()会把字符串编译成python代码，然后再执行该代码。
#执行表达式，并且返回结果
#eval  执行，有返回值，把字符串转换为表达式，进行计算，并返回结果


'''
s = "print(123)"

r = compile(s,"<string>","exec")
k = exec(r)
print(k)  #返回None
'''



#
'''
s = "8*8"
ret = eval(s)
print(ret)
'''
#快速查看，对象提供了那些功能
#print(dir(list))
#查看帮助信息
#help(list)

#共99页面，每页显示10条,需要多少页
'''
r = divmod(100,10) #生成的是元组类型
print(r)
print(r[0])
print(r[1])
n1,n2 = divmod(100,10)
print(n1)
print(n2)
'''

'''
def f1(args):
    result = []
    for item in args:
        if item > 22:
            result.append(item)
    return result
li = [11,22,33,44,55]
ret = f1(li)
print(ret)
'''

'''
def f2(a):
    if a > 22:
        return True
li = [11,22,33,44,55]
ret = filter(f2,li)
print(list(ret))
print(ret)
'''
#filter 内部循环，参数比较

#lambda 自动return
'''
f1 = lambda a: a>30
ret = f1(90)
print(ret)
'''
'''
li = [11,22,33,44,55]

result = filter(lambda a: a>33,li)
print(list(result))
print(result)
'''
'''

'''
'''
li = [11,22,33,44,55]
result = map(lambda a: a + 200,li)
print(list(result))
r = filter(lambda a: a + 200,li)
print(list(r))
#filter  :函数返回True，将元素添加
#map  # 将函数返回元素添加到结果中
'''
'''
s = "李杰"
print(len(s))

s = "李杰"
b = bytes(s,encoding='utf-8')
print(len(b))

'''
'''
li = max([11,22,33,44,55])
print(li)
'''
'''

li = [11,22,33]
reversed(li)

li = [11,22,33,44]
li.sort()
sorted(li)
'''

import os
try:
    from prettytable import PrettyTable
except ImportError:
    os.system("python -m pip install prettytable")


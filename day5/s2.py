#!/usr/bin/env  python
# -*- coding:utf-8 -*-
'''
s1 = "adflsdf{0}a123{0}123{1}".format(123, "alex")
print(s1)
s2 = "----{:*^20s}======".format('alex')
print(s2)
s3 = "adfsdf {:.2%}".format(0.232332)
print(s3)

'''
'''
t1 = "i am {}, age {} ,{}".format("seven",18,'alex')
print(t1)
t2 = "i am {}, age {} ,{}".format(*["seven",18,'alex'])
print(t2)
t3 = "i am {0}, age {1},really {0}".format("seven",18)
print(t3)
t4 = "i am {0}, age {1},really {0}".format(*["seven",18])
print(t4)
t5 = "i am {name}, age {age}, really {name}".format(name="seven",age=18)
print(t5)
t6 = "i am {name}, age {age} ,really {name}".format(**{"name": "seven","age":18})
print(t6)

t7 = "i am "
'''

#生成器，使用函数创造
# li = [11,22,33,44,]
# result = filter(lambda a:a>22,li)
# print(result)

'''

def func():
    print('A')
    yield 1
    print('B')
    yield 2
    print('C')
    yield 3

ret = func()
print(ret)
for i in ret:
    print(i)

#解释器执行过程
ret = func()
r1 = ret.__next__()  #进入函数找到yield，获取yield 后面的数据
print(r1)
r2 = ret.__next__()  #进入函数找到yield，获取yield 后面的数据
print(r2)
r3 = ret.__next__()  #进入函数找到yield，获取yield 后面的数据
print(r3)
'''

'''

def myrang(arg):
    start = 0
    while True:
        if start > arg:
            return
        yield start
        start += 1
ret = myrang(3)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
'''

#递归
def func(n):
    n += 1
    if n >= 4:
        return 'end'
    return func(n)

r = func(1)
print(r)

#思考题：1*2*3*4*5*6*7
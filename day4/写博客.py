#!/usr/bin/env  python
# -*- coding:utf-8 -*-
'''
with open('aa','r',encoding='utf-8') as f1:
    for line in f1:
        line_strip = line.strip()

        print(line_strip,bool(line_strip))

s = "print(123)"

'''

"""
'''例1：接收字符串，先把字符串转换为python代码，然后再执行该代码'''
s = "print(123)"
exec(s)
'''例2：接收到的是代码，直接执行该代码'''
s = "print(123)"
r = compile(s,"<string>","exec")
exec(r)
'''例3：没有返回值，即没有结果。只能返回None'''
s = "print(123)"
r = compile(s,"<string>","exec")
k = exec(r)
print(k)
'''例1：将字符串s转换为代码，并执行s的表达式'''
s = "8*8"
ret = eval(s)
print(ret)

print(dir(list))
"""
"""

'''例1：获取divmod()的值'''
r = divmod(98,10) #生成的是元组类型
print(r,type(r))
print(r[0])
print(r[1])
'''例2：获取n1,n2的值'''
n1,n2 = divmod(98,10)
print(n1)
print(n2)
"""
"""
'''例1：获取列表大于22的元素，平时做法'''
def f1(args):
    result_list = []
    for item in args:
        if item > 22:
            result_list.append(item)
    return result_list

list1  = [11,22,33,44,55]
r = f1(list1)
print(r)
"""
"""
'''例2：使用filter函数实现'''
def f2(a):
    if a > 22:
        return True
li = [11,22,33,44,55]
ret = filter(f2,li)
print(list(ret))
"""

"""
'''例3：使用filter函数与lambda'''
list1 = [11,22,33,44,55]
ret = filter(lambda a:a>22,list1)
print(list(ret))
"""
"""

'''例1:for循环实现'''
list1 = [11,22,33,44,55]
def f1(arg):
    result_list = []
    for item in arg:
        result_list.append(item +100)
    return result_list
t = f1(list1)
print(t)

'''例2：使用map函数实现'''
'''
'''
list1 = [11,22,33,44,55]
def f2(a):
    return a + 100
result = map(f2,list1)
print(list(result))


'''例3：map函数与lambda'''
list1 = [11,22,33,44,55]
result = map(lambda a: a+100,list1)
print(list(result))


"""
"""
li = [11,22,33,44,55]
result = map(lambda a: a + 200,li)
print(list(result))
r = filter(lambda a: a + 200,li)
print(list(r))

#filter  :函数返回True，将元素添加
#map  # 将函数返回元素添加到结果中
'''例1:计算字符串长度'''
s = "abcd"
k = len(s)
print(k)
'''例2：计算汉字长度'''
s = "北京"
k = len(s)
print(k)
'''例3：按照字节计算汉字长度'''
s = "北京"
b = bytes(s,encoding='utf-8',)
print(len(b))
'''例4：计算列表长度'''
list1 = [11,22,33,44,55]
print(len(list1))
'''例5：计算字典长度'''
dict1 = {"key1":"value1","key2":"value2","key3":"value3"}
print(len(dict1))
"""

"""

'''例1：判断字符串对象是否为str的实例，是返回True,否则返回False'''
s = "beijing"
r = isinstance(s,str)
print(r)
'''例2：判断是字符串对象是否为list类的实例，是返回True，否则返回False'''
s = "beijing"
r = isinstance(s,list)
print(r)
"""
"""

li = [11,22,33,44]
def f1(arg):
    arg.append(55)
li = f1(li)
print(li)
"""

"""

'''例1：把下面的3个列表中的beijing is China输出'''
list1 = ["beijing",11,22,33]
list2 = ["is",11,22,33]
list3 = ["China",11,22,33]
r = zip(list1,list2,list3)
#print(list(r))
li = list(r)
temp = li[0]
print(temp)
k = " ".join(temp)
print(k)

list1 = ["beijing",11,22,33]
list2 = ["is",11,22,33]
list3 = ["China",11,22,33]
r = zip(list1,list2,list3)
print(list(r))

"""
'''
s = "8*8"
r = compile(s,"<string>","exec")
k = exec(r)
#print(k)
'''
'''例1'''
def foo():
    print('foo')
foo    #表示是函数
foo()   #表示执行函数
'''例2：'''
def foo():
    print('foo')
foo = lambda x=1: x+1
foo()  #执行下面的lambda表达式，而不再是原来的foo函数，因为函数foo被重新定义
















#!/usr/bin/env  python
# -*- coding:utf-8 -*-

#list __init__，内部
'''
# 1、set，无序，不重复序列
#创建
#方法一：
s1 = {"123","456"}

print(type(s1))
#方法二：
s2 = set()  #创建空集合

#方法三：
#列表转换为集合
li = [11,22,11,22]
s3 = set(li)
print(s3)

#二、操作集合
#1.集合添加元素
s = set()
s.add(123)
print(s)

#A中存在，B中不存在
s1 = {11,22,33}
s2 = {22,33,44}

s3 = s1.difference(s2)

print(s3)


#对称chaji

s4 = s1.symmetric_difference(s2)

print(s3)

#
s1.difference_update(s2)
print(s1)

s1.symmetric_difference_update(s2)

'''

'''
#移除
s1 = {11,22,33}
s1.discard(1111)  #移除的不存在不会报错,最常用

#s1.remove(1111)  #移除的值不存在会报错

ret = s1.pop()   #随机移除一个元素，并打印被移除的元素
print(ret)

'''

'''

#交集
s1 = {11,22,33}
s2 = {22,33,44}

s3 = s1.intersection(s2)
s1.intersection_update(s2)
print(s3)
'''
'''
#并集
s1 = {11,22,33}
s2 = {22,33,44}
s3 = s1.union(s2)

print(s3)
'''

'''
#批量添加元素
li = [11,22,33,44]
s1.update(li)     #update接受一个可以被迭代的对象，也就是可以被for循环的。update相当于调用多次add函数
print(s1)
'''


'''
li = [11,22,33]   #list __init__
li()              #list __call__
li[0]             # list __getitem__

li[0] = 123       # list __setitem__

def li[1]          #list __delitem__
'''


old_dict = {
    "#1":8,
    "#2":4,
    "#4":2,
}

new_dict = {
    "#1": 4,
    "#2": 4,
    "#3": 2,

}
'''
#应该删除那个几个曹位

old_set = set(old_dict)
print(old_set)

new_set = set(new_dict)
print(new_set)

#需要删除的
remove_set = old_set.difference(new_set)
print(remove_set)

old_list = list(old_dict)
print(old_list)
'''

old_set = set(old_dict.values())
print(old_set)
#需要删除的，取 old_set中存在的，而new_set 中不存在的
old_set = set(old_dict.keys())   # 把知道的key转换成集合
new_set = set(new_dict.keys())

#print(old_set)
#print(new_set)

remove_set = old_set.difference(new_set)
print(remove_set)

#需要增加的曹位 ,取new_set中存在的，而old_set 中不存在的

add_set = new_set.difference(old_set)
print(add_set)

#需要更新的曹位， 取 new_set和old_set 中的交集

update_set = new_set.intersection(old_set)
update_set2 = old_set.intersection(new_set)
print(update_set)
print(update_set2)
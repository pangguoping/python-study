#!/usr/bin/env  python
# -*- coding:utf-8 -*-

'''
name1=name.count(9)
print(name1)
name2=name[3].count(9)
print(name2)
name3=name1+name2
print(name3)
for i in range(name3)
'''
#找出有多少个9

name = ['Alex','jack','Rain','A','B','C','A']
for i in range(name.count('A')):
    pos_name_of = name.index('A')
    name[pos_name_of]=999999
print(name)

'''
name = ['Alex','jack','Rain','A','B','C','A']
for i in range(name.count('A')):
    pos_name_of = name.index('A')
    name[pos_name_of]=999999
print(name)
'''

#找出有多少个9，并删除

name = ['Alex','jack','Rain','A','B','C','A']
for i in range(name.count('A')):
    pos_name_of = name.index('A')
    name.pop(pos_name_of)
print(name)



'''
name = ["A","B","C","D","E","F","G","A","A"]
name2 = name.count("A")
print(name2)
'''


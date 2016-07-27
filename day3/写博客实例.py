#!/usr/bin/env  python
# -*- coding:utf-8 -*-
'''
s1 = set()
print(type(s1))

s1 = {"123","456"}
print(s1)
print(type(s1))

list1 = [11,22,11,22]
s1 = set(list1)
print(s1)

dict1 = {
    "key1":11,
    "key2":22,
    "key3":33,
}
set_dict1 = set(dict1.keys())
print(set_dict1)
'''

'''
s1 = set()
s1.add(123)
s1.add(123)
s1.add(123)

print(s1)
'''
'''

s1 = set()
list1 = [11,22,33,44]   #update接受一个可以被迭代的对象，也就是可以被for循环的。update相当于调用多次add函数
s1.update(list1)
print(s1)
'''
'''

def A(a):
    if a == 1:
        return 222

    #在函数中，一旦执行return，函数执行过程立即终止

    return 333


R = A(2)
print(R)


'''
'''
s1 = {11,22,33}
s2 = {22,33,44}
s1.symmetric_difference_update(s2)
print(s1)
'''
'''
s1 = {11,22,33}
ret = s1.pop()   #随机移除一个元素，并打印被移除的元素
print(ret)
'''

'''
s1 = {11,22,33}
s2 = {22,33,44}

s3 = s1.intersection(s2)
print(s3)
s1.intersection_update(s2)
print(s1)
'''

'''
s1 = {11,22,33}
s2 = {22,33,44}
s3 = s1.union(s2)

print(s3)
'''
'''
s = "百度"
n = bytes(s,encoding="gbk")
print(n)
'''

'''
new_str = str(bytes("百度",encoding="utf-8"),encoding="utf-8")
print(new_str)
'''
'''
#f = open('db','r')  #只读
#f = open('db','w')  #只写，先清空原文件
#f = open('db','x')  #文件存在，报错；不存在，创建并只写
#f = open('db','a')  #追加
f = open('db','r',encoding="utf-8")
'''

'''
data = f.read()
print(data,type(data))

文件句柄 = open('文件路径','模式')
'''
'''
f = open("db",'r+',encoding="utf-8")
data = f.read(1)
print(f.tell())
f.close()
'''

# f.write("777")
# print(data)
# f.close()
# f = open("db",'r+',encoding="utf-8")
# data = f.read()
# print(data)
'''
f = open("db",'r+',encoding="utf-8")
for line in f:
    print(line)
'''

'''

with open('file1','r',encoding="utf-8") as f1,open('file2','w',encoding="utf-8") as f2:
    times = 0
    for line in f1:
        times += 1
        if times < 10:
            f2.write(line)
        else:
            break

'''
'''
with open('file1','r',encoding="utf-8") as f1,open('file2','w',encoding="utf-8") as f2:
    for line in f1:
        new_str = line.replace("baidu",'google')
        f2.write(new_str)
'''

'''
with open('file1','r',encoding="utf-8") as f1,open('file2','w',encoding="utf-8") as f2:
    for line in f1:
        if line == "xx":
            f2.write()
            f2.write()
'''













f = open("file1",'r+',encoding="utf-8")

# data = f.read()
# print(data)
# f.write("\n"+"google.baidu.com")
# f.flush()
# data = f.read()
# print(data)
#
# f.close()
f = open("file1",'r+',encoding="utf-8")
#data1 = f.readlines()
#print(data1)
'''
for line in f.readlines():
     line = line.strip()
     print(line)
'''
'''
line = ""
5 > 2
'''



















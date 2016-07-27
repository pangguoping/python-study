#!/usr/bin/env  python
# -*- coding:utf-8 -*-

'''
def sendmail():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["武沛齐", 'wptawy@126.com'])
    msg['To'] = formataddr(["走人", '424662508@qq.com'])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("wptawy@126.com", "WW.3945.59")
    server.sendmail('wptawy@126.com', ['815632410@qq.com', ], msg.as_string())
    server.quit()

sendmail()

'''
'''
def sendmail(xxoo)   # xxoo 是形式参数


#实际参数
ret = sendmail("alex")    #alex 就是实际参数

while True:
    em = input("请输入邮箱地址：")
    result = sendmail(em)
    if result == "cc"
        print("发送成功")
    else:
        print("发送失败")
  '''
'''

def send(xxoo,content)
    print("发送邮件成功："，xxoo,content)
    return True

while True:
    em = input("请输入邮箱地址：")
    result = sendmail(em,content)
    if result == True
        print("发送成功")
    else:
        print("发送失败")


#默认参数：
'''

#普通参数
'''

def send(user,content,xx):
    print(user,content,xx)

send("user1:","hello","ok")
'''
#默认参数：

'''
def send(user,content,xx="OK"):
    print(user,content,xx)

send("user1:","hello","FFFF")
send("user1","hello")
'''
#指定参数

'''
def send(user,content):
    print(user,content)

send(content="hello", user = "user1")
'''


#参数*
'''

def f1(*args):
    print(args)
list1 = [11,22,"alex","hehe"]
f1(*list1)  # 把列表中的每个值，分别作为元祖的每个元素

#f1(list1)  #把整个列表内容当成一个整体作为元祖的一个元素

#f1(list1,'name')

#f1(list1)  #把整个内容当成一个整体作为元祖的一个元素
#f1(*list1)  # 把列表中的每个值，分别作为元祖的每个元素

'''

#**

'''
def f1(**args):
    print(args,type(args))

dict1 = {'k1':"v1",'k2':"v2"}
f1(kk=dict1)
#dict1 = {'k1':"v1",'k2':"v2"}
#f1(**dict1)
#f1(n1="test",n2=30)

'''

#万能参数
'''
def f1(*args,**kwargs):
    print(args)
    print(kwargs)

f1(11,22,33,44,k1="v1",k2="v2")
'''

'''
s1 = "i am {0},age {1}".format("alex",18)
print(s1)
s2 =  "i am {0},age {1}".format(*["alex",18])
print(s2)
#####################3
#s1 = "i am {name},age {age}".format(name="test",age=18)
#print(s1)
dic = {'name':'alex',"age":18}
s2 = "i am {name},age {age}".format(**dic)
print(s2)
'''
#全局变量,所有作用域都可读
#对全局变量进行【重新赋值】，需要global
#特殊：列表字典，可修改，但是不可以重新赋值
#全局变量必须使用大写


#对全局变量进行【重新赋值】，需要global
'''

NAME = "test"

def f1():
    age = 18
    global NAME #表示，name是全局变量。
    NAME = "123"
    print(age,NAME)
def f2():
    age = 19
    print(age,NAME)
f1()
f2()
'''



#特殊：列表字典，可修改，但是不可以重新赋值
'''
NAME = [11,22,33,44]
def f1():
    #NAME.append(9999)  #可以修改
    NAME = "123"   #不可以重新赋值
    print(NAME)

f1()
'''

#三元运算，三目运算
#如果1==1 成立，name = "alex"
# 否则，name = "SB"

#name = "alex" if 1 == 1 else "SB"  ; print(name)

#lamb表达式
'''

def f1(a1):
    return a1 + 100
r1 = f1(100)
print(r1)

f2 = lambda a1,a2=9: a1 + a2 +100

r2 = f2(9)
print(r2)

'''
# 0 ,None ,"",[],()  都是False
#print(bool(()))
# all  所有为真，才为真
'''

n = all([1,2,3,()])
print(n)
'''
# any 只要有真，就为真,也就是都为假，才会为假
'''

n = any([[],0,"",None])
print(n)

'''
'''

print(bin(5))
print(oct(9))
print(hex(15))

'''

# 字符串转换字节类型
# bytes(只要转换的字符串，按照什么编码)
'''
s = "李杰"   #一个字节8位，一个汉字三个字节

n = bytes(s,encoding="utf-8")
print(n)
n = bytes(s,encoding="gbk")
print(n)
'''
#字节转化成字符串
'''
n1 = str(bytes("李杰",encoding="utf-8","utf-8"))
print(n1)
'''

#文件操作
#1、打开文件
'''
f = open('db','r')   #只读
f = open('db','w')  #只写，首先把原文件清空
f = open('db','x')  #如果文件存在就报错。不存在，创建并写内容
f = open('db','a') #追加，文件末尾
'''
'''

f = open('db','r',encoding="utf-8")
data = f.read()
print(data,type(data))

'''

'''


f = open('db','rb')
data = f.read()
print(data,type(data))
'''

'''


f = open('db','a',encoding="utf-8")
f.write("李杰")
f.close()
'''
'''

f = open('db','ab')
f.write(bytes("李杰",encoding="utf-8"))
f.close()
'''
'''

f = open('db','r+',encoding="utf-8")
data = f.read()
print(data)
f.write("777")
f.close()
'''
'''

#指定写的位置
f = open('db','r+',encoding="utf-8")  #如果打开模式无b，则read，按照字符读取
data = f.read()
print(data)
print(f.tell())   # tell 获取当前的位置（字节）
f.seek(f.tell())    #调整当前指针位置，seek() 永远是以字节移动位置
f.write("777")   #当前指针位置开始向后覆盖
f.close()
'''

#2、操作文件
#read()   # 无参数，读全部：有参数，  b：按字节，无b ：按照字符
#tell()  #获取当前指针位置（字节）
#seek(1)  #指针调转到指定位置（字节）
#write()  # 写数据 ，b：字节； 无b：字符
#close
# fileno   #文件描述符
#flush  #强制写硬盘
#readline   仅读取一行

#truncate  截断，指针位置后清空。

# for循环文件对象 f = open(xxx)
'''
for line in f:
    print(line)
 #3、关闭文件
f.close()

with open('xb') as f:   #代码块执行完成后自动关闭文件
    pass

with open('db1') as f1,open("db2") as f2:   #打开两个文件
    pass

'''
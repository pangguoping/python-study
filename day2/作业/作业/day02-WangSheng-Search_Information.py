#!/usr/bin/env python
# _*_ coding:utf8 _*_

import time

#用于设置标志位
def BreakFlag():
    while True:
        Break_Flag = raw_input('''\t\t\t是否继续？(y/n)''')
        if Break_Flag == 'y' or Break_Flag == 'n':
            return Break_Flag
        else:
            print '''\t\t输入错误，请重新输入！\n'''


Info_File = open('information.txt','r') #只读方式打开员工信息表文件
Employee_Info = Info_File.readlines() #读入员工信息，并生成一个员工信息表列表，列表中元素为员工信息字符串
Info_File.close() #关闭员工信息表文件
Break_Flag = ''
print '''\n\t\t\t\t\033[34;1m您好，欢迎来到员工信息查询系统！\033[0m\n'''
while Break_Flag != 'n':
    while True:
        Search_Info = raw_input('''\n\t\t\t请输入您需要查询的信息:''')
        if len(Search_Info) > 2:   #判断输入字符长度，小于3个字符，则需要重新输入
            break
        else:
            print '''\n\t\t\t\033[31;1m您输入不合法，请重新输入！\033[0m\n'''
    count_number = 0
    Search_Info_List = []
    for i in Employee_Info:
        if i.count(Search_Info) > 0:  
            Search_Info_List.append(i.replace(Search_Info,'''\033[42;31;1m%s\033[0m'''%Search_Info))  #将搜索到的字符串进行替换，并追加到Search_Info_List列表中
            count_number += i.count(Search_Info) #统计每次搜寻到字符串的个数，并进行累加
    if count_number > 0: #若搜寻到字符串，将统计到的字符串总个数和包含字符串的列表进行屏幕打印
        print '''\n\t\t\t共查询到:\033[31;1m %s \033[0m条信息！\n'''%count_number 
        for i in Search_Info_List:
            print i
        Break_Flag = BreakFlag()  
    else: 
        print '''\n\t\t\t\033[31;1m没有您查找的信息！\033[0m\n'''
        Break_Flag = BreakFlag()
for i in range(3):
    print '''\n\t\t\t\033[34;5m谢谢使用员工信息查询系统，%s秒后，退出系统\033[0m'''%(3-i)
    time.sleep(1)
exit()
    

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
"""



tp1 = "i am %s" % "tiantian"
print(tp1)
tp2 = "i am %s age %d" %("tiantian",19)
print(tp2)
tp3 = "i am %(name)s age %(age)d" % {'name':'tiantian','age':18}
print(tp3)
#右对齐
tp4 = "%(name)+30s age %(age)d" % {'name':'tiantian','age':18}
print(tp4)
#左对齐
tp5 = "%(name)-30s age %(age)d" % {'name':'tiantian','age':18}
print(tp5)

#保留两位小数，四舍五入
tp6 = "%(a).2f" %{'a':1.37834}
print(tp6)
tpl = "i am %s" % "alex"

tpl = "i am %s age %d" % ("alex", 18)

tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}

tpl = "percent %.2f" % 99.97623
#
tpl = "i am %(pp).2f" % {"pp": 123.425556}
print(tpl)

tpl = "i am %(pp).2f %%" % {"pp": 123.425556,}
print(tpl)
"""
"""
s1 = "i am {} ,age {}, {}".format("seven",18,'alex')
print(s1)
s2 = "i am {}, age {}, {}".format(*["seven",18,'alex'])
print(s2)
s3 = "i am {0} , age {1}, really {0}".format("seven",18)
print(s3)
s3 = "i am {0} , age {1}, really {0}".format(*["seven",18])
print(s3)
s4 = "i am {name},age {age},really {name}".format(name="seven",age=18)
print(s4)
s5 = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
print(s5)
s6 = "i am {0[0]},age{0[1]} ,really {0[2]}".format([1,2,3],[11,22,33])
print(s6)
s7 = "i am {:s}, age {:d} , money {:f}".format("seven",18,88888.1)
print(s7)
s8 = "i am {:s} , age {:d}".format(*["seven",18])
print(s8)
s9 = "i am {name:s}, age {age:d}".format(name="seven", age=18)
print(s9)
s10 = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
print(s10)
s11 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(s11)
s12 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(s12)
s13 = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
print(s13)
s14 = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
print(s14)


"""
'''

li = [11,22,33,44]
s = filter(lambda x:x>22,li)
print(s)
r =range(100)
print(r)
for i in r:
    print(i)
'''

'''

def func():
    print('start')
    yield 1
    yield 2
    yield 3
ret = func()
a1 = ret.__next__()  #进入函数找到yield，获取yield后面的数据
print(a1)
a2 = ret.__next__() #进入函数找到yield，获取yield后面的数据
print(a2)
a2 = ret.__next__()  #进入函数找到yield，获取yield后面的数据
print(a2)
'''
'''

a = iter([1,2,3,4,5])
a1 = a.__next__()
print(a1)
a2 = a.__next__()
print(a2)
a3 = a.__next__()
print(a3)
a4 = a.__next__()
print(a4)
a5 = a.__next__()
print(a5)

'''

'''
def func(n):
    n += 1
    if n >= 4:
        return 'end'
    return func(n)

r = func(1)
print(r)
'''

'''
import sys
import time


def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 100):
        time.sleep(0.1)
        view_bar(i, 100)

'''
import sys
print(sys.path)
#结果：

sys.argv           #命令行参数List，第一个元素是程序本身路径
sys.exit(n)        #退出程序，正常退出时exit(0)
sys.version        #获取Python解释程序的版本信息
sys.maxint         #最大的Int值
sys.path           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       #返回操作系统平台名称
sys.stdin          #输入相关
sys.stdout         #输出相关
sys.stderror       #错误相关

os.getcwd()                 #获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")         #改变当前脚本工作目录；相当于shell下cd
os.curdir                   #返回当前目录: ('.')
os.pardir                   #获取当前目录的父目录字符串名：('..')
os.makedirs('dir1/dir2')    #可生成多层递归目录
os.removedirs('dirname1')   #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')         #生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')         #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')       #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()                 #删除一个文件
os.rename("oldname","new")  #重命名文件/目录
os.stat('path/filename')    #获取文件/目录信息
os.sep                      #操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep                  #当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep                  #用于分割文件路径的字符串
os.name                     #字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")   #运行shell命令，直接显示
os.environ                  #获取系统环境变量
os.path.abspath(path)       #返回path规范化的绝对路径
os.path.split(path)         #将path分割成目录和文件名二元组返回
os.path.dirname(path)       #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)      #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)        #如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)         #如果path是绝对路径，返回True
os.path.isfile(path)        #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)         #如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)      #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)      #返回path所指向的文件或者目录的最后修改时间
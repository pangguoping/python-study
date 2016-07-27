#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import re

#匹配外部有括号，内部没有小括号
bracket_flag_str = re.compile('(\([^()]+\))')
#从左到右匹配乘除
mul_div_exec_str = re.compile('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*')

def sign_exec(args):
    """
    加减除了，将+-替换为-,--换为+
    :param args: 表达式字符串
    :return: 返回替换后的结果
    """
    return re.sub(r'\+\-','-',re.sub(r'\-{2}','+',args))

def add_sub_exec(args):

    """
    加减计算
    :param args:
    :return: 返回结果
    """
    if args.startswith('-'):
        args = '0%s' %(args)
    elif args.startswith('+'): #以+开头，将开头的+去掉
        args = re.sub(r'\+','',args)
    args = re.sub(r'\-','+-',args)  #将-替换为+-
    args_list = re.split(r'\+',args) #以+将字符串分割为列表
    for i in args_list:
        args_list[args_list.index(i)] = float(i) #转换为float类型
    result = sum(args_list) #计算和
    return result

def exec_had_drop_contect(args):
    """
    处理括号内优先计算
    :param args:
    :return:
    """
    if not mul_div_exec_str.search(args):   #如果不匹配，说明已计算完成
        return args
    else:
        #将字符串分割成两部分
        before,after = mul_div_exec_str.split(args,1)
        contect = mul_div_exec_str.search(args).group()
        #计算乘法
        if len(contect.split('*'))>1:
            v1,v3 = contect.split('*')
            v = float(v1)*float(v3)
        else:
            #除法
            v1,v3 = contect.split('/')
            if float(v3) == float(0):
                exit('不能除以0')
            else:
                v = float(v1)/float(v3)
        #拼接字符串
        new_str = '%s%s%s'%(before,v,after)
        #拼接后的字符串进行加减号处理
        had_sign_exec_str = sign_exec(new_str)
        #args 重新赋值
        args = had_sign_exec_str
    return exec_had_drop_contect(args)

def drop_brakets(args):
    """
    括号处理函数
    :param args:
    :return:
    """
    #没有括号，结束递归
    if not bracket_flag_str.search(args):
        return args
    else:
        before,mid,after = bracket_flag_str.split(args,1)
        #print(before,mid,after)
        had_drop_contect = mid[1:-1]
        add_sub_result = exec_had_drop_contect(had_drop_contect)
        result = add_sub_exec(add_sub_result)
        args = '%s%s%s'%(before,str(result),after)
    return drop_brakets(args)

def calc(args):
    """
    计算函数，先处理括号，然后计算乘除，再计算加减，并返回结果
    :param args:
    :return: 返回计算结果
    """
    no_brakets = drop_brakets(args)
    no_mul_div = exec_had_drop_contect(no_brakets)
    result = add_sub_exec(no_mul_div)
    print(result)

def check_formula(args):
    """
    判断用户输入字符串是否符合
    :param args:
    :return:
    """
    if len(re.findall('\(',args)) == len(re.findall('\)',args)):
        return True
    else:
        print('括号数量错误')
        return False

#运行主函数
if __name__ == '__main__':
    print('欢迎使用只带小括号计算器'.center(60,'*'))
    inp = input('请输入你要计算的表达式，只支持加减乘除小括号计算：')
    inp = inp.strip()
    res = check_formula(inp)
    if res:
        #字符串符合表达式，执行计算
        calc(inp)
    else:
        #退出
        exit('格式输入错误')

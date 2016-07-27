#!/usr/bin/env python
# -*-coding=utf-8-*-
#pangguoping

import prettytable,time,os

USER_STATE = False
LOGIN_STATE=False
USER_NAME = None
def check_auth(func):
    def inner(*args,**kwargs):
        if USER_STATE:
            r = func(*args,**kwargs)
            return r
        else:
            print('\033[31;1m用户%s没有权限操作\033[0m' %USER_NAME)
    return inner

def check_user_state(USER_NAME):
    with open('user_info','r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(USER_NAME) == True and USER_NAME == line.split('|')[0]:
                user_states = line.split('|')[4]
                if user_states == '1':
                    global USER_STATE
                    USER_STATE = True
                else:
                    pass
    return USER_STATE
def user_name_list():
     name_list = []
     with open('user_info','r',encoding='utf-8') as f:
         for line in f:
             user_name = line.strip().split('|')[0]
             name_list.append(user_name)
     return name_list

def user_pwd_list():
    pwd_list = []
    with open('user_info','r',encoding='utf-8') as f:
        for line in f:
            user_pwd = line.strip().split('|')[1]
            pwd_list.append(user_pwd)
    return pwd_list


def login():
    name_list = user_name_list()
    pwd_list = user_pwd_list()
    USER_NAME = input('请输入用户名：')
    pwd = input('请输入密码：')
    #print(name_list)
    #print(pwd_list)
    #print(name_list.index(USER_NAME))
    #print(pwd_list[1])
    if pwd == pwd_list[name_list.index(USER_NAME)]:
        global LOGIN_STATE
        LOGIN_STATE = True
        print("登陆成功")
    return LOGIN_STATE, USER_NAME
#r=login()
#r1,r2= login()
#print(r1,r2)
#print(r)
def register():
    name_list = user_name_list()
    user_name = input('请输入用户名：')
    if user_name in name_list:
        print('Sorry,用户%s已经被注册！请更换其他名称。谢谢' %user_name)
        return False,user_name
    else:
        pwd = input('请输入密码：')
        mail = input('请输入邮箱：')
        tel = input('请输入电话：')
        info = [user_name,pwd,mail,tel,'0']
        new_user = '|'.join(info)
        with open('user_info','a',encoding='utf-8') as f:
            f.write('%s\n' %new_user)

    return True,user_name
def find_user_list(USER_NAME):
    with open('user_info','r',encoding='utf-8') as f:
        for line in f:
            if line.startswith(USER_NAME) == True and USER_NAME == line.strip().split('|')[0]:
                user_name = USER_NAME
                pwd = line.strip().split('|')[1]
                mail = line.strip().split('|')[2]
                tel = line.strip().split('|')[3]
                user_type = line.strip().split('|')[4]
                new_user_list = [user_name,pwd,mail,tel,user_type]
                #print(new_user_list)
            else:
                pass
    return new_user_list
#print(find_user_list('alex'))
def change_pwd(USER_NAME):
    new_pwd = input('请输入新密码：')
    with open('user_info','r',encoding='utf-8') as old_file,open('user_info_new','w',encoding='utf-8') as new_file:
        for line in old_file:
            if line.startswith(USER_NAME) == True and USER_NAME == line.strip().split('|')[0]:
                line_list = find_user_list(USER_NAME)
                line_list[1] = new_pwd
                new_line = '|'.join(line_list)
                new_file.write('%s\n' %new_line)
                print('账号%s,密码修改成功。' %USER_NAME)
            else:
                new_file.write(line)
    os.rename('user_info', 'user_info.bak')
    os.rename('user_info_new', 'user_info')
    os.remove('user_info.bak')
    return True

def change_mail(USER_NAME):
    new_mail = input("请输入新邮箱：")
    with open('user_info','r',encoding='utf-8') as old_file,open('user_info_new','w',encoding='utf-8') as new_file:
        for line in old_file:
            if line.startswith(USER_NAME) == True and USER_NAME == line.strip().split('|')[0]:
                line_list = find_user_list(USER_NAME)
                line_list[2] = new_mail
                new_line = '|'.join(line_list)
                new_file.write('%s\n' % new_line)
                print('账号%s,mail修改成功。' % USER_NAME)
            else:
                new_file.write(line)
    os.rename('user_info','user_info.bak')
    os.rename('user_info_new','user_info')
    os.remove('user_info.bak')
    return True
#change_mail('alex')
def change_tel(USER_NAME):
    new_tel = input('请输入新手机号码：')
    with open('user_info','r',encoding='utf-8') as old_file , open('user_info_new','w',encoding='utf-8') as new_file:

        for line in old_file:
            if line.startswith(USER_NAME) and USER_NAME == line.strip().split('|')[0]:
                new_list = find_user_list(USER_NAME)
                new_list[3] = new_tel
                new_line = '|'.join(new_list)
                new_file.write('%s\n' %new_line)
            else:
                new_file.write(line)
    os.rename('user_info','user_info.bak')
    os.rename('user_info_new','user_info')
    os.remove('user_info.bak')
    return True

def modify_user_info(USER_NAME):
    row=prettytable.PrettyTable()
    row.field_names=['修改密码','修改邮箱','修改联系电话']
    row.add_row([1,2,3])
    print(row)
    while True:
        inp=input('请选择功能菜单,\033[32;1m返回主菜单请输入b或者back\033[0m:')
        if inp == '1':
            res=change_pwd(USER_NAME)
            if res:
                print('密码修改成功')
                break
        elif inp == '2':
            res=change_mail(USER_NAME)
            if res:
                print('邮箱修改成功')
                break
        elif inp == '3':
            res=change_tel(USER_NAME)
            if res:
                print('电话修改成功')
                break
        elif inp == 'back' or inp == 'b':
            break
        else:
            print('输入有误,请重新输入!')
    return True
#把文件中的密码设置为空
def no_pwd_file():
    with open('user_info','r') as old_file,open('no_pwd','w') as new_file:
        for line in old_file:
            line = line.strip().split('|')
            del line[1]
            line = '|'.join(line)
            new_file.write('%s\n' %line)

def search(keywords):
        no_pwd_file()
        res = []
        search_res_list = []
        user_type = None
        with open('no_pwd', 'r') as f:
            for line in f:
                line = line.strip()
                if keywords in line:
                    res.append(line)
        if len(res) == 0:
            print('通过关键字查询,无结果.')
        else:
            for line in res:
                if line.split('|')[3] == '0':
                    user_type = '普通用户'
                elif line.split('|')[3] == '1':
                    user_type = '管理员'
                li = [line.split('|')[0], line.split('|')[1],
                      line.split('|')[2], user_type, ]
                search_res_list.append(li)
            row = prettytable.PrettyTable()
            row.field_names = ['用户名', '邮箱', '电话', '用户类型']
            for line in search_res_list:
                row.add_row([line[0], line[1], line[2], line[3], ])
            print(row)
        os.remove('no_pwd')


#查询所有用户信息
@check_auth
def show_all_user():
    no_pwd_file()
    row = prettytable.PrettyTable()
    row.field_names = ['用户名','密码','邮箱','电话','账号类型']
    with open('no_pwd','r') as f:
        for line in f:
            line = line.strip()
            if line.split('|')[3] == '1':
                user_type = '管理员'
            elif line.split('|')[3] == '0':
                user_type = '普通用户'
            row.add_row([line.split('|')[0],'****',line.split('|')[1],line.split('|')[2],user_type])
    print(row)
    os.remove('no_pwd')
    return True
#删除指定的账号
@check_auth
def delete_user():
    show_all_user()
    name = input('请输入要删除的账号')
    name_list = user_name_list()
    if name in name_list:
        with open('user_info','r',encoding='utf-8') as old_file,open('user_info_new','w') as new_file:
            for line in old_file:
                if line.strip().startswith(name) and name == line.strip().split('|')[0]:
                    pass
                else:
                    new_file.write(line)
        os.rename('user_info','user_info.bak')
        os.rename('user_info_new','user_info')
        os.remove('user_info.bak')
        print('账号%s删除完成 ' %name)

@check_auth
def edit_user():
    row = prettytable.PrettyTable()
    row.field_names = ['增加用户','删除用户']
    row.add_row([1,2])
    print(row)
    while True:
        inp = input('请选择功能\033[32;1m返回输入back或者b\033[0m:')
        if inp == '1':
            res,name = register()
            if res:
                print('新增用户%s' %name)
        elif inp == '2':
            delete_user()
            break
        elif inp == 'b' or inp == 'back':
            break
        else:
            print('输入有误，请重新登录')

@check_auth
def update_user(account):
    with open('user_info','r') as old_file,open('user_info_new','w') as new_file:
        for line in old_file:
            if line.strip().startswith(account) and account == line.strip().split('|')[0]:
                new_line_list = line.strip().split('|')
                if new_line_list[4] == '1':
                    return False
                else:
                    new_line_list[4]='1'
                    new_line = '|'.join(new_line_list)
                    new_file.write('%s\n' %new_line)
            else:
                new_file.write(line)
    os.rename('user_info','user_info.bak')
    os.rename('user_info_new','user_info')
    os.remove('user_info.bak')
    return True
@check_auth
def reset_pwd(account,new_pwd):
    with open('user_info','r',encoding='utf-8') as old_file,open('user_info_new','w',encoding='utf-8') as new_file:
        for line in old_file:
            if line.strip().startswith(account) and account == line.strip().split('|')[0]:
                new_line_list = line.strip().split('|')
                new_line_list[1] = new_pwd
                new_line = '|'.join(new_line_list)
                new_file.write('%s\n' %new_line)
            else:
                new_file.write(line)
    os.rename('user_info','user_info.bak')
    os.rename('user_info_new','user_info')
    os.remove('user_info.bak')
    return True

def logout():
    global USER_STATE,LOGIN_STATE,USER_NAME
    USER_STATE,LOGIN_STATE,USER_NAME = False,False,None
    exit('退出程序！！')

def show_menu():
    row = prettytable.PrettyTable()
    row.field_names=['查看%s账户信息'%USER_NAME,'修改%s账户信息' %USER_NAME,
                     '模糊查询',
                     '查看所有用户',
                     '提升指定用户为管理员',
                     '重置成员密码',
                     '增加删除成员',
                     '退出']
    row.add_row([1,2,3,4,5,6,7,'q|quit'])
    print('\033[32;1m欢迎访问oldboy培训管理系统\033[0m'.center(120))
    print(row)
def show_user_info(USER_NAME):
    user_info_list = []
    with open('user_info','r',encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith(USER_NAME) == True and USER_NAME == line.split('|')[0]:
                user_info_list.extend(line.split('|'))
            #print(user_info_list)
        if len(user_info_list) == 0:
            print('此用户不存在或没有相关权限')
        else:
            user_type = None
            if user_info_list[4] == '1':
                user_type = '管理员'
            elif user_info_list[4] == '0':
                user_type = '普通用户'
            row = prettytable.PrettyTable()
            row.field_names = ['用户名','密码','邮箱','电话','账户类型']
            row.add_row([user_info_list[0],'*****',user_info_list[2],user_info_list[3],user_type])
            print(row)
#show_user_info('alex')
def main():
    row = prettytable.PrettyTable()
    row.field_names = ['功能','登录','注册用户']
    row.add_row(['操作编号','1','2'])
    print(row)
    inp = input('请输入操作编号:')
    if inp == '1':
        global LOGIN_STATE,USER_NAME
        LOGIN_STATE,USER_NAME = login()
        global USER_STATE
        USER_STATE = check_user_state(USER_NAME)
        if LOGIN_STATE == True:
            while True:
                show_menu()
                inp=input('请输入相应的操作编号，祝你好运，加油！')
                if inp == '1':
                    show_user_info(USER_NAME)
                    time.sleep(1)
                elif inp == '2':
                    modify_user_info(USER_NAME)
                elif inp == '3':
                    keywords = input('请输入要查询的关键字')
                    res = search(keywords)
                elif inp == '4':
                    show_all_user()
                elif inp == '5':
                    res = show_all_user()
                    if res:
                        account = input('请输入您要提升的用户账号名称:')
                        name_list = user_name_list()
                        if account in name_list:
                            res = update_user(account)
                            if res:
                                print('权限提升成功')
                            else:
                                print('\033[31;1m%s已经是管理员,'
                                      '无需提升权限!\033[0m' % account)
                            time.sleep(1)
                        else:
                            print('\033[31;1m无此账户:%s信息\033[0m' % account)
                    else:
                        pass
                elif inp == '6':
                    res = show_all_user()
                    if res:
                        account = input('请输入您要修改用户账号名称:')
                        name_list = user_name_list()
                        if account in name_list:
                            new_pwd = input('请输入账户的新密码:')
                            res = reset_pwd(account, new_pwd)
                            if res:
                                print('密码已重置成功')
                        else:
                            print('\033[31;1m无此账户:%s信息\033[0m' % account)
                        time.sleep(1)
                    else:
                        pass
                        time.sleep(1)
                elif inp == '7':
                    edit_user()
                    time.sleep(1)
                if inp == 'q' or inp == 'quit':
                    logout()
        else:
                print('输入有误,请重新输入!')

    elif inp == '2':
        res, name = register()
        if res:
            print('用户%s注册成功' % name)
        else:
            pass



main()
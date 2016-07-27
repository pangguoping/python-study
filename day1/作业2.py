#!/usr/bin/env  python
# -*- coding:utf-8 -*-

#!/usr/bin/env  python
# -*- coding:utf-8 -*-
# auther :  pangguoping

black_file=open('black_user.txt','r')  #用户黑名单
user_file = open('user.txt','r') 保存用户名密码
message_dict = { }
#下面for循环是把用户名密码转换为字典
for i in user_file:
    line = i.strip()
    line_list = line.split()
    message_dict[line_list[0]] = line_list[1]
user_file.close()



counter = 0   #定义一个计数器
last_name = ""   #定义一个空变量，用于保存登录的用户名
while True:

    user_name = input("please input your name:")   #输入用户名
    user_passwd = input("please input your password:")  #输入密码
    line = back_file.read()

    if user_name in line:
        print('your name is blackuser,please call administrator')
        print(user_name)
        break
        f.close()
    else:
        if user_name in message_dict.keys() and user_passwd == message_dict[user_name]:
            print("Welcom to login !")
            break
        elif user_name in message_dict.keys():

            if last_name == user_name:
                if counter < 2:
                    last_name = user_name
                    print('counter1',counter)
                    print("Invalid username or  password !")
                    counter += 1
                    print('counter2', counter)

                else:
                    add_black = open('black_user.txt', 'a')
                    add_black.write(user_name+'\n')
                    add_black.close()
                    print("your name is clock",user_name)
                    break
            else:
                last_name = user_name
                counter = 0
                print("Invalid username or  password !")
                print('counter3', counter)
                counter += 1
                print('counter4', counter)

        else:
                last_name = user_name
                counter = 0
                print("Invalid username or  password !")










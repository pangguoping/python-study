#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.1.103', port=3306, user='root', passwd='123456', db='test')
# 开启自动提交SQL，如果这里不设置，以后的命令需要执行conn.commit()来提交执行，否则都在内存中
conn.autocommit(True)

# 创建游标
cur = conn.cursor()

# 执行普通SQL，并返回受影响行数
effect_row = cur.execute("insert into t1 values (1, 'Boss')")
print(effect_row)  # out：1
#
# 执行带占位符的SQL，并返回受影响行数
effect_row = cur.execute("insert into t1 values (2,'%s')" % "xiaodi")
print(effect_row)  # out：1
#
# 执行多行数据的SQL，并返回受影响行数
effect_row = cur.executemany("insert into t1(id,name) values (%s, %s)", [(3, 'zhubajie'), (4, 'sunwukong')])
print(effect_row)  # out: 2

# 获取最新自增ID，注意：如果该表的列是非自增类型的，则获取到的数值为0
id = cur.lastrowid
print(id)  # out :4
cur.execute('select * from t1')

# 获取第一行数据
row_1 = cur.fetchone()
print(row_1)  # out:  (1, 'Boss')
# 获取前n行数据
row_2 = cur.fetchmany(3)
print(row_2)  # out: ((2, 'xiaodi'), (3, 'zhubajie'), (4, 'sunwukong'))
# 获取所有数据
row_3 = cur.fetchall()
print(row_3)  # out: ((1, 'Boss'), (2, 'xiaodi'), (3, 'zhubajie'), (4, 'sunwukong'))
# 提交
conn.commit()

# 关闭游标
cur.close()
# 关闭连接
conn.close()


# 游标设置为字典类型
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/t1", max_overflow=5)

# 执行SQL
# cur = engine.execute(
#     "INSERT INTO hosts (host, color_id) VALUES ('1.1.1.22', 3)"
# )

# 新插入行自增ID
# cur.lastrowid

# 执行SQL
# cur = engine.execute(
#     "INSERT INTO hosts (host, color_id) VALUES(%s, %s)",[('1.1.1.22', 3),('1.1.1.221', 3),]
# )


# 执行SQL
# cur = engine.execute(
#     "INSERT INTO hosts (host, color_id) VALUES (%(host)s, %(color_id)s)",
#     host='1.1.1.99', color_id=3
# )

# 执行SQL
# cur = engine.execute('select * from hosts')
# 获取第一行数据
# cur.fetchone()
# 获取第n行数据
# cur.fetchmany(3)
# 获取所有数据
# cur.fetchall()
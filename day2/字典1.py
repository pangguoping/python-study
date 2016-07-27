#!/usr/bin/env  python
# -*- coding:utf-8 -*-
#name = [1,3,4,5,5,6,7]
id_db = {
    20123123232323:{
        'name':"Dashanpao",
        'age': 24,
        'addr': 'Dongbei'
    },
    201231232323245: {
        'name': "Dashanpao",
        'age': 24,
        'addr': 'Dongbei'
    }

}
print(id_db)
print(id_db[201231232323245])
id_db[201231232323245]['name'] = "wangminghu"   #修改value值
id_db[201231232323245]['qq_of'] = 123456    #增加value
id_db[201231232323245].pop("addr")  #删除value "addr"

#获取指定key的值
v = id_db.get(201231232323245)
print(v)

#字典覆盖
dic2 ={
    'name':"wang"
}
id_db.update(dic2)
print(id_db)

#获取字典的所有key
print(id_db.values())
#获取字典所有的value
print(id_db.keys())
#id_db.has_key(asdfdsfdsfd)  #only in 2.x

1234566 in id_db   # equals to above has_key(x)

#取一个key，如果不存在，就设置
print(id_db.setdefault(12312323,"haha"))
print(id_db)

#
print(id_db.fromkeys([1,2,3,44,4,5,6],'dddd'))

#随机删除字典中的元素

#循环字典
for k,v in id_db.items():#效率低，因为要有一个dict to list 的转换过程
    print(k,v)

for key in id_db:  #效率高
    print(key,id_db[key ])
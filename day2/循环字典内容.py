#!/usr/bin/env  python
# -*- coding:utf-8 -*-

'''
id_db = {
    11:{
        'name':"A",
        'age': 20,
        'addr': 'C1'
    },
    12: {
        'name': "B",
        'age': 24,
        'addr': 'C2'
    }
}

'''
id_db = {
    11:{
        'name':"A",
        'age': 20,
        'addr': 'C1'
    },
    12: {
        'name': "B",
        'age': 25,
        'addr': 'C2'
    }
}
print(11 in id_db)   # equals to above has_key(x)

print(15 in id_db)


#获取字典的所有key的value值
#print(id_db.values())
#获取字典所有key
#print(id_db.keys())
#id_db.has_key(asdfdsfdsfd)  #only in 2.x

#print(11 in id_db)   # equals to above has_key(x)

#print(15 in id_db)

#取一个key，如果不存在，就设置
#print(id_db.setdefault(12312323,"haha"))
#print(id_db)


'''
for key in id_db:  #效率高
    print(key,id_db[key])
'''


'''
for k,v in id_db.items():#效率低，因为要有一个dict to list 的转换过程
    print(k,v)
'''




#1.取出字典某个key的value值
#print(id_db[11])

#2.修改某个字典key对应的value
#id_db[11]["name"]= "C"
#print(id_db)

#3.为某个key增加一个vlaue值
#id_db[11]["qq"]= "12345"
#print(id_db[11])

#4.删除指定key对应的指定value
#id_db[11].pop("name")
#print(id_db)

#5.获取指定key的value值,如果指定的key不存在，那么会返回None
#v = id_db.get(11)
#print(v)
#v = id_db.get(13)
#print(v)

#6.获取指定key的value值,如果指定的key不存在，那么会报错
#v = id_db[12]
#print(v)


#7.向子典中添加内容，如果key存在会替换原来的key中对应的value
#dic2 = {
#    'name':'adfsdfsd',
 #   11:{
#        'name:'"wangwang"
#    }

#}

#id_db.update(dic2)
#print(id_db)

#8.
#print(id_db.items())
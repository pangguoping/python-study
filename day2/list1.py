#!/usr/bin/env  python
# -*- coding:utf-8 -*-


name = ["1","2","3","4","5","6","7","8","9"]
print(name)
name.insert(5,"k")
name.insert(5,"z")
print(name)
name38=name[2:8]
#nameremove=name.remove("k")

print(name38)
print(name)
#删除加入的两个人
#name.remove("z")
name=name[:5] + name[7:]
#或者 del name[5:7]
print("name2")
print(name)
#name.remove("k")

#为组长加备注

name[0]="组长：" +  name[0]
#name[0]="a(组长)"
print(name)

#每隔一个元素打一个
name3=name[::2]
print(name3)

#列表中查找元素
name = ["1","2","3","4","5","6","7","8","9"]
#从列表中查找某个元素：
print("8" in name)
if 8 in name:
    print(8 is name)

#修改列表中的同一个元素的多个位置
name=[1,2,3,4,5,6,7,8,9,9]
for i in range(name.count(9)):
    ele_index = name.index(9)
    name[ele_index] = 99999999
print(name)


#列表合并
name.extend(name2)

#列表反转
name.remove()

#list排序
#python3.5 里面，字符和字母无法一块排序，但是python2.7里面不能这么排序
name.sort()

#删除指定元素
name.pop(i) # i的值为索引 ,pop()默认删除最后一个元素

#列表copy
#第一层的数据会copy，第二层的数据不会copy,相当于软连接,也就是浅copy
name3 = name.copy()



#列表深copy   ，完全克隆一份
#name4=copy.deepcopy(name)
#print(name4)





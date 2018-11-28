#!/user/bin/python


list = ['runoob', 786 , 2.23 , 'john' , 70.2 ]
tinylist = [123, 'john']

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist

list.append("php") #列表末尾添加元素
print list

list.count("php")

list.pop(1)
print list

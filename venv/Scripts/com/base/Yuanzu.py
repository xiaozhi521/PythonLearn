#!/user/bin/python
# -*- coding: UTF-8 -*-

tuple = ( 'runoob', 786 , 2.23 , 'john' , 70.2)
tinytuple = (123,'john')

print tuple
print tuple[0]
print tuple[2:5]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple

print "==========="
for aa in tuple:
    print aa



#元组不允许更新，列表是可以更新的


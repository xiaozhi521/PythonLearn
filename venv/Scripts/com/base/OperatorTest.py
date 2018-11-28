#!/user/bin/python
# -*- coding: UTF-8 -*-
# Python 运算符
a = 20
b = 30
# 算术运算符
print "a + b = ", (b-a)
print "a * b :", a * b
print "a / b :", a / b
print "a % b :", a % b

#比较运算符
if a >=b:
    print "a 大于 b"
else:
    print "a 小于 b"

if a <= b :
    print "a 小于 b"
else:
    print "a 大于 b"

#Python逻辑运算符
#and	x and y	    布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 	(a and b) 返回 20。
#or	    x or y	    布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	            (a or b) 返回 10。
#not	not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	    not(a and b) 返回 False


print ~2 ** a + b - a * b

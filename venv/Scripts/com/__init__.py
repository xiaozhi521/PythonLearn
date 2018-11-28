#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
'''
文件名：_init_.py
'''

print "111111111111111111111"
if False:
    print "True"
else:
  print "False"

"""
多行语句
"""
##方式一
days=[1,2,3,34,5]
print(days)  #输出：[1, 2, 3, 34, 5]
##方式二
days2={1,23,4}
print(days2)  #输出：set([1, 4, 23])
##方式三
days3 = '世界，' + \
    "你好" + \
    "！！！"
print(days3)  #输出：世界，你好！！！


y = 1
x = 2
print x + y
if x == 0 :
    print 10
elif x == 10:
    print 100
else :
    print x

print "sys.argv:"
print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)


a ,b ,c = 1 , 2.0 , "123f"
print a,b,c





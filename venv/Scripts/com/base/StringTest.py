#!/user/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
#Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
#解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
str = "Hello World"
print(str)  #输出完整的字符串
print str[0]    #输出字符串中的第一个字符
print str[2:5]  #输出字符串中第三个至第五个之间的字符串
print str[2:]   #输出从第三个开始的字符串
print str * 2   #输出字符串两次
print str + "TEST" #输出连接的字符串



print True|False
print "你好,Python!"

'''
[ : ]	截取字符串中的一部分
 in     成员运算符 - 如果字符串中包含给定的字符返回 True
 not in 成员运算符 - 如果字符串中不包含给定的字符返回 True
'''
print "e" in str  # True


print str.center(20, '=')
print str.endswith("ld")




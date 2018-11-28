#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar;

"""
    定义函数规则：
        1、函数代码块以 def 关键词开头，后接函数表示符名称和()
        2、任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数
        3、函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明
        4、函数内容以冒号起始，并且缩进
        5、return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
"""
"""
    1、默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误
    2、要注意定义可变参数和关键字参数的语法：
        *args是可变参数，args接收的是一个tuple
        **kw是关键字参数，kw接收的是一个dict
    3、以及调用函数时如何传入可变参数和关键字参数的语法:
        可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
        关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    4、使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
    5、命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
    6、定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
"""
def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print str
   return

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print fact(3)
def getLeapYear(startYear,endYear):
    "获取两年之间的闰年"
    yearList = []
    while True:
        if startYear > endYear:
            break
        if calendar.isleap(startYear):
            yearList.append(startYear)
        startYear += 1
    return yearList

print getLeapYear(1900,2000)
print len(getLeapYear(endYear = 2000,startYear = 1900))

"""
     匿名函数
    1、python 使用 lambda 来创建匿名函数。
    2、lambda只是一个表达式，函数体比def简单很多。
    3、lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    4、lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
    5、虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)
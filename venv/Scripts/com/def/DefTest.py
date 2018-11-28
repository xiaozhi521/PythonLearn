#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import __init__;

#__init__.printme("111")

Money = 2000

def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1

print Money
AddMoney()
print Money

import math

content = dir(math)
print content;

print locals() # 返回的是所有能在该函数里访问的命名
print globals() # 返回的是所有在该函数里能访问的全局名字
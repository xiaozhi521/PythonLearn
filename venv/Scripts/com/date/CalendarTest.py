#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar;
import time;

cal = calendar.month(2018,11)
print cal

print calendar.isleap(2020)  ## 是闰年返回 True，否则为 False。

print calendar.leapdays(2000,2020)

print "====获取 2000 年到 2020 之间的闰年==="
year = 2000
yearCount = 0
while True:
    if year > 2020:
        break
    if calendar.isleap(year):
        yearCount += 1
        print year
    year += 1

print "闰年数量：",yearCount

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;  # 引入time模块

current_time = time.time()
print current_time  #时间间隔是以秒为单位的浮点小数

clock = time.clock()

localtime = time.localtime()
print localtime
#   time.struct_time(tm_year=2018, tm_ mon=11, tm_mday=28, tm_hour=9, tm_min=46, tm_sec=59, tm_wday=2, tm_yday=332, tm_isdst=0)

localtime = time.asctime( time.localtime(time.time()) )
print localtime
#   Wed Nov 28 10:03:07 2018

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#   2018-11-28 10:03:39

print time.strftime("%Y-%m-%d %H:%M:%S %A %a", time.localtime())

#获取年
year = time.strftime("%Y",time.localtime())
print "年：" + year
#获取月
month = time.strftime("%m",time.localtime())
print "月：" + month
#获取年日
day = time.strftime("%d",time.localtime())
print "日：" + day
#获取小时 24 H
hour24 = time.strftime("%H",time.localtime())
print "24小时制：" + hour24
#获取小时 12 h
hour12 = time.strftime("%I",time.localtime())
print "12小时制：" + hour12
#获取分
minnus = time.strftime("%M",time.localtime())
print "分：" + minnus
#获取秒
seconds = time.strftime("%S",time.localtime())
print "秒：" + seconds

clock = time.clock()
print clock


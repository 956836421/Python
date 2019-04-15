#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
# path = input("文件路径:")
path = ["/data/logs1", "/data/logs","sdcard/ex","/sdcard/loomogoRecord/elevator_search","/sdcard/loomogoRecord/build/"]
print(path)
path_sel = input("select:")
a = "adb pull"
b = " "
c = path[int(path_sel)]
d = "F:/Python/img/"
e = input("存放文件夹")
cmdstr = a + b + c + b + d + e
os.system(cmdstr)
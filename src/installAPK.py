#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

path = "C:/Users/Wwd/Desktop/新建文件夹/Apk"
path_list = os.listdir(path)
path_list.sort()  # 对读取的路径进行排序

for filename in path_list:
    with open("Text.txt","a") as f:
        f.write(os.path.split(os.path.join(path, filename))[-1].split(".")[0]+"\n")
result = []
with open('Text.txt','r') as f:
	for line in f:
		result.append(list(line.strip('\n').split(',')))
length = (len(result))
for i in  range(length):
    i += 1
    print(i,"-",result[i-1])
os.remove("Text.txt")
sys = input("输入数字进行选择：")
while True:
    if sys.isdigit():
        break
    else:
        print("输入错误，请输入整数！！！（例如：1,2,3,4.....）")
        sys = input("请重新输入：")
info = (result[int(sys)-1])
info = ','.join(info)
apk = (info +".apk")
print(apk)

cmdstr = "adb install -r " + path + '/'+apk
#print(cmdstr)
print("正在安装.......................")
os.system("adb root")
os.system(cmdstr)
print("完成")
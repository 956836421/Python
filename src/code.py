#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class ProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width

    def __call__(self, x):
        self.pointer = int(self.width * (x / 100.0))
        return "|" + "#" * self.pointer + "-" * (self.width - self.pointer) + "|\n %d任务完成！ " % int(x)

if __name__ == '__main__':
    import time,os
    pb = ProgressBar()

    for i in range(0,101,2):
        os.system('cls')
        print(pb(i))
        time.sleep(0.1)
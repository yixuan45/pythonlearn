# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
from time import sleep


def func1(name):
    print("当前进程ID：", os.getpid())
    print("父进程ID：", os.getpid())
    print(f"process:{name} start")
    sleep(3)
    print(f"process:{name} end")


"""这是一个关于windows上多进程实现的bug。
在windows上，子进程会自动import启动它的这个文件，而
在import的时候是会自动执行这些语句的。
如果不加__main__限制的话，就会无限递归创建子进程，进
而报错。
于是import的时候使用 __name__ =="__main__" 保护
起来就可以了"""

if __name__ == '__main__':
    print("当前进程ID：", os.getpid())
    # 创建进程
    p1 = Process(target=func1, args=('p1',))
    p2 = Process(target=func1, args=('p2',))
    p1.start()
    p2.start()

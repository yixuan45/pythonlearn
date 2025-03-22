# -*- coding: utf-8 -*-
from multiprocessing import Process
from time import sleep


class MyProcess(Process):
    def __init__(self, name):
        Process.__init__(self)  # 第二行代码 Process.__init__(self) 的作用是调用父类 Process 的构造函数（__init__ 方法）。
        self.name = name

    def run(self):
        print(f"Process:{self.name} start")
        sleep(3)
        print(f"Process:{self.name} end")


if __name__ == '__main__':
    # 创建进程
    p1 = MyProcess("p1")
    p2 = MyProcess("p2")
    p1.start()
    p2.start()

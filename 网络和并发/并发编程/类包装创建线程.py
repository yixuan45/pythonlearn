# -*- coding: utf-8 -*-
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):  # 这是重写方法
        print(f"线程{self.name},start")  # 线程创建开始就会执行的语句
        for i in range(3):
            print(f"线程{self.name},{i}")
            time.sleep(2)
        print(f"线程{self.name},end")


if __name__ == '__main__':
    print("主线程，start")
    # 创建线程
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    # 启动线程
    t1.start()
    t2.start()
    print("主线程,end")

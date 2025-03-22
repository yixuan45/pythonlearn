# -*- coding: utf-8 -*-
from threading import Thread
import time


def func1(name):
    print(f"线程{name},start")
    for i in range(3):
        print(f"线程:{name},{i}")
        time.sleep(1)
    print(f"线程{name},end")


if __name__ == '__main__':
    print("主线程，start")
    # 创建线程
    t1 = Thread(target=func1, args=("a1",))
    t2 = Thread(target=func1, args=("a2",))
    # 启动线程
    t1.start()
    t2.start()

    print("主线程,end")

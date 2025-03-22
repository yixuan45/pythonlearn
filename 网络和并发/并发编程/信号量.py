# -*- coding: utf-8 -*-
from threading import Thread, Lock
from time import sleep
from multiprocessing import Semaphore

"""
一个房间一次只允许两个人通过
若不使用信号量，会造成所有人都进入这个房子
若只允许一人通过可以用锁-Lock()
"""


def home(name, se):
    se.acquire()  # 拿到了一把钥匙
    print(f"{name}进入了房间")
    sleep(3)
    print(f'*****************{name}走出来房间')
    se.release()  # 还回了一把钥匙


if __name__ == '__main__':
    se = Semaphore(2)  # 创建信号量的对象，有两把钥匙
    for i in range(7):
        p = Thread(target=home, args=(f'tom{i}', se))
        p.start()

# -*- coding: utf-8 -*-
# 小伙伴们，围着吃火锅，当菜上齐了，请客的主人说：开吃！
# 于是小伙伴一起动筷子，这种场景如何实现
import threading
from threading import Thread, Event
from time import sleep

event = Event()


def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print(f'{name}已经启动')
    print(f'小伙伴{name}已经进入了就餐状态！')
    sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print(f'{name}收到了通知了.')
    print(f'小伙伴{name}开始吃咯！')


if __name__ == '__main__':
    # 创建新线程
    thread1 = threading.Thread(target=chihuoguo, args=("tom",))
    thread2 = threading.Thread(target=chihuoguo, args=('cherry',))
    # 开始线程
    thread1.start()
    thread2.start()

    # 发送事件通知
    print('--->>>主线程通知小伙伴开吃咯！')
    sleep(2)
    event.set()

# -*- coding: utf-8 -*-
from queue import Queue
from threading import Thread
from time import sleep

queue = Queue()


def producer():
    num = 1
    while True:
        if queue.qsize() < 5:
            print(f'生产：{num}号，大馒头')
            queue.put(f'大馒头:{num}号')
            num += 1
        else:
            print('馒头框满了，等待人来消费')
        sleep(1)


def consumer():
    while True:
        print(f'获取馒头：{queue.get()}')
        sleep(1)


if __name__ == '__main__':
    queue = Queue()
    t = Thread(target=producer)
    t.start()
    c = Thread(target=consumer)
    c.start()
    c2 = Thread(target=consumer)
    c2.start()

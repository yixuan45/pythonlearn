# -*- coding: utf-8 -*-
from threading import Thread, Lock
from time import sleep


class Account(object):
    def __init__(self, money, name):
        self.money = money
        self.name = name


class Drawing(Thread):
    def __init__(self, drawingNum, account):
        Thread.__init__(self)
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0

    def run(self):
        lock1.acquire()
        if self.account.money - self.drawingNum < 0:
            return
        sleep(1)
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        lock1.release()
        print(f"账户：{self.account.name},余额是：{self.account.money}")
        print(f"账户：{self.account.name},总共取了:{self.expenseTotal}")


if __name__ == '__main__':
    a1 = Account(100, 'laoyang')
    lock1 = Lock()  # 创建一个锁对象
    draw1 = Drawing(80, a1)
    draw2 = Drawing(80, a1)
    draw1.start()
    draw2.start()

# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep


class Account(object):
    def __init__(self, money, name):
        self.money = money
        self.name = name


class Drawing(Thread):
    def __init__(self, drawdingNum, account):
        Thread.__init__(self)
        self.drawingNum = drawdingNum
        self.account = account
        self.expenseTotal = 0

    def run(self):
        if self.account.money - self.drawingNum < 0:
            return
        sleep(1)
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        print(f"账户:{self.account.name},余额是:{self.account.money}")
        print(f"账户:{self.account.name},总共取了：{self.expenseTotal}")


if __name__ == '__main__':
    a1 = Account(100, "laoyang")
    draw1 = Drawing(80, a1)
    draw2 = Drawing(80, a1)
    draw1.start()
    draw2.start()

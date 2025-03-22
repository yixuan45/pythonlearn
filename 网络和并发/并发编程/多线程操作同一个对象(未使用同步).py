# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep


class Account(object):
    def __init__(self, money, name):
        self.money = money
        self.name = name


class Drawing(Thread):
    def __init__(self, drawingNum, account):
        """
        :param drawingNum:
        :param account:
        """
        Thread.__init__(self)
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0

    def run(self):
        if self.account.money - self.drawingNum < 0:
            return
        sleep(1)  # 判断完后阻塞。其他线程开始运行
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        print(f"账户:{self.account.name},余额是：{self.account.money}")
        print(f"账户:{self.account.name}，总共取了:{self.expenseTotal}")


if __name__ == '__main__':
    a1 = Account(100, "laoyang")
    draw1 = Drawing(80, a1)  # 定义取钱线程对象
    draw2 = Drawing(80, a1)  # 定义取钱线程对象
    draw1.start()
    draw2.start()

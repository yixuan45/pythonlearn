# -*- coding: utf-8 -*-
"""
一个实现四则运算的计算器
"""


class Calculator(object):
    def __init__(self):
        self.number = 0  # 默认number为0
        self.a = 0
        self.b = 0

    def __str__(self):
        return "这是一个实现四则运算的计算器"

    def add(self, a, b):
        """
        进行a+b进行加法计算
        :param a: 参数一
        :param b: 参数二
        :return: 两数之和
        """
        return a + b

    def minus(self, a, b):
        """
        实现a减去b
        :param a:被减数
        :param b: 减数
        :return: 两数之差
        """
        return a - b

    def main(self):
        """
        程序运行的主函数
        :return:
        """
        print("1.进行加法计算\n2.进行减法计算\n")
        self.number = int(input("请输入你选择的功能:"))
        self.a = float(input("请输入a的值"))
        self.b = float(input("请输入b的值"))
        if self.number == 1:
            print("两数之和为:\n", self.add(self.a, self.b))
        else:
            print("两数之差为:\n", self.minus(self.a, self.b))


if __name__ == '__main__':
    # 程序运行的入口
    # 测试用
    calculator = Calculator()  # 实例化对象
    print(calculator)
    calculator.main()

import time
import copy

# def printmax(a, b):
#     """
#     返回两个数的最大值
#     :param a: 一个参数
#     :param b: 一个参数
#     :return: 返回两个数的最大值
#     """
#     if (a > b):
#         print("较大值为{}".format(a))
#     else:
#         print("较大值为{}".format(b))
#
#
# help(printmax)  # 可以打印其文档
# # print(printmax.__doc__)

# a = 1000
#
#
# def test01():
#     start = time.time()
#     global a
#     for i in range(100000000):
#         a += 1
#     print("最终的值为{}".format(a))
#     end = time.time()
#     print("耗时{}".format(end - start))
#
#
# def test02():
#     start = time.time()
#     a = 1000
#     for i in range(100000000):
#         a += 1
#     print("最终的值为{}".format(a))
#     end = time.time()
#     print("耗时{}".format(end - start))


# def testCopy():
#     """测试浅拷贝"""
#     a = [10, 20, [5, 6]]
#     b = copy.copy(a)
#     print("a的值为{}".format(a))
#     print("b的值为{}".format(b))
#     """浅拷贝"""
#     b.append(30)
#     b[2].append(7)
#     print("浅拷贝后，修改b.....")
#     print("a的值为{}".format(a))
#     print("b的值为{}".format(b))
#
#
# def testDeepCopy():
#     """测试深拷贝"""
#     a = [10, 20, [5, 6]]
#     b=copy.deepcopy(a)
#     print("a的值为{}".format(a))
#     print("b的值为{}".format(b))
#     b.append(30)
#     b[2].append(7)
#     print("深拷贝后，修改b的值....")
#     print("a的值为{}".format(a))
#     print("b的值为{}".format(b))


# a = (10, 20, [5, 6])
# print("a", id(a))
#
#
# def test01(m):
#     print("m", id(m))
#     m[2][0] = 888
#     print("修改m后m的值为{}".format(m))
#     print("m", id(m))


# def f1(a, b, *c):
#     print(a, b, c)
#     print(c[1])

# def f2(a, b, **c):
#     print(a, b, c)

# sum_A = lambda a, b, c: a + b + c
# def f1():
#     print(1)
#
#
# def f2():
#     print(2)
#
#
# def f3():
#     print(3)

# list1=[lambda a:a*1,lambda b:b*2,lambda c:c*3]

# s = "print('abcde')"
# eval(s)
#
# a = 10
# b = 20
# c = eval("a+b")
# print(c)
#
# dict1 = dict(a=100, b=200)
# d=eval("a+b",dict1)
# print(d)

# def jiecheng(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jiecheng(n - 1)

s = "global"


def outer():
    s = "outer"

    def inner():
        s = "inner"
        print(s)

    inner()


if __name__ == '__main__':
    outer()

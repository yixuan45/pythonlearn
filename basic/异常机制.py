# # 测试简单的0不能做除数
# a = 3 / 0

# def a():
#     print("run in a() start!")
#     num = 1 / 0
#     print("run in a() end!")
#
#
# def b():
#     print("run in b() start!")
#     a()
#     print("run in b() end!")
#
#
# def c():
#     print("run in c() start!")
#     b()
#     print("run in c() end!")
#
#
# print("step1")
# c()
# print("step2")

# try:
#     print("step1")
#     a = 3 / 0
#     print("step2")
#
# except BaseException as e:
#     print("step3")
#     print(e)
# print("step4")
# print("step5")


# while True:
#     try:
#         x = int(input("请输入一个数字:"))
#         print("您输入的数字是：", x)
#         if x == 88:
#             print("退出程序")
#             break
#     except BaseException as e:
#         print("异常，输入的不是数字！")
#         print(e)


# try:
#     a=input("请输入被除数：")
#     b=input("请输入除数：")
#     c=float(a)/float(b)
#     print(c)
#
# except ZeroDivisionError:
#     print("异常：除数不能为0")
# except TypeError:
#     print("异常：除数和被除数都应该为数值类型")
# except BaseException as e:
#     print(e)
#     print(type(e))

# try:
#     a = input("请输入被除数：")
#     b = input("请输入除数：")
#     c = float(a) / float(b)
# except BaseException as e:
#     print(e)
# else:
#     print("除的结果是：", c)
# finally:
#     print("我是finally语句，无论是否发生异常，我都会被执行！！！")
# print("程序执行结束")

# try:
#     # f = open('a.txt', "r")
#     f = open("b.txt", 'r')
#     content = f.read()
#     print(content)
# except BaseException as e:
#     print(e)
#     print(type(e))
# finally:
#     print("关闭文件")
#     try:
#         f.close()
#     except BaseException as a:
#         if a.__str__()=="name 'f' is not defined":
#             print("a 没有被定义成功，不用关闭")
#
# print("继续执行其他代码")
# print("程序结束")

# int a =3
# print(a)

# print(a)

# a=3/0
# print(a)

# a=float("laogao")
# print(a)

# a=123+"abc"
# print(a)

# a=100
# a.sayhi()
# print(a)


# a = [4, 5, 6]
# a[10]
# print(a[10])

# a = {'name': "老高", 'age': 18}
# a['salary']
#
#
# with open("a.txt") as f:
#     # content=f.readline()
#     # print(content)
#     for line in f:
#         print(line, end='')

# import traceback
#
# try:
#     print("step1")
#     num = 1 / 0
# except:
#     with open("c.log", "a") as f:  # append
#         traceback.print_exc(file=f)
#         print("打印成功")


# # 自定义异常类
# class AgeError(Exception):
#     def __init__(self, errorInfo):
#         Exception.__init__(self)
#         self.errorInfo = errorInfo
#
#     def __str__(self):
#         return str(self.errorInfo) + ",年龄错误！应该在1-150之间"
#
#
# if __name__ == "__main__":
#     age = int(input("请输入一个年龄："))
#     if ((age < 1) or (age > 150)):
#         raise AgeError(age)
#     else:
#         print("正常的年龄：", age)

# def aa():
#     print("run in aa")
#     num1=3
#     num2=num1*4
#
# aa()


# def a():
#     print("start in a")
#     num = 10
#     b(num)
#     print("end in a,num is:" + str(num))
#
#
# def b(s):
#     s = 100
#     print("run in b,s is:" + str(s))
#
#
# a()

# f = open(r"a.txt", "a")  # r是把字符串中的所有字符全都转成路径
# f.write("Hello World!!")
# f.close()

# with open(r"a.txt", "r+") as f:
#     for i in range(0, 5):
#         f.write("老高{}！！\n".format(i))
#         f.seek(0)
#         for line in f:
#             print(line, end='')

# with open(r"a.txt", "w", encoding="utf-8") as f:
#     f.write("黄仕宇是傻逼")

# with open(r"a.txt", "w", encoding="utf-8") as f:
#     s = ["老高\n", "黄仕\n", "你好\n"]
#     f.writelines(s)

# try:
#     f = open(r"a.txt", "a")
#     s = "老高"
#     f.write(s)
# except BaseException as e:
#     print(e)
# finally:
#     f.close()

# with open(r"a.txt", "r", encoding="utf-8") as f:
#     print(f.read(4))  # 读取4个字符

# with open(r"a.txt", "r", encoding="gbk") as f:
#     for line in f:
#         print(line, end="")

# with open(r"a.txt", "r") as f:
#     lines = f.readlines()
#     # rstrip的作用就是去除右侧的空白符
#     lines2 = [line.rstrip() + "  #" + str(index) + "\n" for index, line in zip(range(1, len(lines) + 1), lines)]
#
# with open(r"a.txt", "w") as f:
#     f.writelines(lines2)

# with open('test.jpg', 'rb') as text1, open('ddd.jpg', "wb") as text2:
#     for line in text1:
#         text2.write(line)

# import pickle
#
# with open(r"data.dat", "wb") as f:
#     name = "老高"
#     age = 34
#     score = [90, 80, 60]
#     resume = {'name': name, 'age': age, 'score': score}
#     pickle.dump(resume, f)
#
# with open("data.dat", "rb") as f:
#     resume2 = pickle.load(f)
#     print(resume2)


# import os

# os.system("calc.exe") #调用计算机
# os.system("ping www.baidu.com")
# os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\腾讯软件\\QQ\\QQ.lnk")

# import os
#
# path = os.getcwd()
# list_files = os.walk(path, topdown=False)
#
# for root, dirs, files in list_files:
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))

# import shutil
#
# shutil.copyfile("a.txt", "a_copy.txt")


# import os
#
#
# def my_print_file(path, level):
#     child_files = os.listdir(path)
#     for file in child_files:
#         file_path = os.path.join(path, file)
#         print("\t" * level + file_path)
#         if os.path.isdir(file_path):
#             my_print_file(file_path, level + 1)
#
#
# my_print_file("relearn_new", 0)

# import math
# help(math)




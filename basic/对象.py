# class Student(object):
#     def __init__(self, name, score, *jineng):
#         self.name = name
#         self.score = score
#         self.skill = jineng
#
#     def say_score(self):
#         print("{}的分数为{}".format(self.name, self.score))
#
#     def attack(self, skill):
#         print("{}使用了{}技能".format(self.name, skill))
#
#     def main(self):
#         """
#         整个对象的主函数
#         :return:
#         """
#         oder = input("请输入你要使用的技能1.九阴白骨爪，2.六脉神剑")
#         if oder == 1:
#             self.attack(self.skill[0])
#         else:
#             self.attack(self.skill[1])
#
#
# if __name__ == '__main__':
#     student1 = Student("张三", 19, '九阴白骨爪', '六脉神剑')
#     # print(student1.skill[0])
#     Student.attack(student1, '九阴白骨爪')
#     student1.main()


# class Student(object):
#     company = "重庆交通大学"  # 类属性
#     count = 0  # 类属性
#
#     def __init__(self, name, score):
#         self.name = name  # 实例属性
#         self.score = score
#         Student.count = Student.count + 1
#
#     def say_score(self):  # 实例方法
#         print("我的公司是:", Student.company)
#         print(self.name, '的分数为：', self.score)
#
#
# if __name__ == '__main__':
#     s1 = Student('王总', 80)  # s1是实例对象，自动调用__init__()方法
#     s2 = Student('张三', 70)
#     s1.say_score()
#     print('一共创建了{}个Student对象'.format(Student.count))

# class Student(object):
#     company = "SXT"  # 类属性
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def printCompany(cls):
#         print("这个学生的company属性为:", cls.company)
#
#     @staticmethod
#     def add(a, b):
#         print("{}+{}={}".format(a, b, a + b))
#         return a + b
#
#
# if __name__ == '__main__':
#     sum = Student.add(10, 20)
#     print(sum)
#     student = Student('李阳')
#     student.add(10, 20)


# class Car(object):
#     def __init__(self, age, money):
#         self.money = money
#         self.age = age
#
#     def __call__(self, age, money):
#         print("call方法")
#         print("车龄{0}\n金额{1}".format(age, money))
#
#     def say_money(self):
#         print("常规方法")
#         print("车龄{0}\n金额{1}".format(self.age, self.money))
#
#
# if __name__ == '__main__':
#     car = Car(3, 200000)
#     car.say_money()
#     print()
#     car(3, 20000)

# # python中没有方法的重载。定义多个同名的方法，只有最后一个有效
# class Person(object):
#     name = '李阳'
#
#     def say_hi(self):
#         print("hello")
#
#     def say_hi(self):
#         print("{},hello".format(self.name))
#
#
# if __name__ == '__main__':
#     person = Person()
#     person.say_hi()

# class Person(object):
#     def work(self):
#         print("努力上班！")
#
#
# def play_game(self):
#     print("玩游戏")
#
#
# def work2(self):
#     print("好好工作，努力上班！")
#
#
# if __name__ == '__main__':
#     Person.play = play_game
#     Person.work = work2
#
#     person = Person()
#     person.play()
#     person.work()


# class Employee(object):
#     __company = "重庆"  # 解释器运行时，把__company转成了_Employee__company
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#         self.age = age
#
#     def say_company(self):
#         print("我的公司是:", Employee.__company)
#         print("我的年龄是：", self.__age)
#
#
#     def __work(self):
#         print("我的工作就是玩！")
#
#
# # print(dir(Employee))
# print(Employee._Employee__company)
# a = Employee("王总", 18)
# a.say_company()
# a._Employee__work()
# print("这是一个公共属性", a.age)
# print("这是一个私有属性", a._Employee__age)


# class Employee(object):
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#
# emp1 = Employee("王总", 30000)
# print(emp1._Employee__salary)
# emp1.salary=50000
# print(emp1.salary)

# import numpy as np
#
# # 生成10个标准正态分布（均值为0，标准差为1）的随机数
# noise = np.random.normal(0, 1, 1)
# print(noise)


# class Employee(object):
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     @property
#     def salary(self):
#         print("薪资是:", self.__salary)
#         return self.__salary
#
#     @salary.setter
#     def salary(self, salary):
#         if 0 < salary < 1000000:
#             self.__salary = salary
#         else:
#             print("薪资录入错误！只能在0-100000之间！")
#
#     @salary.deleter
#     def salary(self):
#         print("Deleting salary...")
#         del self.__salary
#
#
# if __name__ == '__main__':
#     emp1 = Employee('老高', 30000)
#     print(emp1.salary)
#     emp1.salary = 50000
#     print(emp1.salary)
#     del emp1.salary
#     print(emp1.salary)


# a = None
# if a is None and a == None:
#     print("a是None")  # 会执行
# if a==False or a==0:
#     print("None不等于False")

import turtle


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# def draw_sharingan_eye():
#     # 设置初始参数
#     turtle.speed(10)
#     turtle.bgcolor("black")
#
#     # 绘制黑色眼珠
#     draw_circle("black", 50, 0, -50)
#
#     # 绘制红色眼白
#     draw_circle("red", 70, 0, -70)
#
#     # 绘制中间的小白圈
#     draw_circle("white", 30, 0, -30)
#
#     # 绘制半透明的环
#     draw_circle("darkred", 65, 0, -65)
#
#     # 绘制写轮眼的“米”字
#     turtle.color("black")
#     turtle.pensize(5)
#     turtle.penup()
#     turtle.goto(0, -50)
#     turtle.pendown()
#     turtle.goto(0, 20)  # 竖线
#
#     turtle.penup()
#     turtle.goto(-30, -50)
#     turtle.pendown()
#     turtle.goto(30, 20)  # 左斜线
#
#     turtle.penup()
#     turtle.goto(30, -50)
#     turtle.pendown()
#     turtle.goto(-30, 20)  # 右斜线
#
#     turtle.penup()
#     turtle.goto(-30, -50)
#     turtle.pendown()
#     turtle.goto(30, -50)  # 下面的水平线
#
#     # 隐藏海龟
#     turtle.hideturtle()
#
#
# # 设置窗口大小和清晰度
# turtle.setup(width=600, height=600)
#
# # 调用绘制函数
# draw_sharingan_eye()
#
# # 完成绘制
# turtle.done()

# class Student:
#     pass
#
# class Car:#父类是object
#     pass
#
# class Benz(Car):
#     pass

# class Person(object):
#     def __init__(self, name, age):
#         print("创建Person")
#         self.name = name
#         self.__age = age
#
#     def say_age(self):
#         print("{0}的年龄为{1}岁".format(self.name, self.__age))
#
#
# class Student(Person):
#     def __init__(self, name, age, score):
#         # Person.__init__(self, name, age)
#         super(Student, self).__init__(name, age)
#         print("创建Student类")
#         self.score = score
#
#
# s1 = Student("老王", 18, 90)
# s1.say_age()

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_age(self):
#         print(self.name, "的年龄是：", self.age)
#
#     def say_name(self):
#         print("我是", self.name)
#
#
# class Student(Person):
#     def __init__(self, name, age, score):
#         Person.__init__(self, name, age)
#         self.score = score
#
#     def say_score(self):
#         print(self.name, "的分数是：", self.score)
#
#     def say_name(self):
#         print("报告老师，我是", self.name)#父类方法的重写
#
#
# s1 = Student("老高", 15, 85)
# s1.say_score()
# s1.say_name()
# s1.say_age()

# class A: pass
# class B(A): pass
# class C(B): pass
# print(C.mro())

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_age(self):
#         print(self.name, "的年龄是：", self.age)
#
#
# obj = object()
# print(dir(obj))
#
# s2 = Person("老高", 18)
# print(dir(s2))
# print(s2.say_age)
# print(type(s2.say_age))

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def __str__(self):
#         """
#         将对象转化成一个字符串描述，一般用于print方法
#         :return:
#         """
#         print("重写__str__方法")
#         return "名字是:{0},年龄是{1}".format(self.name, self.__age)
#
#
# p = Person("老高", 18)
# print(p)
# s = str(p)


# class A(object):
#     def aa(self):
#         print("这是A的方法")
#
#
# class B(object):
#     def bb(self):
#         print("这是B的方法")
#
#
# class C(B, A):
#     def cc(self):
#         print("这是C的方法")
#
#
# if __name__ == '__main__':
#     c = C()
#     c.cc()
#     c.bb()
#     c.aa()


# class A(object):
#     def aa(self):
#         print("aa")
#
#     def say(self):
#         print("say AAA!")
#
#
# class B(object):
#     def bb(self):
#         print("bb")
#
#     def say(self):
#         print("say BBB!")
#
#
# class C(B, A):
#     def cc(self):
#         print("cc")
#
#
# c = C()
# print(C.mro())  # 打印类的层次结构
# c.say()  # 解释器寻找方法是“从左到右”的方式寻找，此时会执行B类中的say()

# class A(object):
#     def __init__(self):
#         print("A的构造方法")
#
#     def say(self):
#         print("A:", self)
#         print("say AAA")
#
#
# class B(A):
#     def __init__(self):
#         super(B, self).__init__()#调用父类的构造方法
#         print("B的构造方法")
#
#     def say(self):
#         #A.say(self) 调用父类的say方法
#         super(B, self).say()#通过super()调用父类的方法
#         print("say BBB")
#
# b=B()
# b.say()

# class Animal(object):
#     def shout(self):
#         print("动物叫了一声")
#
#
# class Dog(Animal):
#     def shout(self):
#         print("小狗，汪汪")
#
#
# class Cat(Animal):
#     def shout(self):
#         print("小猫，喵喵喵")
#
#
# def animalShout(animal):
#     animal.shout()  # 会产生多态，传入的对象不同，则调用的方法也不一样
#
#
# animalShout(Dog())
# animalShout(Cat())


# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         if isinstance(other, Person):
#             return "{0}--{1}".format(self.name, other.name)
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return self.name * other
#         else:
#             return "不是同类对象，不能相乘"
#
#
# p1 = Person("老高")
# p2 = Person("胡图图")
# x = p1 + p2
# print(x)
# print(p1 * 3)

# import copy
#
#
# class MobilePhone(object):
#     def __init__(self, cpu):
#         self.cpu = cpu
#
#
# class CPU(object):
#     pass
#
#
# c = CPU()
# m = MobilePhone(c)

# print("浅拷贝")
# m2 = copy.copy(m)  # 浅拷贝，m2是m对象的一个浅拷贝对象
# print("m:", id(m))
# print("m2:", id(m2))
# print("m中的cpu:", id(m.cpu))
# print("m2中的cpu：", id(m2.cpu))

# print("深拷贝...")
# m3 = copy.deepcopy(m)  # 深拷贝
# print("m", id(m))
# print("m3", id(m3))
# print("m中的cpu", id(m.cpu))
# print("m3中的cpu", id(m3.cpu))


# class CPU(object):
#     def calculate(self):
#         print("正在计算，算个12345！")
#
#
# class Screen(object):
#     def show(self):
#         print("显示一个好看的画面，亮瞎你的钛合金眼")
#
#
# class MobilePhone(object):
#     def __init__(self, cpu, screen):
#         self.cpu = cpu
#         self.screen = screen
#
#
# c = CPU()
# s = Screen()
# m = MobilePhone(c, s)
# m.cpu.calculate()
# m.screen.show()


# class Benz(object):
#     pass
#
# class BMW(object):
#     pass
#
# class BYD(object):
#     pass
#
# class CarFactory(object):
#     def createCar(self, brand):
#         if brand == "奔驰":
#             return Benz()
#         elif brand == "宝马":
#             return BMW()
#         elif brand == "比亚迪":
#             return BYD()
#         else:
#             return "位置品牌，无法创建"
#
#
# factory = CarFactory()
# c1 = factory.createCar("奔驰")
# c2 = factory.createCar("宝马")
# print(c1)
# print(c2)

# class MySingleton(object):
#     __obj = None
#     __init_flag = True
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__obj == None:
#             cls.__obj = object.__new__(cls)
#         return cls.__obj
#
#     def __init__(self, name):
#         if MySingleton.__init_flag:
#             print("初始化第一个对象...")
#             self.name = name
#             MySingleton.__init_flag = False
#
#
# a = MySingleton("aa")
# print(a.name)
# b = MySingleton("bb")
# print(b.name)
# class Benz: pass
#
#
# class BMW: pass
#
#
# class BYD: pass
#
#
# class CarFactory(object):
#     __obj = None
#     __init_flag = True
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__obj == None:
#             cls.__obj = object.__new__(cls)
#
#         return cls.__obj
#
#     def __init__(self):
#         if CarFactory.__init_flag:
#             print("init.....")
#             CarFactory.__init_flag = False
#
#     def createCar(self, brand):
#         if brand == "奔驰":
#             return Benz()
#         elif brand == "宝马":
#             return BMW()
#         elif brand == "比亚迪":
#             return BYD()
#         else:
#             return "位置品牌，无法创建"
#
#
# factory = CarFactory()
# c1 = factory.createCar("奔驰")
# c2 = factory.createCar("宝马")
# print(c1)
# print(c2)
# factory2 = CarFactory()
# print(factory)
# print(factory2)

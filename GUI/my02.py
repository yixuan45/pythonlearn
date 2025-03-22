# -*- coding: utf-8 -*-
"""测试一个经典的GUI程序写法，使用面向对象的方式"""
from tkinter import *


class Application(Frame):
    """
    测试labels标签
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()  # 创建的框架

    def createWidget(self):
        self.label01 = Label(self, text="老高", width=10, height=2, bg="black", fg="white")
        # self.label01["text"]="cccc" # 通过__setitem__方法进行了重新定义参数
        # self.label01.config(fg="red", bg="green") ,本质上也是通过键值对的方式进行将参数的融合
        self.label01.pack()

        self.label02 = Label(self, text="老杨", width=10, height=2, bg="blue", fg="white", font=("黑体", 30))
        self.label02.pack()

        # 显示图像
        # global photo  # 把photo声明成全局变量，如果是局部变量，不然本方法执行后，图像对象销毁
        self.photo = PhotoImage(file="img/3.gif")
        self.label03 = Label(self, image=self.photo)
        self.label03.pack()

        self.label04 = Label(self, text="你好！\n我是一名初学者\n正在学习python编程",
                             borderwidth=1, relief="solid", justify="right")
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x500+200+200")
    app = Application(master=root)
    root.mainloop()

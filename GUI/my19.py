# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.a

    def createWidget(self):
        """创建框架"""
        s1 = Scale(self, from_=10, to=50, length=200, tickinterval=5, orient=HORIZONTAL,
                   command=self.test1)  # 默认是竖直的，HORIZONTAL是水平的,这里调用test的时候，会默认将value的值传入函数中
        s1.pack()
        self.a = Label(self, text="yyx", width=10, height=1, bg="white", fg="red")
        self.a.pack()

    def test1(self, value):
        print("滑块的值：", value)
        newFont = ("宋体", value)
        self.a.config(font=newFont)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("yyx的系统")
    app = Application(root)
    root.mainloop()

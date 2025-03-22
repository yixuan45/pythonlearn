# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """
    一个Button的学习方法
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.photo = PhotoImage(file="img/3.gif")
        self.label01 = Label(self, image=self.photo)
        self.label01.pack()

        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()

        self.btn02 = Button(self, image=self.photo, command=self.login)
        self.btn02.pack()

    def login(self):
        """登录方法"""
        messagebox.showinfo("欢迎来学习", "登录成功，请开始学习")


if __name__ == '__main__':
    root = Tk()
    root.geometry("700x600+300+200")
    app = Application(root)
    root.mainloop()

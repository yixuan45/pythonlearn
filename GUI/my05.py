# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgt()

    def createWidgt(self):
        """创建登录界面的组件"""
        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        # StringVar变量绑定到指定的组件。
        # StringVar变量的值发生变化，组件内容也变化。
        # 组件内容发生变化，StringVar变量的值也发生变化。
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get())
        print(self.entry01.get())

        # 创建密码框
        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="******")
        self.entry02.pack()

        # 登录按钮
        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        print("用户名:" + username)
        print("密 码 :" + pwd)
        messagebox.showinfo("老杨系统", "恭喜登录成功")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+200+100")
    root.title("entry文本")
    app = Application(root)
    root.mainloop()

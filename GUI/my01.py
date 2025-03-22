# -*- coding: utf-8 -*-
"""测试一个经典的GUI程序写法，使用面向对象的方式"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """
    一个经典的GUI程序的类的写法
    """

    def __init__(self, master=None):
        super().__init__(master)  # super()代表的是父类的定义，而不是父类对象
        self.master = master  # 传入root作为继承
        self.pack()  # 是用来将一个组件（如按钮、标签、框架等）添加到其父容器中的一种布局管理方法。

        self.createWiget()  # 调用创建组件方法

    def createWiget(self):
        """创建组件"""
        self.btn01 = Button(self.master)
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        # 创建一个退出按钮
        self.btnQuit = Button(self.master, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你99多玫瑰花")


if __name__ == '__main__':
    """Application 类实例化时，将 master 参数设为 root，这意味着 Application 的所有组件（在 Frame 中创建）都将在 root 主窗口中显示。"""
    root = Tk()  # 创建一个Tk对象
    root.geometry("400x100+200+300")  # 设置Tk的窗口大小和范围
    root.title("一个经典的GUI程序类的测试")  # 设置Tk的的名字
    app = Application(master=root)  # 实例化一个Application对象
    root.mainloop()  # 它的作用是启动 Tkinter 事件循环，让你的应用程序开始运行并等待用户的操作

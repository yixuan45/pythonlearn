# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        # a1 = showinfo(title="yyx系统", message="yyx大牛")
        # a2 = askokcancel(title="yyx系统", message="你是不是gay")
        # a3 = askquestion(title="yyx系统", message="你是不是傻逼")
        # a4 = showerror(title="yyx系统", message="报错了")
        # a5 = showwarning(title="yyx系统", message="无法进行这样的操作")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("yyx的系统")
    app = Application(root)
    root.mainloop()

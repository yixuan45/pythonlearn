# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        Button(self, text="选择背景色", command=self.test1).pack()

    def test1(self):
        s1 = colorchooser.askcolor(color="white", title="选择背景色")
        print(s1)
        self.master.config(bg=s1[1])


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("yyx的系统")
    app = Application(root)
    root.mainloop()

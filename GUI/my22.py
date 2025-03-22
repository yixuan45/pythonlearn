# -*- coding: utf-8 -*-
from tkinter.simpledialog import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.createWidget()

    def createWidget(self):
        """用于创建组件"""
        Button(self, text="老杨你多大了？请输入", command=self.test1).pack()
        self.show = Label(self, width=40, height=3, bg="green")
        self.show.pack()

    def test1(self):
        a = askinteger(title="输入年龄", prompt="请输入年龄", initialvalue=18, minvalue=1, maxvalue=150)
        self.show["text"] = a


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("yyx的系统")
    app = Application(root)
    root.mainloop()

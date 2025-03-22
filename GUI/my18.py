# -*- coding: utf-8 -*-
# from tkinter import *
#
# root = Tk()
# root.geometry("200x100")
# v = StringVar(root)
# v.set("彭于晏")
# om = OptionMenu(root, v, "彭于晏", "刘亦菲", "yyx")
#
# om["width"] = 10
# om.pack()
#
#
# def test1():
#     print("最爱的人：", v.get())
#
#
# Button(root, text="确定", command=test1).pack()
#
# root.mainloop()


from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        Label(self, text="最爱的人是谁：").grid(row=0, column=0)
        v = StringVar(self)
        v.set("彭于晏")
        om = OptionMenu(self, v, "彭于晏", "刘亦菲", "yyx")
        om["width"] = 10
        om.grid(row=0, column=1)
        Btn1 = Button(self, text="确定", command=lambda: self.test1(v))
        Btn1.grid(row=1, column=1)

    def test1(self, v):
        print("最爱的人：", v.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x100")
    root.title("最爱的明星")
    app = Application(root)
    root.mainloop()

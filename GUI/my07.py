# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.v = StringVar()
        self.v.set("女")

        self.election1 = Radiobutton(self, text="男", value="男", variable=self.v)
        self.election2 = Radiobutton(self, text="女", value="女", variable=self.v)

        self.election1.pack(side="left")
        self.election2.pack(side="left")
        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        messagebox.showinfo("测试", "选择的性别:" + self.v.get())


if __name__ == '__main__':
    root = Tk()
    root.title("老杨的系统")
    root.geometry("300x100+200+100")
    app = Application(root)
    root.mainloop()

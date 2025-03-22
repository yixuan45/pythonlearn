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
        self.codeHobby = IntVar()
        self.videoHobby = IntVar()

        print(self.codeHobby.get())  # 默认值是0
        self.c1 = Checkbutton(self, text="敲代码", variable=self.codeHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text="看视频", variable=self.videoHobby, onvalue=1, offvalue=0)
        self.c1.pack(side="left")
        self.c2.pack(side="left")
        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        if self.videoHobby.get() == 1:
            messagebox.showinfo("老杨的系统", "我也喜欢看视频")
        if self.codeHobby.get() == 1:
            messagebox.showinfo("老杨的系统", "我也喜欢敲代码")


if __name__ == '__main__':
    root = Tk()
    root.title("老杨的系统")
    root.geometry("400x300+200+100")
    app = Application(root)
    root.mainloop()

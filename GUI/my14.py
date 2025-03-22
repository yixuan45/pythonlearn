# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """通过place布局管理器实现扑克牌位置控制"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.yabs = 100
        self.createWidget()


    def createWidget(self):
        """创建控制组件"""
        # self.photo = PhotoImage(file="img/puke/1.gif")
        # self.puke1 = Label(self.master, image=self.photo)
        # self.puke1.place(x=10, y=50)
        self.photos = [PhotoImage(file="img/puke/" + str(i + 1) + ".gif") for i in range(6)]
        self.pukes = [Label(self.master, image=self.photos[i]) for i in range(6)]
        for i in range(6):
            self.pukes[i].place(x=10 + i * 120, y=self.yabs)

        # 为所有的Label增加事件处理
        for i in range(6):
            self.pukes[i].bind_class("Label", "<Button-1>", self.chupai)

    def chupai(self, event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())
        if event.widget.winfo_y() == self.yabs:
            event.widget.place(y=self.yabs - 50)
        else:
            event.widget.place(y=self.yabs)


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x400+300+200")
    root.title("扑克牌玩具")
    app = Application(root)
    root.mainloop()

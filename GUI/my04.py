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
        """框架方法"""
        self.butn1 = Button(self.master, text="begin",
                            width=6, height=3, anchor=E, command=self.songhua)  # anchor的作用就是决定你的text文本唯一按钮的那个位置
        self.butn1.pack()

        # 插入图片
        self.photo = PhotoImage(file="img/1.gif")
        self.butn2 = Button(self.master, image=self.photo, command=self.login)
        self.butn2.pack()
        self.butn2.config(state=DISABLED)  # 加入state会让你不能点击，就让你取消点击状态

    def songhua(self):
        """点击开始送花"""
        messagebox.showinfo("恭喜你", "得到两朵玫瑰花")

    def login(self):
        messagebox.showinfo("系统", "登录成功！欢迎开始学习！")


if __name__ == '__main__':
    root = Tk()
    root.title("button练习")
    root.geometry("400x300+200+100")
    app = Application(root)
    root.mainloop()

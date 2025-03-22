# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.canvas = Canvas(self, width=400, height=500, bg="green")
        self.canvas.pack()
        # 画一条直线
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个椭圆，坐标两双。为椭圆的边界矩形左上角和底部右下角
        oval = self.canvas.create_oval(50, 50, 100, 100)  # 画圆是在它所在的外切矩形的左边点

        global photo
        photo = PhotoImage(file="img/3.gif")
        self.canvas.create_image(200, 300, image=photo)

        Button(self, text="画10个矩阵", command=self.draw50Recg).pack(side="left")

    def draw50Recg(self):
        for i in range(0, 10):
            x1 = random.randrange(int(self.canvas["width"]) / 2)  # 生成一个从0到这个数中的其中一个数
            y1 = random.randrange(int(self.canvas["height"]) / 2)
            x2 = x1 + random.randrange(int(self.canvas["width"]) / 2)
            y2 = y1 + random.randrange(int(self.canvas["height"]) / 2)
            self.canvas.create_rectangle(x1, y1, x2, y2)


if __name__ == '__main__':
    root = Tk()
    root.title("老杨的系统")
    root.geometry("400x600+200+100")
    app = Application(root)
    root.mainloop()

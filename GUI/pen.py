# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None, win_width=900, win_height=450):
        super().__init__(master)
        self.pack()
        self.master = master
        self.x = 0
        self.y = 0
        self.bgcolor = "#000000"
        self.fgcolor = "#ff0000"
        self.lastDraw = 0  # 表示最后绘制的图形
        self.startDrawFlag = False

        # 创建元素参数区域
        self.canvasPad = None
        self.win_width = win_width
        self.win_height = win_height

        self.createWidget()

    def createWidget(self):
        """创建控件"""
        # 创建绘图区
        self.canvasPad = Canvas(self.master, width=self.win_width, height=self.win_height * 0.9, bg=self.bgcolor)
        self.canvasPad.pack(fill=tkinter.BOTH, expand=True)

        # 创建功能按钮
        btn_start = Button(self.master, text="开始", name="start")
        btn_start.pack(side="left", padx="10")
        btn_pen = Button(self.master, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")
        btn_rect = Button(self.master, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")
        btn_clear = Button(self.master, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")
        btn_eraser = Button(self.master, text="橡皮擦", name="eraser")
        btn_eraser.pack(side="left", padx="10")
        btn_line = Button(self.master, text="直线", name="line")
        btn_line.pack(side="left", padx="10")
        btn_lineArrow = Button(self.master, text="箭头直线", name="lineArrow")
        btn_lineArrow.pack(side="left", padx="10")
        btn_color = Button(self.master, text="颜色", name="color")
        btn_color.pack(side="left", padx="10")

        # 时间处理
        self.canvasPad.bind_class("Button", "<1>", self.eventManger)
        self.canvasPad.bind("<ButtonRelease-1>", self.stopDraw)

        """绑定快捷键区域"""
        # 绑定窗口变化
        self.master.bind("<Configure>", self.resize_canvas)

    def test(self):
        """用于测试专用"""
        pass

    def eventManger(self, event):
        """整个事件管理"""
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.canvasPad.bind("<B1-Motion>", self.myline)
        elif name == "lineArrow":
            self.canvasPad.bind("<B1-Motion>", self.mylineArrow)
        elif name == "rect":
            self.canvasPad.bind("<B1-Motion>", self.myRect)
        elif name == "pen":
            self.canvasPad.bind("<B1-Motion>", self.myPen)
        elif name == "eraser":
            self.canvasPad.bind("<B1-Motion>", self.myEraser)

    def startDraw(self, event):
        self.canvasPad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def stopDraw(self, evnet):
        self.startDrawFlag = False
        self.lastDraw = 0

    def myline(self, event):
        """创建直线"""
        self.startDraw(event)
        self.lastDraw = self.canvasPad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

    def mylineArrow(self, event):
        """绘制箭头直线"""
        self.startDraw(event)
        self.lastDraw = self.canvasPad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.canvasPad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def myPen(self, event):
        self.startDraw(event)
        self.canvasPad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    def myEraser(self, event):
        self.startDraw(event)
        self.canvasPad.create_rectangle(event.x - 6, event.y - 6, event.x + 6, event.y + 6,
                                                        fill=self.bgcolor)
        self.x = event.x
        self.y = event.y

    def resize_canvas(self, event):
        """canvas的窗口跟随root的窗口变化"""
        self.canvasPad.config(width=event.width, height=event.height * 0.9)


if __name__ == '__main__':
    win_width = 900
    win_height = 450
    root = Tk()
    root.geometry("600x500")
    root.title("yyx的画图软件")
    app = Application(root, win_width=win_width, win_height=win_height)
    root.mainloop()

# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


class Application(Frame):  # 制作一个简易的计算器
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.createWidget()

    def createWidget(self):
        """通过grid布局实现计算器的界面"""
        # 按钮
        binText = (("MC", "M+", "M-", "MR"),
                   ("C", "±", "÷", "x"),
                   (7, 8, 9, "-"),
                   (4, 5, 6, "+"),
                   (1, 2, 3, "="),
                   (0, "."))

        # 输入框
        self.v1 = StringVar()
        self.entry01 = Entry(self, textvariable=self.v1)
        self.entry01.grid(row=0, column=0, columnspan=4, pady=10)  # pady=10 意味着在 entry01 的顶部和底部各添加 10 像素的空间。
        for rindex, rText in enumerate(binText):
            for cindex, cvalue in enumerate(rText):
                if cvalue == "=":
                    Button(self, text=cvalue, width=2, command=self.mainCaculate()).grid(row=rindex + 1, column=cindex,
                                                                                         rowspan=2, sticky=NSEW)
                elif cvalue == 0:
                    Button(self, text=cvalue, width=2).grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
                elif cvalue == ".":
                    Button(self, text=cvalue, width=2).grid(row=rindex + 1, column=cindex + 1, sticky=NSEW)
                else:
                    Button(self, text=cvalue, width=4).grid(row=rindex + 1, column=cindex, sticky=NSEW)
                    # sticky=NSEW，意味着按钮会填充整个单元格

    def mainCaculate(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.title("简易计算器")
    root.geometry("250x250+200+100")
    app = Application(root)
    root.mainloop()

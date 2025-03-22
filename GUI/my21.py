# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.createWidget()

    def createWidget(self):
        """用于创建组件"""
        Button(self, text="选择编辑的视频文件", command=self.test1).pack()
        self.show = Label(self, width=40, height=3, bg="green")
        self.show.pack()

    def test1(self):
        f = filedialog.askopenfilename(title="上传文件", initialdir="d:", filetypes=[("视频文件", "mp4")])
        self.show["text"] = f


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("yyx的程序")
    app = Application(root)
    root.mainloop()

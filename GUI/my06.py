# -*- coding: utf-8 -*-
import webbrowser
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建框架"""
        self.w1 = Text(self.master, width=40, height=12, bg="gray")  # 注意这里的self.master可以是root，但是不能是self
        # 宽度20个字母（10个汉字），高度一个行高
        self.w1.pack()

        self.w1.insert(1.0, "0123456789\nabcdefg")  # 这里的1.0的意思是第一行第0列
        self.w1.insert(2.3, "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦\n ")

        Button(self, text="重复插入文本", command=self.insertText).pack(side="left")
        Button(self, text="返回文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="通过tag精准控制文本", command=self.testTag).pack(side="left")

    def insertText(self):
        # INSERT索引表示在光标出插入
        self.w1.insert(INSERT, "老杨")
        # END索引号表示在最后插入
        self.w1.insert(END, "你好，我是你大哥")

    def returnText(self):
        # indexes(索引)是用来纸箱Text组件中文本的位置，
        # Text的组件索引也是对应实际字符之间的位置
        # 核心：行号以1开始，列好以0开始
        print(self.w1.get(1.2, 1.6))
        self.w1.insert(1.8, "老杨")
        print("所有文本内容为：\n" + self.w1.get(1.0, END))

    def addImage(self):
        """在光标位置插入图片"""
        global photo
        photo = PhotoImage(file="img/3.gif")
        self.w1.image_create(END, image=photo)  # 在文章的末尾插入
        self.w1.image_create(INSERT, image=photo)  # 在鼠标的光标出插入图片

    def addWidget(self):
        """增加新的控件方法"""
        b1 = Button(self.w1, text="爱你老杨", command=self.songhua)
        # 在text创建组件的命令
        self.w1.window_create(INSERT, window=b1)

    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "good good study ,day day up!\n老杨，老杨\n我爱你\n就像老鼠爱大米\n百度")
        self.w1.tag_add("good", 1.0, 1.9)  # 第一个参数为标记名称，第二个参数和第三个参数是索引的位置
        self.w1.tag_config("good", background="yellow", foreground="red")  # 第一个参数是需要添加配置的标记，第二和第三个参数的含义是添加前景色和背景色

        self.w1.tag_add("baidu", 5.0, 5.2)
        self.w1.tag_config("baidu", underline=True)
        self.w1.tag_bind("baidu", "<Button-1>", self.webshow)

    def webshow(self, event):
        webbrowser.open("http://www.baidu.com")

    def songhua(self):
        """送花"""
        messagebox.showinfo("老杨系统", "送你9999朵玫瑰花")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+200+100")
    root.title("老杨系统")
    app = Application(root)
    root.mainloop()

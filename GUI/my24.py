# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.textpad = None

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        # 创建主菜单栏
        menubar = Menu(self)

        # 创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将子菜单加入到主菜单栏
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮组(H)", menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.test)
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.test)
        menuFile.add_command(label="保存", accelerator="ctrl+s", command=self.test)
        menuFile.add_separator()  # 添加分割线
        menuFile.add_command(label="退出", accelerator="ctrl+q", command=self.test)

        # 将主菜单栏加到根窗口
        self.master["menu"] = menubar

        # 文本编辑区
        self.textpad = Text(self, width=50, height=30)
        self.textpad.pack()

        # 创建上下菜单
        self.contentMenu = Menu(self.master)
        self.contentMenu.add_command(label="背景颜色", command=self.test)

        # 为右键绑定事件
        self.master.bind("<Button-3>", self.createContextMenu)

    def test(self):
        """用于测试"""
        pass

    def createContextMenu(self, event):
        """菜单在鼠标右键单击的坐标处显示"""
        self.contentMenu.post(event.x_root, event.y_root)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("yyx的记事本系统")
    app = Application(root)
    root.mainloop()

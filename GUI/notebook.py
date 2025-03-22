# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.colorchooser import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master

        # 对象参数
        self.textpad = None  # 初始化文本编辑区对象
        self.filename = None

        self.createWidget()

    def createWidget(self):
        """用于创建模块"""
        # 创建主菜单栏
        menubar = Menu(root)  # 创建一个主菜单对象

        # 创建子菜单
        menuFile = Menu(menubar)  # 将menuFile对象放在Menu中
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将子菜单加入到主菜单栏中
        menubar.add_cascade(label="文件(F)", menu=menuFile)  # 文件放到menuFile中
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.newFile)
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.openFile)
        menuFile.add_command(label="保存", accelerator="ctrl+s", command=self.saveFile)
        menuFile.add_separator()  # 添加分割线
        menuFile.add_command(label="退出", accelerator="ctrl+q", command=self.test)

        # 将主菜单栏加到根窗口
        self.master["menu"] = menubar

        # 文本编辑区
        self.textpad = Text(root)
        self.textpad.pack()

        # 创建上下菜单
        self.contentMenu = Menu(root)
        self.contentMenu.add_command(label="背景颜色", command=self.openAskColor)

        # 为右键绑定事件
        self.master.bind("<Button-3>", self.createContextMenu)

        # 绑定窗口变化事件
        root.bind('<Configure>', self.on_resize)

    def test(self):
        """用于测试专用"""
        pass

    def createContextMenu(self, event):
        """菜单在鼠标右键单击的坐标处显示"""
        self.contentMenu.post(event.x_root, event.y_root)

    def openFile(self):
        if self.textpad.get("1.0", "end") != "\n":
            if messagebox.askquestion("yyx的记事本", "请问是否要保存当前文本数据") == "yes":
                self.saveFile()
            else:
                self.textpad.delete("1.0", "end")
        try:
            with askopenfile(title="打开文本文件") as f:
                self.textpad.insert(INSERT, f.read())
                self.filename = f.name
                # print(self.filename)
        except:
            messagebox.showinfo("yyx的记事本", "未打开文件，请重试")

    def saveFile(self):
        if self.filename == None:
            # 说明未选择要存取的的文件
            messagebox.showinfo("yyx的记事本", "请选择你要存储的文件")
            try:
                with askopenfile(title="打开你要存储的文本文件") as f:
                    self.filename = f.name
            except:
                messagebox.showinfo("yyx的记事本", "未保存成功，请重试")
        else:
            # 如果当前文件板中存在数据，但是想存入新的文件
            if messagebox.askquestion("yyx的记事本", "请问要把当前的文本数据存入其他文件中吗") == "yes":
                try:
                    with askopenfile(title="打开你要存储的文本文件") as f:
                        self.filename = f.name
                    self.filename = None
                except:
                    messagebox.showinfo("yyx的记事本", "未保存成功,请重试")
            else:
                with open(self.filename, "w") as f:
                    c = self.textpad.get(1.0, END)
                    f.write(c)
                self.filename = None  # 再进行写入过后要将filename令为None值

    def newFile(self):
        """创建一个新的文件"""
        self.filename = asksaveasfilename(title="另存为", initialfile="未命名.txt", filetype=[("文本文档", "*.txt")],
                                          defaultextension=".txt")
        self.saveFile()

    def openAskColor(self):
        """打开背景颜色框"""
        s1 = askcolor(color="red", title="选择背景色")
        self.textpad.config(bg=s1[1])

    def on_resize(self, event):
        """textpad的窗口跟随root的窗口变化"""
        self.textpad.config(width=event.width, height=event.height)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("yyx的记事本")
    app = Application(root)
    root.mainloop()

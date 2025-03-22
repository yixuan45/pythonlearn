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
        # 用户名
        self.label01 = Label(self, text="用户名")
        self.label01.grid(row=0, column=0)
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1)
        v1.set("12346578")
        print(self.entry01.get())
        self.label02 = Label(self, text="用户名为手机号")
        self.label02.grid(row=0, column=2)

        # 密码
        self.label03 = Label(self, text="密码")
        self.label03.grid(row=1, column=0)
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.grid(row=1, column=1)

        # 登录
        Button(self, text="登录", command=lambda: self.login(self.entry01.get(), self.entry02.get())).grid(row=2,
                                                                                                         column=1,
                                                                                                         sticky="EW")
        Button(self, text="取消", command=self.quxiao).grid(row=2, column=2, sticky="EW")

    def login(self, admin, key):
        """
        用于登录
        :param admin:用户名
        :param key: 密码
        :return:
        """
        if admin == "17729686779" and key == "123456":
            messagebox.showinfo("老杨的系统", "密码正确")
        else:
            messagebox.showinfo("老杨的系统", "密码错误")

    def quxiao(self):
        """取消登录"""
        self.entry01.delete(0, END)
        self.entry01.insert(0, "123456")
        self.entry02.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    root.title("老杨的系统")
    root.geometry("400x300+200+100")
    app = Application(root)
    root.mainloop()

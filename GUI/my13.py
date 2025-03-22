# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("布局管理place")
root["bg"] = "white"
f1 = Frame(root, width=200, height=200, bg="green")
f1.place(x=30, y=20)
Button(root, text="老杨").place(relx=0.5, x=100, y=20, relwidth=0.2, relheight=0.5)
# 如果relx和x同时存在的话，就是先定位relx的位置，然后再定位x的位置，就是定位了relx的位置后，向两边移x
Button(f1, text="老杨爱睡觉").place(relx=0.6, rely=0.7)
Button(f1, text="老杨大哥").place(relx=0.5, rely=0.2)

root.mainloop()

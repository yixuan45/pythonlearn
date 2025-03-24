# -*- coding: utf-8 -*-
from socket import *

s = socket(AF_INET, SOCK_DGRAM)  # 创建套接字
addr = ('127.0.0.1', 8877)  # 准备接收方地址
data = input("请输入：")
# 发送数据时，python3需要将字符串转成byte
s.sendto(data.encode('gbk'), addr)  # 默认的网络助手使用的编码是gbk,sendto的第一个参数为要发送的数据，第二个参数为要发送参数的地址
s.close()

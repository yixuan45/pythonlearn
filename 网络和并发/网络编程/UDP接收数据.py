# -*- coding: utf-8 -*-
from socket import *

s = socket(AF_INET, SOCK_DGRAM)  # 创建一个无连接的套接字
# 绑定接受信息端口
s.bind(('127.0.0.1', 8877))  # 绑定一个端口，ip地址和端口号
print("等待接收数据！")
redata = s.recvfrom(1024)  # 1024表示本次接收的最大字节数
print(redata)
print(f'收到远程信息：{redata[0].decode("gbk")},from{redata[1]}')
s.close()

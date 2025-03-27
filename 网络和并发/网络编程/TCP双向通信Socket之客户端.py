# -*- coding: utf-8 -*-
'''
双向通信Socket之客户端
将控制台输入的信息发送给服务端
读取服务端的数据，将内容输出到控制台
'''

from socket import *

# 创建客户端Socket对象
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
# 连接服务器
tcp_client_socket.connect(('127.0.0.1', 8877))
while True:
    msg = input('>')
    # 想服务器发送信息
    tcp_client_socket.send(msg.encode('gbk'))
    if msg == 'end':
        break
    # 接受服务端数据
    re_data = tcp_client_socket.recv(1024)
    print('服务端说：', re_data.decode('gbk'))
tcp_client_socket.close()

# -*- coding: utf-8 -*-
"""
双向通信Socket之服务端读取客户端发送的数据，将内容输出到控制台将控制台输入的消息发送给客户端
"""
from socket import *

tcp_server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定端口
tcp_server_socket.bind(('127.0.0.1', 8877))
# 监听客服端的连接
tcp_server_socket.listen()
print("服务端已经启动，等待客户端链接")
# 接受客户端链接
tcp_client_socket, host = tcp_server_socket.accept()
print("一个客户端建立连接成功！")
while True:
    # 读取客户端的消息
    re_data = tcp_client_socket.recv(1024).decode('gbk')
    # 将消息输出到控制台
    print('客户端说：', re_data)
    if re_data == 'end':
        break
    # 获取控制台消息
    msg = input('>')
    tcp_client_socket.send(msg.encode('gbk'))
tcp_client_socket.close()
tcp_server_socket.close()

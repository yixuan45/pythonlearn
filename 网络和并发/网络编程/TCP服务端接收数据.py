# -*- coding: utf-8 -*-
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8899))
server_socket.listen(5)
client_socket, client_info = server_socket.accept()
# clientsocket 表示这个新的客户端
# clientInfo 表示这个信的客户端的ip以及port
recv_data = client_socket.recv(1024)
print('client_socket:', client_socket)
print('client_info:', client_info)
print(f"收到消息：{recv_data.decode('gbk')},来自{client_info}")
client_socket.close()
server_socket.close()
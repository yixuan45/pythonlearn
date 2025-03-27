# -*- coding: utf-8 -*-
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8899))
# 注意
# 1.tcp客户端已经连接号了服务器，所以在以后的数据发送中，不需要填写对方的ip和port--->打电话，区别于udp。
# 2.udp在发送数据的时候，因为没有之前的连接，所以需要再每次的发送中，都要填写接收方的ip和port--->写信
client_socket.send("haha".encode("gbk"))
client_socket.close()

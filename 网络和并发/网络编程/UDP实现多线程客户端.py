# -*- coding: utf-8 -*-
from socket import *
from threading import Thread

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('127.0.0.1', 8080))


# 不停的接收
def recv_data():
    while True:
        redata = udp_socket.recvfrom(1024)
        print(f'收到消息{redata[0].decode("gbk")},from{redata[1]}')


# 不停发送
def send_data():
    while True:
        data = input('请输入消息：')
        addr = ('127.0.0.1', 8989)
        udp_socket.sendto(data.encode('gbk'), addr)


if __name__ == '__main__':
    #创建两个线程
    t1=Thread(target=send_data)
    t2=Thread(target=recv_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

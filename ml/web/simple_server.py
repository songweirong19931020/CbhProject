# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: simple_server.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/24 9:55
# ---
import socket

server = socket.socket()
ip_port = ('127.0.0.1',8082)
server.bind(ip_port)
server.listen()


while 1 :
    conn,addr = server.accept()

    from_client_msg = conn.recv(1024)
    print(from_client_msg.decode('utf-8'))
    conn.send(b'http/1.1 200 ok\r\n\r\n')
    # conn.send(b'hello girl')
    with open('04test.html','rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

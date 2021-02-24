# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: server.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/22 16:04
# ---
from gevent import monkey
monkey.patch_all() #GEVENT如何检查是否能规避某个模块的io操作，在patch_all之前和之后分别打印一次，如果不一致，就说明能够规避
import socket
import gevent

def func(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        MSG = msg.upper()
        conn.send(MSG.encode('utf-8'))



sk = socket.socket() #TCP协议
sk.bind(('127.0.0.1',65000))
sk.listen() #开始监听

while True:
    conn,_ = sk.accept() #接受请求
    gevent.spawn(func,conn)
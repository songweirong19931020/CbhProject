# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: client.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/22 16:04
# ---
import socket
import gevent
import time
sk = socket.socket()

sk.connect(('127.0.0.1',65000))

while True:
    sk.send(b'hello')
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.5)
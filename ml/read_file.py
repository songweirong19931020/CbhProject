# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: read_file.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/11 11:19
# ---
#500G
def myreadlines(f,newline):
    buf = "" #放缓存
    while True:
        while newline in buf:#处理字符串过长重复读问题
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4956*10)
        if not chunk:
            #边缘条件判断---是否已经读到文件结尾
            yield buf
            break
        buf += chunk
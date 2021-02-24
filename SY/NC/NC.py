# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: NC.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/28 10:59
# ---
import pyautogui as pag
import time


import os
import time
import pyautogui as pag
try:
 while True:
  print("Press Ctrl-C to end")
  screenWidth, screenHeight = pag.size() #获取屏幕的尺寸
  print(screenWidth,screenHeight)
  x,y = pag.position() #获取当前鼠标的位置
  posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
  print(posStr)
  time.sleep(0.2)
  os.system('cls') #清楚屏幕
except KeyboardInterrupt:
 print('end....')


def update_levelcode(y_ix,num_index):
    time.sleep(3)
    pag.doubleClick(1114,y_ix)#进入
    time.sleep(2)
    pag.doubleClick(680,267)
    time.sleep(2)
    pag.click(1264,475)#删除
    time.sleep(2)
    pag.click(937,560)#确定删除
    time.sleep(2)
    pag.click(971,411)
    time.sleep(1)
    pag.hotkey('ctrl', 'a')
    time.sleep(1)
    pag.press('delete')  # 清空所有内容
    time.sleep(1)
    pag.typewrite('A')
    time.sleep(1)
    pag.click(1165,411) #删除数字
    time.sleep(1)
    pag.hotkey('ctrl', 'a')
    time.sleep(1)
    pag.press('delete')  # 清空所有内容
    pag.typewrite(num_index)
    time.sleep(1)
    pag.click(1208,448)
    time.sleep(1)
    pag.click(1218,799)

def new_update(y_ix,num_index):
    time.sleep(3)
    pag.doubleClick(1107, y_ix)  # 进入
    time.sleep(2)
    pag.doubleClick(680, 267)
    time.sleep(2)
    pag.click(1165,411) #删除数字
    time.sleep(1)
    pag.hotkey('ctrl', 'a')
    time.sleep(1)
    pag.press('delete')  # 清空所有内容
    pag.typewrite(num_index)
    time.sleep(1.5)
    pag.click(1273,451)
    time.sleep(1.5)
    pag.click(1218, 799)
ii = 250
num = 37
for i in range(0,13): #16
    new_update(ii,str(num))
    # print(i)
    # print(ii)
    ii+=37
    num += 1

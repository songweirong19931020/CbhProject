# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: asyncio接口.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/22 16:44
# ---
import asyncio

async def func(name):
    print('start',name)
    #await 可能会发生阻塞的方法
    #await关键字必须写在一个async函数里
    await asyncio.sleep(1)
    print('end')


loop = asyncio.get_event_loop()
# loop.run_until_complete(func('swr')) #启一个任务
loop.run_until_complete(asyncio.wait([func('swr'),func('leslie')])) #启一个任务



# 协程的原理
import time
def sleep(n):
    print('start sleep')
    yield time.time()+n
    print('end sleep')

def func(n):
    print(123)
    g = sleep(n)
    yield from g
    print(456)

n=1
g = func(n)
ret = next(g)
print(ret)
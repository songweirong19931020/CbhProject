# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: theard_condition.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/26 10:23
# ---

import threading
#条件变量，用于复杂逻辑锁
# class XiaoAi(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name='XiaoAi')
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}在".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{}好啊".format(self.name))
#         self.lock.release()
#
#
# class TianMall(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name='TianMall')
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}:小艾同学".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{}:我们来对古诗吧".format(self.name))
#         self.lock.release()

#运用condition
from threading import Condition
class XiaoAi(threading.Thread):
    def __init__(self,cond):
        super().__init__(name='XiaoAi')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}好的".format(self.name))
            self.cond.notify()



class TianMall(threading.Thread):
    def __init__(self,cond):
        super().__init__(name='TianMall')
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}:小艾同学".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}:我们来对古诗把".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    lock = threading.Condition()
    xiaoai = XiaoAi(lock)
    tianmao = TianMall(lock)
    #启动顺序很重要
    # condition有两把锁，一个会在线程调用wait方法的时候释放，
    # 上面的锁胡子哎每次调用wait时分配一把，并放入condition的等待队列中，等待notify方法的唤醒
    xiaoai.start()
    tianmao.start()
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: TreeGraph.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/19 10:09
# ---
import datetime
import time

today = datetime.date.today()
def Get_2_Month(month_time=[],cycle_day=2,is_current=0):
    '''
    :param month_time:
    :return: month_list:存放202001-T-1月份数据数据
    '''
    if is_current==1:
        cycle_day = cycle_day - 1
        first = today.replace(day=1)
        end_month = today
    else:
        cycle_day=cycle_day
        first = today.replace(day=1)
        end_month = (first - datetime.timedelta(days=1))
    cycle_day = cycle_day * 30
    start_month = (today - datetime.timedelta(days=cycle_day))
    # b = datetime.date.today()
    month_time=[]
    for i in range(start_month.toordinal(), end_month.toordinal()):
        # print(datetime.date.fromordinal(i))
        month_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m")))
        month_list = list(set(month_time))
        month_list.sort()
    return month_list



def Get_Month_All(month_time=[],year = 2020,month=1,days=1):
    '''
    :param month_time:
    :return: month_list:存放202001-T-1月份数据数据
    '''
    start_month = datetime.date(year, month, days)
    first = today.replace(day=1)
    end_month = (first - datetime.timedelta(days=1))
    # b = datetime.date.today()
    # month_time=[]
    for i in range(start_month.toordinal(), end_month.toordinal()):
        # print(datetime.date.fromordinal(i))
        month_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m")))
        month_list = list(set(month_time))
    return month_list

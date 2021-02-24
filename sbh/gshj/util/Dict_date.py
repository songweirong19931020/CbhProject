# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Dict_date
   Description :
   Author :       CBH
   date：         2020/7/4 21: 01
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/4 21: 01:
-------------------------------------------------
"""
import datetime
import time

today = datetime.date.today()


def Get_Time_All(list_time=[],year = 2020,month=1,days=1,e_year = 2020,e_month=6,e_days=30):
    '''
    :param list_time:
    :return: date_list:存放日期列表，保存到20200101-当前时间
    '''
    start_date = datetime.date(year, month, days)
    end_date = datetime.date(e_year, e_month, e_days)
    for i in range(start_date.toordinal(), end_date.toordinal()):
        # print(datetime.date.fromordinal(i))
        list_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m%d")))
    date_list = list_time
    return date_list


def Get_Time_All_Split(list_time=[],start_date='2020-1-1',end_date='2020-6-30'):
    '''
    :param list_time:
    :return: date_list:存放日期列表，保存到20200101-当前时间
    '''
    split_start = start_date.split('-')
    split_end = end_date.split('-')
    start_date = datetime.date(int(split_start[0]),int(split_start[1]), int(split_start[2]))
    end_date = datetime.date(int(split_end[0]), int(split_end[1]), int(split_end[2]))
    for i in range(start_date.toordinal(), end_date.toordinal()):
        # print(datetime.date.fromordinal(i))
        list_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m%d")))
    date_list = list_time
    return date_list

a = Get_Time_All_Split(start_date='2020-6-30',end_date='2020-10-30')

def Get_Time_section_30(list_time=[],cycle_day=30):
    a = (today - datetime.timedelta(days=cycle_day))
    b = datetime.date.today()
    for i in range(a.toordinal(), b.toordinal()):
        # print(datetime.date.fromordinal(i))
        list_time.append(datetime.date.fromordinal(i).strftime("%Y%m%d"))
    return list_time

def Get_Time_section_60_30(list_time=[]):
    a = (today - datetime.timedelta(days=60))
    b = (today - datetime.timedelta(days=30))
    for i in range(a.toordinal(), b.toordinal()):
        # print(datetime.date.fromordinal(i))
        list_time.append(datetime.date.fromordinal(i).strftime("%Y%m%d"))
    return list_time


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









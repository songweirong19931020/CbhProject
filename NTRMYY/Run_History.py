# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Run_History.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/7 12:35
# ---
from NTRMYY.util.Connect_oracle import *
from NTRMYY.util.account import *
from NTRMYY.util.Run_Sql_Demo import *
from NTRMYY.util.Get_func import *
import pandas as pd
import numpy as np
import itertools
import multiprocessing
from io import StringIO
import datetime as dt
from dateutil.parser import parse
from NTRMYY.util.Dict_date import *
from NTRMYY.util.LogUitl import *
from concurrent.futures import ThreadPoolExecutor,as_completed
log = Logger(r'C:\Users\CBH\Downloads\Detailed.log', logging.ERROR, logging.DEBUG)
# list_time = Get_Time_All_Split([],start_date='2020-1-1',end_date='2020-12-30') #dw指定开始日期,非双位数月份前面不要额外加0
list_time = Get_Month_All([],2020,1) #dw指定开始日期,非双位数月份前面不要额外加0
list_function_name = Get_FuncName(routine_schema='dw',list_function_name=[],) #dw任务
# list_function_name = Get_FuncName(routine_schema='dwd',list_function_name=[],in_out_flag='I')  # 多个人物之间逗号隔开  dwd任务
n = 1
list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
re = Run_Simple(max_workers=1,routine_schema='dw',list_time=list_time,list_result=list_result)

list_result_reveser = [list_result[i:i + n] for i in range(0, len(list_function_name))]

def text_list(list_func_name=[],result_hob=[]):
    try:
        for f_name in list_func_name:
            # print(f_name)
            result_hob.append(f_name)
        # print(f"task:{f_name} finished")
    except Exception as e:
        print(e)
        log.info("任务失败，循环结束！")
    # return f_name


if __name__ == '__main__':
    total_job=len(list_function_name)
    try:
        with ThreadPoolExecutor(max_workers=5) as t:
            obj_list = []
            for i in range(len(list_result)):
                obj = t.submit(text_list, list_result[i])
                obj_list.append(obj)
                print("任务完成进度：{}%".format(round((len(obj_list)/total_job),5)*100))
            for future in as_completed(obj_list):
                data = future.result()


    except:
        t.shutdown()


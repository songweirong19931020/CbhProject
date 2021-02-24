# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Function_executor.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/12/7 10:59
# ---
from NTRMYY.util.Dict_date import *
from NTRMYY.util.LogUitl import *
from NTRMYY.util.Run_Sql_Demo import Run_Sql_Excute
from NTRMYY.util.Get_func import *
import datetime as dt
import os,sys
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def Function_Excute(is_retry='0',routine_schema='dwd',max_workers=8,list_time=[],list_result=[]):
    if is_retry == '0':
        try:
            with ThreadPoolExecutor(max_workers=max_workers) as t:
                obj_list=[]
                for i in range(len(list_result)):
                    obj = t.submit(Run_Sql_Excute,list_time, list_result[i],'0',routine_schema)
                    obj_list.append(obj)
                for future in as_completed(obj_list):
                    data = future.result()
        except:
            t.shutdown()
    else:
        try:
            with ThreadPoolExecutor(max_workers=max_workers) as t:
                obj_list=[]
                for i in range(len(list_result)):
                    obj = t.submit(Run_Sql_Excute,list_time, list_result[i],'1',routine_schema)
                    obj_list.append(obj)
                for future in as_completed(obj_list):
                    data = future.result()
        except:
            t.shutdown()

if __name__ == '__main__':
    list_time = Get_Time_section_30(list_time=[],cycle_day=1)
    list_function_name = Get_FuncName(routine_schema='dwd',in_out_flag='OI')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    re = Function_Excute(is_retry='0',routine_schema='dwd',max_workers=8)
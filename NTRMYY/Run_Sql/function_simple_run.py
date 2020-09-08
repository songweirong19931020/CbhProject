# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: function_simple_run.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/8 11:01
# ---
from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.Dict_date import *
from NTRMYY.util.LogUitl import *
import datetime as dt
import pandas as pd
import os,sys
from multiprocessing import Process
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
def Run_Sql_Month(list_time,list_func_name):
    '''
    :param list_time: 时间列表 格式：'202001'
    :param list_function: 函数列表:"fun_dw_inp_drgs_patient_m"
    :return: None
    '''
    try:
        for f_name in list_func_name:
            for t_time in list_time:
                print(list_time.index(t_time))
                with PgSQLContextManager() as db_cursor:
                    start_time = dt.datetime.now()
                    sql = ''' select dwd."{f_name}"('{day_id}','{day_id}'); '''.format(day_id=t_time,f_name = f_name)
                    log.info("执行sql日期为：{}".format(t_time))
                    log.info(sql)
                    db_cursor.execute(sql)
                    end_date = dt.datetime.now()
                    log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')
    except:
        log.info("循环结束")

if __name__ == '__main__':
    list_time = Get_Time_All(list_time=[])
    list_function_name = ['fun_dwd_DI2001_d','fun_dwd_DI2002_d','fun_dwd_DI2003_d',
                          'fun_dwd_DI2004_d','fun_dwd_DI2021_d']
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    #
    # for i in list_result:
    #     print(i)
    p_lst = []
    for arg in list_result:
        print(arg)
        p = Process(target=Run_Sql_Month, args=(list_time, arg))
        p.start()
        p_lst.append(p)
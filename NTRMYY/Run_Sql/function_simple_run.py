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
from NTRMYY.util.Get_func import *
from NTRMYY.NC.error_class import *
import datetime as dt
import pandas as pd
import os,sys
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
def Run_Sql_Month(list_time,list_func_name,routine_schema='dwd'):
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
                    sql = ''' select {routine_schema}."{f_name}"('{day_id}','{day_id}'); '''.format(day_id=t_time,f_name = f_name,routine_schema=routine_schema)
                    log.info("执行sql日期为：{}".format(t_time))
                    log.info(sql)
                    db_cursor.execute(sql)
                    end_date = dt.datetime.now()
                    log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')
    except:
        log.info("循环结束")

if __name__ == '__main__':
    #list_time = Get_Time_Qj_30(list_time=[])
    # list_time = Get_Time_All(list_time=[])
    # list_time = Get_Month_All(month_time=[])
    # list_function_name = Get_FuncName('dwd')
    list_time = ['202010',]
    list_function_name = ['fun_dw_all_med_dept_work_m']
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    #
    # for i in list_result:
    #     print(i)
    # p_lst = []
    # for arg in list_result:
    #     print(arg)
    #     p = Process(target=Run_Sql_Month, args=(list_time, arg,'dw'))
    #     p.start()
    #     p_lst.append(p)

    #第二种线程池写法
    th  = ProcessPoolExecutor(15)
    for i in range(len(list_result)):
        th.submit(Run_Sql_Month,list_time, list_result[i],'dw')


# for i in range(10000):
#     with PgSQLContextManager() as pg_cursor:
#         sql = '''select
#  (pid)
# from pg_catalog.pg_stat_activity a
# where
# a."query" like '%select%fun_dwd%'
# and a.client_addr = '192.168.12.101';
# '''
#         pg_cursor.execute(sql)



if __name__ == '__main__':
    list_time = Get_Time_section_30(list_time=[],cycle_day=60)
    list_function_name = Get_FuncName(routine_schema='dwd',in_out_flag='I')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    try:
        with ThreadPoolExecutor(max_workers=8) as t:
            obj_list=[]
            for i in range(len(list_result)):
                obj = t.submit(Run_Sql_Excute, list_time, list_result[i], '0', 'dwd')
                obj_list.append(obj)
            for future in as_completed(obj_list):
                data = future.result()
        result = Check_Failed_job(routine_schema='dwd',service='DI')
        checkresult(result)
    except:
        t.shutdown()

if __name__ == '__main__':
    list_time = Get_Time_section_30(list_time=[], cycle_day=30)
    list_function_name = Get_FuncName(routine_schema='dwd', in_out_flag='O')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    try:
        with ThreadPoolExecutor(max_workers=8) as t:
            obj_list=[]
            for i in range(len(list_result)):
                obj = t.submit(Run_Sql_Excute, list_time, list_result[i], '0', 'dwd')
                obj_list.append(obj)
            for future in as_completed(obj_list):
                data = future.result()
        result = Check_Failed_job(routine_schema='dwd',service='DU')
        checkresult(result)
    except:
        t.shutdown()


if __name__ == '__main__':
    list_time = Get_Time_section_30(list_time=[],cycle_day=60)
    list_function_name = Get_FuncName('ods')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    p_lst = []
    no_param_list = ['fun_his_v_emr_fc_pati_diag_d']
    try:
        with ThreadPoolExecutor(max_workers=4) as t:
            for arg in list_result:
                if (arg[0] not in no_param_list):
                    obj = t.submit(Run_Sql_Excute, list_time, arg, '0', 'ods')
                else:
                    obj = t.submit(Run_Sql_Excute, list_time, arg, '0', 'ods','1')

    except:
        t.shutdown()




if __name__ == '__main__':
    list_time = Get_2_Month(month_time=[],cycle_day=2)
    list_function_name = Get_FuncName('dw')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    try:
        with ThreadPoolExecutor(max_workers=1) as t:
            obj_list=[]
            for i in range(len(list_result)):
                obj = t.submit(Run_Sql_Excute,list_time, list_result[i],'0','dw')
                obj_list.append(obj)
            for future in as_completed(obj_list):
                data = future.result()
    except:
        t.shutdown()


if __name__ == '__main__':
    list_time = Get_Time_section_30(list_time=[],cycle_day=60)
    list_function_name = Get_FuncName(routine_schema='dwd',in_out_flag='OI')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    try:
        with ThreadPoolExecutor(max_workers=1) as t:
            obj_list=[]
            for i in range(len(list_result)):
                obj = t.submit(Run_Sql_Excute,list_time, list_result[i],'0','dwd')
                obj_list.append(obj)
            for future in as_completed(obj_list):
                data = future.result()
    except:
        t.shutdown()



if __name__ == '__main__':
    list_time = Get_Time_section_30(list_time=[],cycle_day=60)
    p_lst = []
    no_param_list = ['fun_his_v_emr_fc_pati_diag_d']
    result_list = Get_Failed_job(routine_schema='ods')
    if len(result_list)==0:
        print('无失败任务，无需重复执行！')
    else:
        n = len(result_list)
        list_result = [result_list[i:i + n] for i in range(0, len(result_list), n)]
        p_lst = []
        try:
            with ThreadPoolExecutor(max_workers=4) as t:
                for arg in list_result:
                    if (arg[0] not in no_param_list):
                        obj = t.submit(Run_Sql_Excute, list_time, arg, '1', 'ods')
                    else:
                        obj = t.submit(Run_Sql_Excute, list_time, arg, '1', 'ods', '1')
        except:
            t.shutdown()




from util.Dict_date import *
from util.LogUitl import *
from util.Run_Sql_Demo import Run_Sql_Excute
from util.Get_func import *
from util.Temirel import *
import datetime as dt
import os,sys
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if __name__ == '__main__':
    list_time = Get_2_Month(month_time=[],cycle_day=2)
    list_function_name = Get_FuncName('dw')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    try:
        with ThreadPoolExecutor(max_workers=1) as t:
            obj_list=[]
            for i in range(len(list_result)):
                obj = t.submit(Run_Sql_Excute,list_time, list_result[i],'0','dw')
                obj_list.append(obj)
            for future in as_completed(obj_list):
                data = future.result()
    except:
        t.shutdown()





if __name__ == '__main__':
    list_time = Get_Time_section_30(list_time=[],cycle_day=60)
    list_function_name = Get_FuncName(routine_schema='dwd',in_out_flag='OI')
    n = 1
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    try:
        with ThreadPoolExecutor(max_workers=1) as t:
            obj_list=[]
            for i in range(len(list_result)):
                obj = t.submit(Run_Sql_Excute,list_time, list_result[i],'0','dwd')
                obj_list.append(obj)
            for future in as_completed(obj_list):
                data = future.result()
    except:
        t.shutdown()
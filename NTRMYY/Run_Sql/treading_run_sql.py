# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: treading_run_sql.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/15 11:48
# ---
from threading import Thread
from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.Dict_date import *
from NTRMYY.util.LogUitl import *
import datetime as dt
import pandas as pd
import os,sys
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
def Run_Sql_Month(list_time,list_func_name):
    '''
    :param list_time: 时间列表 格式：'202001'
    :param list_function: 函数列表:"fun_dw_inp_drgs_patient_m"
    :return: None
    '''
    # try:
    for f_name in list_func_name:
        for t_time in list_time:
            print(list_time.index(t_time))
            try:
                with PgSQLContextManager() as db_cursor:
                    start_time = dt.datetime.now()
                    sql = ''' select dwd."{f_name}"('{day_id}','{day_id}'); '''.format(day_id=t_time,f_name = f_name)
                    log.info("执行sql日期为：{}".format(t_time))
                    log.info(sql)
                    db_cursor.execute(sql)
                    end_date = dt.datetime.now()
                    log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')
            except:
                with PgSQLContextManager() as db_cursor:
                    sql_log = '''
                                                   insert into dwd.run_table_log(function_name,insert_time,status,start_date,end_date)
                                        values('{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}');'''.format(
                        function_name=f_name, insert_time='now()', status_code='Failed',
                        start_date=t_time, end_date=t_time
                    )
                    db_cursor.execute(sql_log)
                continue
        with PgSQLContextManager() as db_cursor:
            sql_log = '''
                       insert into dwd.run_table_log(function_name,insert_time,status,start_date,end_date)
            values('{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}');'''.format(
                function_name=f_name, insert_time='now()', status_code='Successed',
                start_date=list_time[0], end_date=list_time[-1]
            )
            db_cursor.execute(sql_log)




if __name__ == '__main__':
    list_time = Get_Time_Qj_30(list_time=[])
    with PgSQLContextManager() as db_cursor:
        sql = '''
          select
    --  substring(specific_name from '%#"fun_dwd_D_______#"%' FOR '#'),
     substring(specific_name from '^.{16}'),
    routine_schema, ---数据库名
    specific_name, ----函数事件名
    routine_definition ---函数内容
    from information_schema.routines
    where
    routine_schema ='dwd'
    GROUP BY
    routine_schema, ---数据库名
    specific_name, ----函数事件名
    routine_definition
    having  substring(specific_name from '^.{10}') = 'fun_dwd_DU'
        '''
        db_cursor.execute(sql)
        result = db_cursor.fetchall()
        # df = pd.DataFrame(result)
        # df.columns = ['result', 'a', 'b', 'c']
        # 存放函数名称的列表
        list_function_name = []
        for i in range(len(result)):
            list_function_name.append(result[i][0])
        # for row in df.itertuples(index=True, name='Pandas'):
        #     print(getattr(row, 'result'))
        #     list_function_name.append(getattr(row, 'result'))
    n = 5
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    p_lst = []
    for arg in list_result:
        print(arg)
        p = Thread(target=Run_Sql_Month, args=(list_time,arg))
        p.start()
        p_lst.append(p)
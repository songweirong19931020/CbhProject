# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: PgfunctionAutoRun.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/25 20:54
# ---
from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.Dict_date import *
from NTRMYY.util.LogUitl import *
from NTRMYY.util.Get_func import *
import datetime as dt
import os,sys
from dateutil.parser import parse
log = Logger('Detailed.log', logging.ERROR, logging.DEBUG)
today = datetime.date.today()
class PgFunctionAutoRunsql(object):
    def __init__(self,routine_schema):
        self.routine_schema = routine_schema

    # def __init__(self,routine_schema,fu_name,list_time,list_func_name,is_retry,is_param):
    #     self.routine_schema = routine_schema
    #     self.fu_name = fu_name
    #     self.list_time = list_time
    #     self.list_func_name = list_func_name
    #     self.is_retry = is_retry
    #     self.is_param = is_param

    def Get_Time_section_30(self,list_time=[], cycle_day=30):
        a = (today - datetime.timedelta(days=cycle_day))
        b = datetime.date.today()
        for i in range(a.toordinal(), b.toordinal()):
            # print(datetime.date.fromordinal(i))
            list_time.append(datetime.date.fromordinal(i).strftime("%Y%m%d"))
        return list_time

    def Get_2_Month(self,month_list=[], cycle_day=2):
        '''
        :param month_time:
        :return: month_list:存放202001-T-1月份数据数据
        '''
        cycle_day = cycle_day * 30
        start_month = (today - datetime.timedelta(days=cycle_day))
        first = today.replace(day=1)
        end_month = (first - datetime.timedelta(days=1))
        # b = datetime.date.today()
        month_time = []
        for i in range(start_month.toordinal(), end_month.toordinal()):
            # print(datetime.date.fromordinal(i))
            month_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m")))
            month_list = list(set(month_time))
            month_list.sort()
        return month_list

    def Delete_log(self,routine_schema,fu_name=None):
        with PgSQLContextManager() as db_cursor:
            delete_sql = '''delete from dwd.run_table_log where routine_schema = '{routine_schema}' and date(insert_time)= current_date and function_name = '{function_name}';'''.format(
                routine_schema=routine_schema, function_name=fu_name)
            db_cursor.execute(delete_sql)

    def Get_FuncName(self,routine_schema='dwd', list_function_name=[], in_out_flag='O'):
        with PgSQLContextManager() as db_cursor:
            if routine_schema == 'ods':
                sql = '''
                              select
                         substring(specific_name  from '^(.*?)......$'),
                        routine_schema, ---数据库名
                        specific_name, ----函数事件名
                        routine_definition ---函数内容
                        from information_schema.routines
                        where
                        routine_schema =''' + "'" + routine_schema + "'" + "  and substring(specific_name from '^.{6}') = 'fun_hi'"
                db_cursor.execute(sql)
                result = db_cursor.fetchall()
                # df = pd.DataFrame(result)
                # df.columns = ['result', 'a', 'b', 'c']
                # 存放函数名称的列表
                list_function_name = []
                for i in range(len(result)):
                    list_function_name.append(result[i][0])
            elif routine_schema == 'dw':
                sql = '''
                                          select
                                     substring(specific_name  from '^(.*?)......$'),
                                    routine_schema, ---数据库名
                                    specific_name, ----函数事件名
                                    routine_definition ---函数内容
                                    from information_schema.routines
                                    where
                                    routine_schema =''' + "'" + routine_schema + "'" + "  and substring(specific_name from '^.{6}') = 'fun_dw'"
                db_cursor.execute(sql)
                result = db_cursor.fetchall()
                # df = pd.DataFrame(result)
                # df.columns = ['result', 'a', 'b', 'c']
                # 存放函数名称的列表
                list_function_name = []
                for i in range(len(result)):
                    list_function_name.append(result[i][0])
            else:
                if in_out_flag == 'O':
                    sql = '''
                      select
                 substring(specific_name  from '^(.*?)......$'),
                routine_schema, ---数据库名
                specific_name, ----函数事件名
                routine_definition ---函数内容
                from information_schema.routines
                where
                routine_schema =''' + "'" + routine_schema + "'" + "  and substring(specific_name from '^.{6}') = 'fun_dw' " \
                          + "and replace(substring(specific_name from '.{9,10}'),'fun_dwd_','') = 'DU'"
                    db_cursor.execute(sql)
                    result = db_cursor.fetchall()
                    # df = pd.DataFrame(result)
                    # df.columns = ['result', 'a', 'b', 'c']
                    # 存放函数名称的列表
                    list_function_name = []
                    for i in range(len(result)):
                        list_function_name.append(result[i][0])
                elif in_out_flag == 'I':
                    sql = '''
                                      select
                                 substring(specific_name  from '^(.*?)......$'),
                                routine_schema, ---数据库名
                                specific_name, ----函数事件名
                                routine_definition ---函数内容
                                from information_schema.routines
                                where
                                routine_schema =''' + "'" + routine_schema + "'" + "  and substring(specific_name from '^.{6}') = 'fun_dw' " \
                          + "and replace(substring(specific_name from '.{9,10}'),'fun_dwd_','') = 'DI'"
                    db_cursor.execute(sql)
                    result = db_cursor.fetchall()
                    # df = pd.DataFrame(result)
                    # df.columns = ['result', 'a', 'b', 'c']
                    # 存放函数名称的列表
                    list_function_name = []
                    for i in range(len(result)):
                        list_function_name.append(result[i][0])
                elif in_out_flag == 'OI':
                    sql = '''
                                      select
                                 substring(specific_name  from '^(.*?)......$'),
                                routine_schema, ---数据库名
                                specific_name, ----函数事件名
                                routine_definition ---函数内容
                                from information_schema.routines
                                where
                                routine_schema =''' + "'" + routine_schema + "'" + "  and substring(specific_name from '^.{6}') = 'fun_dw' " \
                          + "and (replace(substring(specific_name from '.{9,10}'),'fun_dwd_','') in('in','ou'))"
                    db_cursor.execute(sql)
                    result = db_cursor.fetchall()
                    # df = pd.DataFrame(result)
                    # df.columns = ['result', 'a', 'b', 'c']
                    # 存放函数名称的列表
                    list_function_name = []
                    for i in range(len(result)):
                        list_function_name.append(result[i][0])
            return list_function_name

    def Get_Failed_job(self,routine_schema='dwd', failed_job=[]):
        with PgSQLContextManager() as pg_cursor:
            select_sql = '''
            select
            distinct
            function_name
            from dwd.run_table_log
            where
            status='Failed'
            and routine_schema= '{routine_schema}'
            and date(insert_time) = current_date
            '''.format(routine_schema=routine_schema)
            pg_cursor.execute(select_sql)
            result = pg_cursor.fetchall()
            failed_job = []
            for i in range(len(result)):
                failed_job.append(result[i][0])
            return failed_job

    def Run_Sql_Excute(self,list_time,list_func_name,is_retry='0',routine_schema='dwd',is_param='0'):
        '''
        :param list_time: 时间列表 格式：'202001'
        :param list_function: 函数列表:"fun_dw_inp_drgs_patient_m"
        :return: None
        '''
        # try:
        if is_retry == '0':
            if is_param == '0':
                for f_name in list_func_name:
                    job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    for t_time in list_time:
                        # print(list_time.index(t_time))
                        try:
                            with PgSQLContextManager() as db_cursor:
                                run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                start_time = dt.datetime.now()
                                sql = ''' select {routine_schema}."{f_name}"('{day_id}','{day_id}'); '''.format(routine_schema=routine_schema,day_id=t_time,f_name = f_name)
                                log.info("执行sql日期为：{}".format(t_time))
                                log.info(sql)
                                db_cursor.execute(sql)
                                end_date = dt.datetime.now()
                                log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=f_name,seconds=end_date-start_time))
                        except Exception as e :
                            with PgSQLContextManager() as db_cursor:
                                failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                failed_use_time = (failed_end_date-run_start_date).seconds
                                sql_log = '''
                                                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                                    routine_schema = routine_schema,
                                    function_name=f_name, insert_time='now()', status_code='Failed',
                                    start_date=t_time, end_date=t_time,retry_count = 'null',job_start_date=run_start_date,
                                    job_end_date=failed_end_date,total_use_time = failed_use_time
                                )
                                db_cursor.execute(sql_log)
                            print(e)
                            continue
                    with PgSQLContextManager() as db_cursor:
                        job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        total_use_time = (job_end_date-job_start_date).seconds
                        sql_log = '''
                                   insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                        values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            routine_schema = routine_schema,function_name=f_name, insert_time='now()', status_code='Successed',
                            start_date=list_time[0], end_date=list_time[-1],retry_count='null',job_start_date=job_start_date,job_end_date=job_end_date,
                            total_use_time = total_use_time
                        )
                        db_cursor.execute(sql_log)
            elif is_param == '1':
                try:
                    with PgSQLContextManager() as db_cursor:
                        run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        start_time = dt.datetime.now()
                        sql = ''' select {routine_schema}."{f_name}"(); '''.format(
                            routine_schema=routine_schema, f_name=list_func_name[0])
                        log.info(sql)
                        db_cursor.execute(sql)
                        end_date = dt.datetime.now()
                        log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=list_func_name[0], seconds=end_date - start_time))
                        job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        total_use_time = (job_end_date - run_start_date).seconds
                        sql_log = '''
                                   insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                        values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            routine_schema=routine_schema, function_name=list_func_name[0], insert_time='now()',
                            status_code='Successed',
                            start_date='null', end_date='null', retry_count='null',
                            job_start_date=run_start_date, job_end_date=job_end_date,
                            total_use_time=total_use_time
                        )
                        db_cursor.execute(sql_log)
                except Exception as e:
                    with PgSQLContextManager() as db_cursor:
                        failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        failed_use_time = (failed_end_date - run_start_date).seconds
                        sql_log = '''
                                                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            routine_schema=routine_schema,
                            function_name=list_func_name[0], insert_time='now()', status_code='Failed',
                            start_date='null', end_date='null', retry_count='null', job_start_date=run_start_date,
                            job_end_date=failed_end_date, total_use_time=failed_use_time
                        )
                        db_cursor.execute(sql_log)
            else:
                print('参数输入错误，只能是0或1！')
        elif is_retry == '1':
            if is_param == '0':
                for f_name in list_func_name:
                    # 先删掉日志表里的数据
                    self.Delete_log(routine_schema=routine_schema,fu_name=f_name)
                    job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    for t_time in list_time:
                        # print(list_time.index(t_time))
                        try:
                            with PgSQLContextManager() as db_cursor:
                                run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                start_time = dt.datetime.now()
                                sql = ''' select {routine_schema}."{f_name}"('{day_id}','{day_id}'); '''.format(routine_schema=routine_schema,day_id=t_time,f_name = f_name)
                                log.info("执行sql日期为：{}".format(t_time))
                                log.info(sql)
                                db_cursor.execute(sql)
                                end_date = dt.datetime.now()
                                log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=f_name,seconds=end_date-start_time))
                        except Exception as e:
                            with PgSQLContextManager() as db_cursor:
                                failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                failed_use_time = (failed_end_date-run_start_date).seconds
                                sql_log = '''
                                                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                                    routine_schema = routine_schema,
                                    function_name=f_name, insert_time='now()', status_code='Failed',
                                    start_date=t_time, end_date=t_time,retry_count = 'null',job_start_date=run_start_date,job_end_date=failed_end_date,total_use_time = failed_use_time
                                )
                                db_cursor.execute(sql_log)
                            print(e)
                            continue
                    with PgSQLContextManager() as db_cursor:
                        #加入检查重跑是否还是失败的验证逻辑
                        failed_job = Get_Failed_job(routine_schema)
                        if len(failed_job)==0:
                            self.Delete_log(routine_schema=routine_schema,fu_name=f_name)
                            job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                            total_use_time = (job_end_date - job_start_date).seconds
                            sql_log = '''
                                       insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                            values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                                routine_schema = routine_schema,function_name=f_name, insert_time='now()', status_code='Successed',
                                start_date=list_time[0], end_date=list_time[-1],retry_count='1',job_start_date=job_start_date,
                                job_end_date=job_end_date,total_use_time = total_use_time
                            )
                            print(sql_log)
                            db_cursor.execute(sql_log)
                        else :
                            print('任务再次执行失败！详情请查看日志。')
                            with PgSQLContextManager() as db_cursor:
                                self.Delete_log(routine_schema=routine_schema,fu_name=f_name)
                                job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                total_use_time = (job_end_date - job_start_date).seconds
                                sql_log = '''
                                                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                                    routine_schema=routine_schema, function_name=f_name, insert_time='now()',
                                    status_code='Failed',
                                    start_date=list_time[0], end_date=list_time[-1], retry_count='1',
                                    job_start_date=job_start_date,
                                    job_end_date=job_end_date, total_use_time=total_use_time
                                )
                                print(sql_log)
                                db_cursor.execute(sql_log)
            elif  is_param == '1':
                try:
                    with PgSQLContextManager() as db_cursor:
                        self.Delete_log(routine_schema=routine_schema, fu_name= list_func_name[0])
                        run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        start_time = dt.datetime.now()
                        sql = ''' select {routine_schema}."{f_name}"(); '''.format(
                            routine_schema=routine_schema, f_name=list_func_name[0])
                        log.info(sql)
                        db_cursor.execute(sql)
                        end_date = dt.datetime.now()
                        log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=list_func_name[0],
                                                                               seconds=end_date - start_time))
                        job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        total_use_time = (job_end_date - run_start_date).seconds
                        sql_log = '''
                                   insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                        values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            routine_schema=routine_schema, function_name=list_func_name[0], insert_time='now()',
                            status_code='Successed',
                            start_date='null', end_date='null', retry_count='1',
                            job_start_date=run_start_date, job_end_date=job_end_date,
                            total_use_time=total_use_time
                        )
                        db_cursor.execute(sql_log)
                except Exception as e:
                    with PgSQLContextManager() as db_cursor:
                        failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        failed_use_time = (failed_end_date - run_start_date).seconds
                        sql_log = '''
                                                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            routine_schema=routine_schema,
                            function_name=list_func_name[0], insert_time='now()', status_code='Failed',
                            start_date='null', end_date='null', retry_count='1', job_start_date=run_start_date,
                            job_end_date=failed_end_date, total_use_time=failed_use_time
                        )
                        db_cursor.execute(sql_log)
        else:
            print('is_retry参数输入错误，只能是0或1！')




list_func_name=['fun_dwd_DI1026_d']

a = PgFunctionAutoRunsql()

a.Get_FuncName()

list_time = a.Get_Time_section_30()

a.Run_Sql_Excute(list_time=list_time,list_func_name=list_func_name)
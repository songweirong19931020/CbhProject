# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: error_class.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/10/27 8:39
# ---
# class Check_Result_Status(Exception):
#     def __init__(self,message):
#         super.__init__(message)
#
#     def __str__(self):
#         print("任务执行失败，报错信息：" + str(self.message))

from NTRMYY.util.account import PgSQLContextManager
class Check_Result_Status(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

def checkresult(reslut_list=[]):
    if len(reslut_list)==0:
        print('所有任务执行成功!')
    else:
        raise Check_Result_Status('''任务执行失败，失败任务清单:{}'''
                              .format(reslut_list))


def Check_Failed_job(routine_schema='dwd',failed_job=[],service='DU'):
    with PgSQLContextManager() as pg_cursor:
        condition = '''and (replace(substring(function_name from '.{9,10}'),'fun_dwd_','')='''
        select_sql='''
        select
        distinct
        function_name
        from dwd.run_table_log
        where
        status='Failed' and date(insert_time)= current_date and routine_schema =''' \
          + "'" + routine_schema + "'" + " and (replace(substring(function_name from '.{9,10}'),'fun_dwd_','')) =" + "'" + service + "'"

        print(select_sql)
        pg_cursor.execute(select_sql)
        result = pg_cursor.fetchall()
        failed_job=[]
        for i in range(len(result)):
            failed_job.append(result[i][0])
        return failed_job



list_2 = []
if  list_2:
    print('list_2 is not none')
else:
    print('list_2 is none')

reslut_list=[1]
if reslut_list:
    print('所有任务执行成功!')
else:
    raise Check_Result_Status('''任务执行失败，失败任务清单:{}'''
                      .format(reslut_list))


def checkresult(reslut_list=[]):
    if reslut_list:
        print('所有任务执行成功!')
    else:
        raise Check_Result_Status('''任务执行失败，失败任务清单:{}'''
                                  .format(reslut_list))
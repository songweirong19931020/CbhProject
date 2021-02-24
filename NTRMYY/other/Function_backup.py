# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Function_backup.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/25 9:12
# ---

from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.LogUitl import *
import pandas as pd
import datetime
import os,sys
def FunctionBackup(path=r'C:\Users\CBH\PycharmProjects\Cenboom\NTRMYY\other'):
    with PgSQLContextManager() as db_cursor:
        select_sql = '''
        select
    routine_schema, ---数据库名
    specific_name, ----函数事件名
    routine_definition ---函数内容
    from information_schema.routines
    where routine_schema not in ('pg_catalog','information_schema','public')
        '''
        db_cursor.execute(select_sql)
        # 返回执行结果
        result = db_cursor.fetchall()
        df = pd.DataFrame(result)
        df.columns = ['base_name', 'func_name', 'detail']
        path = path
        now_time = (datetime.datetime.now()).strftime('%Y-%m-%d')
        now_time = str(now_time)
        df.to_csv('{path}{name}{now_time}.csv'.format(name=os.path.basename(sys.argv[0]).replace('.py',''),now_time=now_time,path = path), index=False)







with PgSQLContextManager() as db_cursor:
    select_sql = '''
    select routine_schema,    ---数据库名
   substring(specific_name  from '^(.*?)......$') as sql_name,
   specific_name,     ----函数事件名
   routine_definition ---函数内容
from information_schema.routines
where routine_schema not in ('pg_catalog', 'information_schema', 'public')
    '''
    db_cursor.execute(select_sql)
    # 返回执行结果
    result = db_cursor.fetchall()
    df = pd.DataFrame(result)



for index,i in enumerate(df[3]):
    # print(i)
    sql = '''
    create function {name}(v_start_date character varying, v_end_date character varying) returns character varying
    language plpgsql
as
{detial}
    '''.format(name=str(df[0][index])+'.'+str(df[1][index]),detial = i)
    print(sql)
    path = r'D:\sql'
    with open(os.path.join(path,str(df[0][index])+'.'+str(df[1][index])+'.sql'),'a+',encoding='utf-8') as f:
        f.write(sql)
        f.close()


for index,i in enumerate(df[1]):
    # print(index)
    # print(str(df[0][index])+'.'+str(i))
    # print(df[0])
    condition = str(df[0][index])+'.'+str(i)
    print(condition)


    with PgSQLContextManager() as db_cursor:
        sql = '''
        select pg_get_functiondef('{conditon}'::regproc)
        '''.format(conditon=condition)
        db_cursor.execute(sql)
        # 返回执行结果
        result1 = db_cursor.fetchall()
        df1 = pd.DataFrame(result)
        path = r'D:\sql'
        df1.to_csv(os.path.join(path,condition+'.sql'))
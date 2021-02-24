# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: datamining.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/17 15:59
# ---
import pandas as pd
import numpy as np
from NTRMYY.util.ba_oracle import *
from NTRMYY.util.account import *
import pandas as pd
from NTRMYY.util.Dict_date import *
import numpy as np
import itertools
import multiprocessing
import datetime as dt
from io import StringIO

with PgSQLContextManager() as db_cursor:
    sql = '''
      select
 substring(specific_name  from '^(.*?)......$'),
routine_schema, ---数据库名
specific_name, ----函数事件名
routine_definition ---函数内容
from information_schema.routines
where
routine_schema =''' + "'" + 'dwd' + "'" + '''  and substring(specific_name from '^.{6}') = 'fun_dw' and substring(specific_name  from '^(.*?)......$') not in ('fun_dwd_DI2009_d','fun_dwd_DI2004_d','fun_dwd_DI2003_d','fun_dwd_DI2002_d','fun_dwd_DI2001_d',
'fun_dwd_DU0002_d','fun_dwd_DU0001_d','fun_dwd_DI2024_d','fun_dwd_DI2021_d','fun_dwd_outp_patient_info_d','fun_dwd_DU1016_d',
'fun_dwd_DU1015_d')'''
    db_cursor.execute(sql)
    result = db_cursor.fetchall()
    # df = pd.DataFrame(result)
    # df.columns = ['result', 'a', 'b', 'c']
    # 存放函数名称的列表
    list_function_name = []
    for i in range(len(result)):
        list_function_name.append(result[i][0])

len(list_function_name)


import re



pattern = '执行任务名称：(.*),执行完成时间为：(.*)'
result = re.findall(pattern,txt)

f_name=[]
second=[]
for i in result:
    print(i[0])
    f_name.append(i[0])
    second.append(i[1])

df = pd.DataFrame()
df['f_name'] = f_name
df['second'] = second

df.to_csv(r'C:\Users\CBH\Desktop\result.csv')


import datetime
import time
today = datetime.date.today()
start_month = (today - datetime.timedelta(days=63))
# start_month = datetime.date(2020, 1, 1)
first = today.replace(day=1)
end_month = (first - datetime.timedelta(days=1))
# b = datetime.date.today()
month_time=[]
for i in range(start_month.toordinal(), end_month.toordinal()):
    # print(datetime.date.fromordinal(i))
    month_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m")))
    month_list = list(set(month_time))
    month_list.sort()



def Get_2_Month(month_time=[]):
    '''
    :param month_time:
    :return: month_list:存放202001-T-1月份数据数据
    '''
    start_month = (today - datetime.timedelta(days=63))
    first = today.replace(day=1)
    end_month = (first - datetime.timedelta(days=1))
    # b = datetime.date.today()
    month_time=[]
    for i in range(start_month.toordinal(), end_month.toordinal()):
        # print(datetime.date.fromordinal(i))
        month_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m")))
        month_list = list(set(month_time))
        month_list.sort()
    return month_list


import datetime as dt
import time
from dateutil.parser import parse
st = dt.datetime.now()
st = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
time.sleep(1)
et = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print((et-st).seconds)
print((et-dt).seconds)


routine_schema= 'dwd'
f_name = 'fun_dddd'
delete_sql = '''delete from dwd.run_table_log where routine_schema = '{routine_schema}' and date(insert_time)= current_date and function_name = '{function_name}';'''.format(
                    routine_schema = routine_schema,function_name = f_name)
print(delete_sql)
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: new_rek_clearn.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/20 17:25
# ---
from NTRMYY.util.Connect_oracle import *
from NTRMYY.util.account import *
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
with OracleSQLContextManager() as db_cursor:
    rek_id_sql = '''
  select to_char(bi.enter_date,'yyyymmdd') as en_date , sum(bi.charges) as cnum
    FROM bms.rek k
  inner JOIN bms.bill_item bi
    on k.id = bi.rek_id
 where k.in_out_flag = 'I'
and to_char(k.rek_date,'yyyymm')>= '202001'
 and to_char(k.rek_date,'yyyymm')< to_char(current_date,'yyyymm')
   group by to_char(bi.enter_date,'yyyymmdd')
    '''
    db_cursor.execute(rek_id_sql)
    result = db_cursor.fetchall()
    dataframe = pd.DataFrame(result,columns=['en_date','cnum'])
    log.info("ORA对比数据已下载！")

with PgSQLContextManager() as pg_cursor:
    pg_rek_sql = '''

  select to_char(bi.enter_date,'yyyymmdd') as en_date , sum(bi.charges) as cnum
    FROM ods.his_bms_rek k
  inner JOIN ods.his_bms_bill_item bi
    on k.id = bi.rek_id
 where k.in_out_flag = 'I'
and to_char(k.rek_date,'yyyymm')>= '202001'
 and to_char(k.rek_date,'yyyymm')< to_char(current_date,'yyyymm')
   group by to_char(bi.enter_date,'yyyymmdd')
    '''
    pg_cursor.execute(pg_rek_sql)
    pg_result = pg_cursor.fetchall()
    pg_dataframe = pd.DataFrame(pg_result,columns=['en_date','cnum'])
    log.info("PG对比数据已下载！")

df3 = pd.merge(left=dataframe, right=pg_dataframe, how='left',
                   left_on='en_date', right_on='en_date')
df5 = df3.fillna(0)
df4 = df5.loc[(df5['cnum_x'] != df5['cnum_y'])]  # 取不同的值

list_time = []
for index,i in enumerate(df5['cnum_x']):
    # print(int(i)-int(df5['cnum_y'][index]))
    if int(i)-int(df5['cnum_y'][index])!=0 and df5['en_date'][index]>'20200101':
        print(df5['en_date'][index])
        list_time.append(df5['en_date'][index])
    else:
        pass

df4.to_csv('cnum.csv')
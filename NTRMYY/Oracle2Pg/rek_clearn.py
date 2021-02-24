# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: rek_clearn.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/20 13:07
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
     select
to_char(bi.enter_date,'yyyymmdd') as en_date,count(1) as cnum
from bms.BILL_ITEM bi
where
bi.rek_id is null
and to_char(bi.enter_date,'yyyymm')>='202001'
and to_char(bi.enter_date,'yyyymm')<'202101'
group by to_char(bi.enter_date,'yyyymmdd')
    '''
    db_cursor.execute(rek_id_sql)
    result = db_cursor.fetchall()
    dataframe = pd.DataFrame(result,columns=['en_date','cnum'])
    log.info("ORA对比数据已下载！")

with PgSQLContextManager() as pg_cursor:
    pg_rek_sql = '''

select
to_char(bi.enter_date,'yyyymmdd') as en_date,count(1) as cnum
from ods.his_bms_bill_item bi
where
bi.rek_id is null
and to_char(bi.enter_date,'yyyymm')>='202001'
and to_char(bi.enter_date,'yyyymm')<'202101'
group by to_char(bi.enter_date,'yyyymmdd')
    '''
    pg_cursor.execute(pg_rek_sql)
    pg_result = pg_cursor.fetchall()
    pg_dataframe = pd.DataFrame(pg_result,columns=['en_date','cnum'])
    log.info("PG对比数据已下载！")

df3 = pd.merge(left=dataframe, right=pg_dataframe, how='left',
                   left_on='en_date', right_on='en_date')
df4 = df3.loc[(df3['cnum_x'] != df3['cnum_y'])]  # 取不同的值

list_time= []
for i in df4['en_date']:
    list_time.append(i)

def loaditem(dta,targetpath):
    for i in dta:
        job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        log.info("任务开始日期：{}".format(i))
        with OracleSQLContextManager() as db_cursor:
            sql = '''select "ID","REK_ID","ITEM_ID","PAI_VISIT_ID","PATIENT_ID","VISIT_ID","ITEM_CLASS","ITEM_CODE","STANDARD_ITEM_CODE","ITEM_NAME","ITEM_SPEC","AMOUNT","UNIT_NAME","FACTOR","RETAIL_FACTOR","QUANTITY","UNIT_QUANTITY","EXEC_QUANTITY","SALES_PRICE","COSTS","CHARGES","CLASS_ON_RCPT","REFUND_FLAG","REL_REFUND_ID","APPLY_CLASS","APPLY_ID","ORDER_ID","DIAG_EMP_ID","DIAG_EMP_NAME","DIAG_BY","SERVICE_LOG_ORG","CHARGED_BY","ORDERED_BY","PERFORMED_BY","INSURANCE_TYPE","CHARGE_DATE","ENTER_DATE","INVOICE_PRINT_STATUS","BRANCH_NO","PERFORMED_DEVICE","SUBJ_CODE","OPERATOR","EXECUTOR","REMARK","CLINIC_ID","CURRENT_NURSING_UNIT","REFUND_APPLY_FLAG","SETTLE_STATUS","EXTERNAL_ID","PRETRANSACT_ID","IN_OUT_FLAG","ITEM_UNIQUE_CODE","INSUR_LEVEL_CODE","INSUR_LEVEL_NAME","PERMED","FREQNAME","DURATION","TREATMENT_GROUP","MEDUNITNAME","FREQUNITNAME","DURATIONUNITNAME","SELF_CHARGE_FLAG" from bms.BILL_ITEM
        where
        ENTER_DATE >=to_date('{date_i}','yyyymmdd')
        and ENTER_DATE<to_date('{date_i}','yyyymmdd')+1'''.format(date_i=i)
            db_cursor.execute(sql)
            result = db_cursor.fetchall()
            dataframe = pd.DataFrame(result)
            dataframe.to_csv(os.path.join(targetpath+"billitem"+str(i)+'.csv'),index=False,header=False)
            job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            total_use_time = (job_end_date - job_start_date).seconds
            log.info("时间：{i},总耗时：{total}".format(i=i,total=total_use_time))

n = 5
list_result = [list_time[i:i + n] for i in range(0, len(list_time), n)]
try:
    with ThreadPoolExecutor(max_workers=10) as t:
        obj_list=[]
        for i in range(len(list_result)):
            obj = t.submit(loaditem,list_result[i],r"C:\Users\CBH\PycharmProjects\Cenboom\newbill"+"\\" )
            obj_list.append(obj)
        for future in as_completed(obj_list):
            data = future.result()
except:
    t.shutdown()

import os
path = r"C:\Users\CBH\PycharmProjects\Cenboom\newbill - 副本"
for i in os.listdir(path):
    os.remove(os.path.join(path,i))

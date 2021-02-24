# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: BILL_ITEM_HISTORY.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/2 22:08
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
from NTRMYY.util.Dict_date import *
from concurrent.futures import ThreadPoolExecutor,as_completed
# dta = Get_Time_section_30(list_time=[],cycle_day=30)
# dta = ['20201201','20201211','20201221']
DATE = Get_Time_section_30(cycle_day=60)
log = Logger(r'C:\Users\CBH\Downloads\Detailed.log', logging.ERROR, logging.DEBUG)
def loaditem(dta,targetpath):
    for i in dta:
        job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        log.info("任务开始日期：{}".format(i))
        with OracleSQLContextManager() as db_cursor:
            sql = '''select "ID","REK_ID","ITEM_ID","PAI_VISIT_ID","PATIENT_ID","VISIT_ID","ITEM_CLASS","ITEM_CODE","STANDARD_ITEM_CODE","ITEM_NAME","ITEM_SPEC","AMOUNT","UNIT_NAME","FACTOR","RETAIL_FACTOR","QUANTITY","UNIT_QUANTITY","EXEC_QUANTITY","SALES_PRICE","COSTS","CHARGES","CLASS_ON_RCPT","REFUND_FLAG","REL_REFUND_ID","APPLY_CLASS","APPLY_ID","ORDER_ID","DIAG_EMP_ID","DIAG_EMP_NAME","DIAG_BY","SERVICE_LOG_ORG","CHARGED_BY","ORDERED_BY","PERFORMED_BY","INSURANCE_TYPE","CHARGE_DATE","ENTER_DATE","INVOICE_PRINT_STATUS","BRANCH_NO","PERFORMED_DEVICE","SUBJ_CODE","OPERATOR","EXECUTOR","REMARK","CLINIC_ID","CURRENT_NURSING_UNIT","REFUND_APPLY_FLAG","SETTLE_STATUS","EXTERNAL_ID","PRETRANSACT_ID","IN_OUT_FLAG","ITEM_UNIQUE_CODE","INSUR_LEVEL_CODE","INSUR_LEVEL_NAME","PERMED","FREQNAME","DURATION","TREATMENT_GROUP","MEDUNITNAME","FREQUNITNAME","DURATIONUNITNAME","SELF_CHARGE_FLAG" from bms.BILL_ITEM
        where
       ENTER_DATE >=trunc(sysdate-90,'mm')
and ENTER_DATE<trunc(sysdate-60,'mm')'''.format(date_i=i)
            db_cursor.execute(sql)
            result = db_cursor.fetchall()
            dataframe = pd.DataFrame(result)
            dataframe.to_csv(os.path.join(targetpath+"billitem"+str(i)+'.csv'),index=False,header=False)
            job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            total_use_time = (job_end_date - job_start_date).seconds
            log.info("时间：{i},总耗时：{total}".format(i=i,total=total_use_time))
    # list_a = dataframe.values.tolist()

plan = loaditem(['202010'],r'C:\Users\CBH\PycharmProjects\Cenboom\NTRMYY\Oracle2Pg')
file_path=r'C:\Users\CBH\PycharmProjects\Cenboom\billitem\billitem20201002.csv'
with open(file_path, 'r', encoding='utf-8') as f:
    df = f.read()
    print(df)
    f.close()


with PgSQLContextManager() as db_cursor:
    ver_sql = '''
       select
pid
from
pg_stat_activity
where
client_addr='192.168.12.101'
        '''
    db_cursor.execute(ver_sql)
    result = db_cursor.fetchall()
    print("long Runing job count:"+str(len(result)))
    for i in result:
        # print(i)
        with PgSQLContextManager() as db_cursor:
            terminate_sql = '''
            select pg_terminate_backend({id});
            '''.format(id=i[0])
            print("执行杀进程操作，oid号："+str(i[0]))
            db_cursor.execute(terminate_sql)
    print('success！total kill job:{}'.format(str(len(result))))
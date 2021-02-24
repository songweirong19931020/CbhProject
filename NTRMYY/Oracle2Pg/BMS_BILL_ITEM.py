# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: BMS_BILL_ITEM.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/12/31 10:07
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
# dta = Get_Time_section_30(list_time=[],cycle_day=30)
# dta = ['20201201','20201211','20201221']
log = Logger(r'C:\Users\CBH\Downloads\Detailed.log', logging.ERROR, logging.DEBUG)
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
    # list_a = dataframe.values.tolist()
# list_time = Get_Time_section_30(list_time=[], cycle_day=90)
list_time=['20201231']
n = 5
list_result = [list_time[i:i + n] for i in range(0, len(list_time), n)]
try:
    with ThreadPoolExecutor(max_workers=10) as t:
        obj_list=[]
        for i in range(len(list_result)):
            obj = t.submit(loaditem,list_result[i],r"C:\Users\CBH\PycharmProjects\Cenboom\billitem"+"\\" )
            obj_list.append(obj)
        for future in as_completed(obj_list):
            data = future.result()
except:
    t.shutdown()
# with PgSQLContextManager() as pg_cursor:
#     output = StringIO()
#     dataframe.to_csv(output, sep='\t', index=False, header=False)
#     output1 = output.getvalue()
#     table_name1 = 'ods.tmp_his_bms_bill_item_20201231'
#     pg_cursor.copy_from(StringIO(output1), table_name1)
# inputfile_dir = r'C:\Users\CBH\PycharmProjects\Cenboom\billitem'
# outputfile = r'C:\Users\CBH\PycharmProjects\Cenboom\billitem\total_bill.csv'
# for inputfile in os.listdir(inputfile_dir):
#     df1 = pd.read_csv(os.path.join(inputfile_dir,inputfile))
#     df1.to_csv(outputfile, mode='a', index=False, header=False)

def load_to_pg(pathname,target_tablename):
    for i in pathname:
        with PgSQLContextManager() as pg_cursor:
            log.info("任务{name}，开始！".format(name=i.split("\\")[-1]))
        #     truncate_sql = '''truncate table ods.tmp_his_bms_bill_item_20201231 where ENTER_DATE >=to_date('20201201','yyyymmdd')'''\
        # '''and ENTER_DATE<to_date('20201201','yyyymmdd')+1'''
        #     pg_cursor.execute(truncate_sql)
            job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            file_path = i
            with open(file_path, 'r', encoding='utf-8') as f:
                insert_sql = """COPY """+target_tablename+""" FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
        escape '\t',
        header true,
        quote '"')"""
                pg_cursor.copy_expert(insert_sql, f)
                job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                total_use_time = (job_end_date - job_start_date).seconds
                log.info("任务：{job},总耗时：{total}".format( job=i.split("\\")[-1],total=total_use_time))


# inputfile_dir = r'C:\Users\CBH\PycharmProjects\Cenboom\billitem'
# list_job=[]
# for inputfile in os.listdir(inputfile_dir):
#     print(inputfile)
#     list_job.append(os.path.join(inputfile_dir,inputfile))
#
# n = 5
# list_result = [list_job[i:i + n] for i in range(0, len(list_job), n)]
#
# for i in list_result:
#     print(i[0].split("\\")[-1])
# # for i in range(len(list_result)):
# #     print(list_result[i][0])
inputfile_dir = r'C:\Users\CBH\PycharmProjects\Cenboom\newbill'
list_job=[]
for inputfile in os.listdir(inputfile_dir):
    print(inputfile)
    list_job.append(os.path.join(inputfile_dir,inputfile))
n = 5
list_result = [list_job[i:i + n] for i in range(0, len(list_job), n)]
# with PgSQLContextManager() as pg_cursor:
    # truncate_sql = '''truncate table ods.tmp_his_bms_bill_item_20201231'''
    # pg_cursor.execute(truncate_sql)
try:
    with ThreadPoolExecutor(max_workers=8) as t:
        obj_list=[]
        for i in range(len(list_result)):
            obj = t.submit(load_to_pg,list_result[i],"ods.his_bms_bill_item" )
            obj_list.append(obj)
        for future in as_completed(obj_list):
            data = future.result()
except Exception as e:
    print(e)
    t.shutdown()
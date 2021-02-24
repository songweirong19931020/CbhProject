# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: ClearDataUpdate.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/20 10:35
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
 where to_char(k.rek_date,'yyyymm')< to_char(current_date,'yyyymm')
   group by to_char(bi.enter_date,'yyyymmdd')
    '''
    db_cursor.execute(rek_id_sql)
    result = db_cursor.fetchall()
    dataframe = pd.DataFrame(result,columns=['en_date','cnums'])
    log.info("ORA对比数据已下载！")

with PgSQLContextManager() as pg_cursor:
    pg_rek_sql = '''
     select to_char(bi.enter_date,'yyyymmdd') as en_date , sum(bi.charges) as cnum
        FROM ods.his_bms_rek k
      inner JOIN ods.his_bms_bill_item bi
        on k.id = bi.rek_id
     where  to_char(k.rek_date,'yyyymm')< to_char(current_date,'yyyymm')
       group by to_char(bi.enter_date,'yyyymmdd')
    '''
    pg_cursor.execute(pg_rek_sql)
    pg_result = pg_cursor.fetchall()
    pg_dataframe = pd.DataFrame(pg_result,columns=['en_date','cnums'])
    log.info("PG对比数据已下载！")


df3 = pd.merge(left=dataframe, right=pg_dataframe, how='left',
                   left_on='en_date', right_on='en_date')
# df4 = df3.loc[(df3['cnums_x'] != df3['cnums_y'])]  # 取不同的值
df5 = df3.fillna(0)
list_time = []
for index,i in enumerate(df5['cnums_x']):
    # print(int(i)-int(df5['cnums_x'][index]))
    if int(i)-int(df5['cnums_y'][index])!=0 and df5['en_date'][index]>'20200101':
        print(df5['en_date'][index])
        list_time.append(df5['en_date'][index])
    else:
        pass



def DeletePGResult(list_date):
    # de_list_id = ','.join(list_date)
    for i in list_date:
        with PgSQLContextManager() as pg_cursor:
            deletesql='''
            delete from ods.his_bms_bill_item
            where to_char(enter_date,'yyyymmdd') = '{list_date}'
            '''.format(list_date=i)
            log.info(deletesql)
            pg_cursor.execute(deletesql)
            log.info("数据已删除！")

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
list_time=['20200905']
# list_time=['20200104','20200120','20200305','20200312','20200317','20200323','20200324','20200326','20200406','20200407','20200408','20200409','20200416','20200611','20200712','20200806','20201101','20201102','20201103','20201104','20201105','20201106','20201107','20201108','20201109','20201110','20201111','20201112','20201113','20201114','20201115','20201116','20201117','20201118','20201119','20201120','20201121','20201122','20201123','20201124','20201125','20201126','20201127','20201128','20201129','20201130','20201201','20201202','20201203','20201204','20201205','20201206','20201207','20201208','20201209','20201210','20201211','20201212','20201213','20201214','20201215','20201216','20201217','20201218','20201219','20201220','20201221','20201222','20201223','20201224','20201225','20201226','20201227','20201228','20201229','20201230','20201231']
# for i in df4['s_end']:
#     list_time.append(i)

# delete = DeletePGResult(list_time)
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

log.info("开始插入数据！")
inputfile_dir = r'C:\Users\CBH\PycharmProjects\Cenboom\newbill'
list_job=[]
for inputfile in os.listdir(inputfile_dir):
    print(inputfile)
    list_job.append(os.path.join(inputfile_dir,inputfile))
n = 5
list_result = [list_job[i:i + n] for i in range(0, len(list_job), n)]
try:
    with ThreadPoolExecutor(max_workers=8) as t:
        obj_list=[]
        for i in range(len(list_result)):
            obj = t.submit(load_to_pg,list_result[i],"ods.his_bms_bill_item" )
            obj_list.append(obj)
        for future in as_completed(obj_list):
            data = future.result()
except Exception as e:
    log.info(e)
    t.shutdown()




with OracleSQLContextManager() as db_cursor:
 #    rek_id_sql = '''
 #  select to_char(bi.enter_date,'yyyymmdd') as en_date , sum(bi.charges) as cnum
 #    FROM bms.rek k
 #  inner JOIN bms.bill_item bi
 #    on k.id = bi.rek_id
 # where to_char(k.rek_date,'yyyymmdd')< to_char(current_date,'yyyymmdd')
 #   group by to_char(bi.enter_date,'yyyymmdd')
 #    '''

    rek_id_sql = '''
     SELECT
    to_char(bi.enter_date,'yyyymmdd') as s_end ,
       COUNT(*) as cnums,
       sum(bi.charges) medical_fees
    from bms.bill_item bi
    where   to_char(bi.enter_date,'yyyymmdd')< to_char(current_date,'yyyymmdd')
    group by to_char(bi.enter_date,'yyyymmdd')
    '''
    db_cursor.execute(rek_id_sql)
    result = db_cursor.fetchall()
    dataframe = pd.DataFrame(result,columns=['s_end','cnums','medical_fees'])
    log.info("ORA对比数据已下载！")


with PgSQLContextManager() as pg_cursor:
    # pg_rek_sql = '''
    # select to_char(bi.enter_date,'yyyymmdd') as en_date , sum(bi.charges) as cnum
    # FROM ods.his_bms_rek k
    # inner JOIN ods.his_bms_bill_item bi
    # on k.id = bi.rek_id
    # where  to_char(k.rek_date,'yyyymmdd')< to_char(current_date,'yyyymmdd')
    # group by to_char(bi.enter_date,'yyyymmdd')'''
    pg_rek_sql = '''
     SELECT
    to_char(bi.enter_date,'yyyymmdd') as s_end ,
       COUNT(*) as cnums,
       sum(bi.charges) medical_fees
    from ods.his_bms_bill_item bi
    where 
     to_char(bi.enter_date,'yyyymmdd')< to_char(current_date,'yyyymmdd')
    group by to_char(bi.enter_date,'yyyymmdd')
    '''
    pg_cursor.execute(pg_rek_sql)
    pg_result = pg_cursor.fetchall()
    pg_dataframe = pd.DataFrame(pg_result,columns=['s_end','cnums','medical_fees'])
    log.info("PG对比数据已下载！")


df3 = pd.merge(left=dataframe, right=pg_dataframe, how='left',
                   left_on='s_end', right_on='s_end')
df4 = df3.loc[(df3['cnums_x'] != df3['cnums_y'])]  # 取不同的值

df5 = df4.fillna(0)
list_time = []
for i in df5['s_end']:
    list_time.append(i)





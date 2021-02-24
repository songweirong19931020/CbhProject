# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Reduce_Find_Bykey.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/6 8:49
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
    select k.id,count(1)
    FROM bms.rek k
  left JOIN bms.bill_item bi
    on k.id = bi.rek_id
 where k.in_out_flag = 'I'
--    and k.rek_date >= to_date('2020-01-01', 'yyyy-mm-dd')
--    and k.rek_date < to_date('2020-11-30', 'yyyy-mm-dd') + 1
group by k.id
    '''
    db_cursor.execute(rek_id_sql)
    result = db_cursor.fetchall()
    dataframe = pd.DataFrame(result,columns=['rek_id','cnums'])
    log.info("ORA对比数据已下载！")

with PgSQLContextManager() as pg_cursor:
    pg_rek_sql = '''
    select k.id,count(1)
    FROM ods.his_bms_rek k
  left JOIN ods.his_bms_bill_item bi
    on k.id = bi.rek_id
 where k.in_out_flag = 'I'
--    and k.rek_date >= to_date('2020-01-01', 'yyyy-mm-dd')
--    and k.rek_date < to_date('2020-11-30', 'yyyy-mm-dd') + 1
group by k.id
    '''
    pg_cursor.execute(pg_rek_sql)
    pg_result = pg_cursor.fetchall()
    pg_dataframe = pd.DataFrame(pg_result,columns=['rek_id','cnums'])
    log.info("PG对比数据已下载！")


def DeletePGResult(rek_id_list):
    de_rek_id = ','.join(rek_id_list)
    with PgSQLContextManager() as pg_cursor:
        deletesql='''
        delete from ods.his_bms_bill_item
        where rek_id in ({rek_list})
        '''.format(rek_list=de_rek_id)
        log.info(deletesql)
        pg_cursor.execute(deletesql)
        log.info("数据已删除！")
def LoadORAResult(targetpath,rek_id_list):
    load_rek_id = ','.join(rek_id_list)
    loadsql='''
    select "ID","REK_ID","ITEM_ID","PAI_VISIT_ID","PATIENT_ID","VISIT_ID","ITEM_CLASS","ITEM_CODE","STANDARD_ITEM_CODE","ITEM_NAME","ITEM_SPEC","AMOUNT","UNIT_NAME","FACTOR","RETAIL_FACTOR","QUANTITY","UNIT_QUANTITY","EXEC_QUANTITY","SALES_PRICE","COSTS","CHARGES","CLASS_ON_RCPT","REFUND_FLAG","REL_REFUND_ID","APPLY_CLASS","APPLY_ID","ORDER_ID","DIAG_EMP_ID","DIAG_EMP_NAME","DIAG_BY","SERVICE_LOG_ORG","CHARGED_BY","ORDERED_BY","PERFORMED_BY","INSURANCE_TYPE","CHARGE_DATE","ENTER_DATE","INVOICE_PRINT_STATUS","BRANCH_NO","PERFORMED_DEVICE","SUBJ_CODE","OPERATOR","EXECUTOR","REMARK","CLINIC_ID","CURRENT_NURSING_UNIT","REFUND_APPLY_FLAG","SETTLE_STATUS","EXTERNAL_ID","PRETRANSACT_ID","IN_OUT_FLAG","ITEM_UNIQUE_CODE","INSUR_LEVEL_CODE","INSUR_LEVEL_NAME","PERMED","FREQNAME","DURATION","TREATMENT_GROUP","MEDUNITNAME","FREQUNITNAME","DURATIONUNITNAME","SELF_CHARGE_FLAG" from bms.BILL_ITEM
        where
        rek_id in ({rek_list})
    '''.format(rek_list=load_rek_id)
    with OracleSQLContextManager() as db_cursor1:
        log.info(loadsql)
        db_cursor1.execute(loadsql)
        result_ora = db_cursor1.fetchall()
        dataframe_result = pd.DataFrame(result_ora)
        dataframe_result.to_csv(os.path.join(targetpath + "billitemrek.csv"), index=False, header=False)
        log.info("数据已下载成功！")
def CopyLoadToPg(file_path,target_tablename):
    with PgSQLContextManager() as pg_cursor:
        log.info("任务{name}，开始！".format(name=target_tablename))
        #     truncate_sql = '''truncate table ods.tmp_his_bms_bill_item_20201231 where ENTER_DATE >=to_date('20201201','yyyymmdd')'''\
        # '''and ENTER_DATE<to_date('20201201','yyyymmdd')+1'''
        #     pg_cursor.execute(truncate_sql)
        job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        with open(file_path, 'r', encoding='utf-8') as f:
            insert_sql = """COPY """ + target_tablename + """ FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
    escape '\t',
    header true,
    quote '"')"""
            pg_cursor.copy_expert(insert_sql, f)
            job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            total_use_time = (job_end_date - job_start_date).seconds
            log.info("任务：{job},总耗时：{total}".format(job=target_tablename, total=total_use_time))


if __name__ == '__main__':
    # 取没有关联后的结果
    df3 = pd.merge(left=dataframe, right=pg_dataframe, how='left',
                   left_on='rek_id', right_on='rek_id')
    df4 = df3.loc[(df3['cnums_x'] != df3['cnums_y'])]  # 取不同的值
    rek_list = []
    for i in df4['rek_id']:
        rek_list.append("'" + str(i) + "'")
    delete_revers = DeletePGResult(rek_list)
    loaddata =LoadORAResult(targetpath=r'C:\Users\CBH\PycharmProjects\Cenboom\NTRMYY'+"\\",rek_id_list=rek_list)
    copyinsert = CopyLoadToPg(r'C:\Users\CBH\PycharmProjects\Cenboom\NTRMYY\billitemrek.csv','ods.his_bms_bill_item')
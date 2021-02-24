# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: ba_medical_record.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/15 15:02
# ---
from NTRMYY.util.ba_oracle import *
from NTRMYY.util.account import *
import pandas as pd
from NTRMYY.util.Dict_date import *
import numpy as np
import itertools
import multiprocessing
import datetime as dt
from io import StringIO
# with BaOracleSQLContextManager() as db_cursor:
#     sql = '''select
#        brxh,bah,brxm,xb,zycs,csrq,nl,hyxh,zyxh,sfzh,gzdw,dwdh,dwyb,jtzz,zzyb,gxrxm,gxxh,gxrzz,gxrdh,xxxh,rh,qjcs,cgcs,bazl,zkys,zkhs,rytj,kzrbh,zrysbh,zzysbh,zyysbh,jxysbh,sxysbh,ryksdm,ryrq,cyksdm,cyrq,zyts,zfy,cyzzd,zgqk,rcfhbz,mcfhbz,sfsj,rybs,cybs,lcybl,fsybl,sqysh,jkkh,zkrq,lyfs,jsyljg1,zryjh,zrymd,ryqhmsj,ryhhmsj,rybq,ywgmbz,zrhsbh,kzrxm,zrysxm,zzysxm,zyysxm,jxysxm,sxysxm,cyzzdmc,dbzgl,lcljgl,lower(utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(INPUT_STRING => bah || zycs))) as md5
# from MHIS.VIEW_MEDICAL_RECORD
# WHERE
# CYRQ >=to_date('20200301','yyyymmdd')
# and CYRQ <to_date('20200301','yyyymmdd')+1'''
#     db_cursor.execute(sql)
#     result = db_cursor.fetchall()
#     data1 = pd.DataFrame(result)
#     data1.to_csv(r"C:\Users\CBH\Desktop\DATA\outp_visit_2.csv", index=None)
#
# with PgSQLContextManager() as pg_cursor:
#     file_path = r"D:\MHIS_VIEW_MEDICAL_RECORD.csv"
#     with open(file_path, 'r', encoding='utf-8') as f:
#         insert_sql = """COPY ods.tmp_view_medical_record FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
#  escape '\t',
#  header true,
#  quote '"')"""
#         pg_cursor.copy_expert(insert_sql, f)



def querry(qj1,num):
    for i in range(0,len(qj1)//2):
        print(qj1[i])
        with BaOracleSQLContextManager() as db_cursor:
            sql = '''
                        select brxh,
       bah,
       brxm,
       xb,
       zycs,
       csrq,
       nl,
       hyxh,
       zyxh,
       sfzh,
       gzdw,
       dwdh,
       dwyb,
       jtzz,
       zzyb,
       gxrxm,
       gxxh,
       gxrzz,
       gxrdh,
       xxxh,
       rh,
       qjcs,
       cgcs,
       bazl,
       zkys,
       zkhs,
       rytj,
       kzrbh,
       zrysbh,
       zzysbh,
       zyysbh,
       jxysbh,
       sxysbh,
       ryksdm,
       ryrq,
       cyksdm,
       cyrq,
       zyts,
       zfy,
       zgqk,
       rcfhbz,
       mcfhbz,
       sfsj,
       rybs,
       cybs,
       lcybl,
       fsybl,
       sqysh,
       jkkh,
       trunc(zkrq,'dd') as zkrq,
       lyfs,
       jsyljg1,
       zryjh,
       zrymd,
       ryqhmsj,
       ryhhmsj,
       rybq,
       ywgmbz,
       zrhsbh,
       trunc(sysdate,'dd') insert_time,
       lower(utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(INPUT_STRING => bah || zycs))) as md5,
       cyzzd,
       kzrxm,
       zrysxm,
       zzysxm,
       zyysxm,
       jxysxm,
       sxysxm,
       cyzzdmc,
       dbzgl,
       lcljgl
from MHIS.VIEW_MEDICAL_RECORD
WHERE
CYRQ >=to_date('{day_id}','yyyymmdd')
and CYRQ <to_date('{day_id}','yyyymmdd')+1'''.format(day_id=qj1[i])
            db_cursor.execute(sql)
            result1 = db_cursor.fetchall()
            data1 = pd.DataFrame(result1)
            # data1 = data1.fillna(0)
            data1.to_csv(r"C:\Users\CBH\Desktop\DATA\BA_MEDICAL_"+str(num)+".csv", index=None)
        with PgSQLContextManager() as pg_cursor:
            file_path = r"C:\Users\CBH\Desktop\DATA\BA_MEDICAL_"+str(num)+".csv"
            with open(file_path, 'r', encoding='utf-8') as f:
                insert_sql = """COPY ods.tmp_patient_medical_record_20200915 FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
        escape '\t',
        header true,
        quote '"')"""
                pg_cursor.copy_expert(insert_sql, f)


def querry1(qj2,num):
    for i in range(len(qj2)//2,len(qj2)):
        print(qj2[i])
        with BaOracleSQLContextManager() as db_cursor:
            sql = '''
            select brxh,
       bah,
       brxm,
       xb,
       zycs,
       csrq,
       nl,
       hyxh,
       zyxh,
       sfzh,
       gzdw,
       dwdh,
       dwyb,
       jtzz,
       zzyb,
       gxrxm,
       gxxh,
       gxrzz,
       gxrdh,
       xxxh,
       rh,
       qjcs,
       cgcs,
       bazl,
       zkys,
       zkhs,
       rytj,
       kzrbh,
       zrysbh,
       zzysbh,
       zyysbh,
       jxysbh,
       sxysbh,
       ryksdm,
       ryrq,
       cyksdm,
       cyrq,
       zyts,
       zfy,
       zgqk,
       rcfhbz,
       mcfhbz,
       sfsj,
       rybs,
       cybs,
       lcybl,
       fsybl,
       sqysh,
       jkkh,
       trunc(zkrq,'dd') as zkrq,
       lyfs,
       jsyljg1,
       zryjh,
       zrymd,
       ryqhmsj,
       ryhhmsj,
       rybq,
       ywgmbz,
       zrhsbh,
       trunc(sysdate,'dd') insert_time,
       lower(utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(INPUT_STRING => bah || zycs))) as md5,
       cyzzd,
       kzrxm,
       zrysxm,
       zzysxm,
       zyysxm,
       jxysxm,
       sxysxm,
       cyzzdmc,
       dbzgl,
       lcljgl
from MHIS.VIEW_MEDICAL_RECORD
WHERE
CYRQ >=to_date('{day_id}','yyyymmdd')
and CYRQ <to_date('{day_id}','yyyymmdd')+1'''.format(day_id=qj2[i])
            db_cursor.execute(sql)
            result = db_cursor.fetchall()
            data1 = pd.DataFrame(result)
            # data1 = data1.fillna(0)
            data1.to_csv(r"C:\Users\CBH\Desktop\DATA\BA_MEDICAL_"+str(num)+".csv", index=None)
        with PgSQLContextManager() as pg_cursor:
            file_path = r"C:\Users\CBH\Desktop\DATA\BA_MEDICAL_"+str(num)+".csv"
            with open(file_path, 'r', encoding='utf-8') as f:
                insert_sql = """COPY ods.tmp_patient_medical_record_20200915 FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
        escape '\t',
        header true,
        quote '"')"""
                pg_cursor.copy_expert(insert_sql, f)



if __name__ == '__main__':
    list_time = Get_Time_All(list_time=[])
    p1 = multiprocessing.Process(target=querry,args=(list_time,1,))
    p2 = multiprocessing.Process(target=querry1,args=(list_time,2,))
    p1.start()
    p2.start()
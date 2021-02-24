# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: drgs_auto_write.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/16 15:41
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

with PgSQLContextManager() as pg_cursor:
    select_sql='''
    select
foo.one_class_name
   from (select distinct one_class_name ,
    substring(one_class_name  from '\d+')::int as rownum
    from   ods.dim_lv_main_diag_oper_info
where type_name='重点疾病')foo
order by foo.rownum asc
    '''
    pg_cursor.execute(select_sql)
    result = pg_cursor.fetchall()

one_class_name=[]
for i in range(len(result)):
    one_class_name.append(result[i][0])

for txt in one_class_name:
    format_text='''
     delete from dw.dw_lv_main_diag_patient_info_m where month_id = to_char(v_StDate_to,'yyyy-mm') and drgs_name='{one_class_name}';
	INSERT INTO dw.dw_lv_main_diag_patient_info_m (
		month_id,
		st_date,
		brxh,
		drgs_name,
		return_in_2to15,
		return_in_16to31,
		insert_date
	)
    ---{one_class_name}
    select to_char(t.cyrq,'yyyy-mm')  AS month_id,
                 date(cyrq) AS st_date,
                 t.brxh,
                 '{one_class_name}' AS drgs_name,
                 null return_in_2to15,
                 null return_in_16to31,
                 now()
      from ods.ba_patient_medical_record t
      where t.cyrq>= v_StDate_to
		AND t.cyrq < v_StDate_to  + interval '1 month'
            AND EXISTS(SELECT 1 FROM ods.ba_patient_diag_info dig
               WHERE dig.brxh=t.brxh
               AND dig.main_diag='1'
               AND EXISTS (SELECT 1 FROM ods.dim_lv_main_diag_oper_info h
                           WHERE h.icd_code=dig.diagdiseasecode
                                 AND h.type_name='重点疾病'
                                 AND h.one_class_name='{one_class_name}'
                                 AND h.compatible_type='1'
                                 AND h.icd_type='ICD10'));
    '''.format(one_class_name=txt)
    print(format_text)
    with open('job_d.sql','a+',encoding='utf-8') as f:
        f.write(format_text)
        f.close()



with PgSQLContextManager() as pg_cursor:
    select_sql='''
        select foo.one_class_name,foo.two_class_name
from
(select  distinct one_class_name,two_class_name ,
                 substring(one_class_name  from '\d+')::int as rownum from   ods.dim_lv_main_diag_oper_info
where type_name='重点手术' and two_class_name is  null
    )foo
order by foo.rownum asc
    '''
    pg_cursor.execute(select_sql)
    result = pg_cursor.fetchall()

one_class_name=[]
for i in range(len(result)):
    one_class_name.append(result[i])

for i in one_class_name:
    print(i[0])

for oper in one_class_name:
    oper_format = '''
      delete from dw.dw_lv_main_oper_patient_info_m where month_id = to_char(v_StDate_to,'yyyy-mm') and drgs_name='{one_class_name}'
      and drgs_name_child = '{two_class_name}';
	INSERT INTO dw.dw_lv_main_oper_patient_info_m (
		month_id,
		st_date,
		brxh,
		drgs_name,
	    drgs_name_child,
		return_in_2to15,
		return_in_16to31,
	    no_plan_return_oper,
		insert_date
	)
	---父：{one_class_name}；子：{two_class_name}
    	select
 to_char(t.cyrq,'yyyy-mm')  AS month_id,
		     date(cyrq) AS st_date,
		     t.brxh,
		     '{one_class_name}' AS drgs_name,
	        '{two_class_name}' as drgs_name_child,
		     null return_in_2to15,
		     null return_in_16to31,
             null no_plan_return_oper,
		     now()
FROM ods.ba_patient_medical_record t
WHERE t.cyrq>=  v_StDate_to
AND t.cyrq < v_StDate_to + interval '1 month'
AND EXISTS(SELECT 1 FROM ods.ba_patient_opertion_info o
           WHERE o.brxh=t.brxh
           AND EXISTS (SELECT 1 FROM ods.dim_lv_main_diag_oper_info h
                        WHERE h.icd_code=o.surgerycode
                             AND h.type_name='重点手术'
                             AND h.one_class_name='{one_class_name}'
                             AND h.two_class_name='{two_class_name}'
                             AND h.compatible_type='1'
                             AND h.icd_type='ICD9'))
AND EXISTS(SELECT 1 FROM ods.ba_patient_diag_info  dig
           WHERE dig.brxh=t.brxh
           AND dig.main_diag='1'
           AND EXISTS (SELECT 1 FROM ods.dim_lv_main_diag_oper_info h
                       WHERE h.icd_code=dig.diagdiseasecode
                             AND h.type_name='重点手术'
                             AND h.one_class_name='{one_class_name}'
                             AND h.compatible_type='1'
                             AND h.icd_type='ICD10'));
    '''.format(one_class_name=oper[0],two_class_name=oper[1])
    print(oper_format)
    with open('job_a.sql','a+',encoding='utf-8') as f:
        f.write(oper_format)
        f.close()
#is null
for oper in one_class_name:
    oper_format = '''
      delete from dw.dw_lv_main_oper_patient_info_m where month_id = to_char(v_StDate_to,'yyyy-mm') and drgs_name='{one_class_name}';
	INSERT INTO dw.dw_lv_main_oper_patient_info_m (
		month_id,
		st_date,
		brxh,
		drgs_name,
	    drgs_name_child,
		return_in_2to15,
		return_in_16to31,
	    no_plan_return_oper,
		insert_date
	)
	---父：{one_class_name}；子：{two_class_name}
    	select
 to_char(t.cyrq,'yyyy-mm')  AS month_id,
		     date(cyrq) AS st_date,
		     t.brxh,
		     '{one_class_name}' AS drgs_name,
	        '{one_class_name}' as drgs_name_child,
		     null return_in_2to15,
		     null return_in_16to31,
             null no_plan_return_oper,
		     now()
FROM ods.ba_patient_medical_record t
WHERE t.cyrq>=  v_StDate_to
AND t.cyrq < v_StDate_to + interval '1 month'
AND EXISTS(SELECT 1 FROM ods.ba_patient_opertion_info o
           WHERE o.brxh=t.brxh
           AND EXISTS (SELECT 1 FROM ods.dim_lv_main_diag_oper_info h
                        WHERE h.icd_code=o.surgerycode
                             AND h.type_name='重点手术'
                             AND h.one_class_name='{one_class_name}'
                             AND h.compatible_type='1'
                             AND h.icd_type='ICD9'));
    '''.format(one_class_name=oper[0],two_class_name=oper[1])
    print(oper_format)
    with open('job_b.sql','a+',encoding='utf-8') as f:
        f.write(oper_format)
        f.close()
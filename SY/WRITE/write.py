# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: write.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/10/19 10:49
# ---
import os,sys
condition_code = [
'A31',
'A3',
'A2',
'A4',
'A9',
'A7',
'A8',
'A10',
'A11',
]
condition_name = [
'材料费',
'化验费',
'检查费',
'治疗费',
'床位费',
'护理费',
'手术费',
'诊疗费',
'输血费',


]
kpi_code = [
'DI1004',
'DI1005',
'DI1006',
'DI1007',
'DI1008',
'DI1009',
'DI1010',
'DI1011',
'DI1012',
]
for i in range(len(condition_code)):
    # print(i)
    sql_context = '''
    select 
        '{kpi_code}',
        coalesce(sum(t.charges),0),
        t.patient_id,
        t.visit_id,
        t.pai_visit_id,
        now(),
       '{condition_name}',
       date(t.enter_date) AS st_date
     from ods.his_bms_bill_item t
     left join ods.his_pts_pai_visit t1 on t.pai_visit_id = t1.pai_visit_id
     where t.enter_date >= v_StDate_to
       and t.enter_date <  v_StDate_to+1
       and t.in_out_flag = 'I' --只统计住院患者
       and t.class_on_rcpt = '{condition_code}'
       and t.charges<>0 
     group by date(t.enter_date),
         t.patient_id,
         t.visit_id,
         t.pai_visit_id
         having coalesce(sum(t.charges),0)<>0 ;
    '''.format(kpi_code = kpi_code[i],condition_name=condition_name[i],
               condition_code=condition_code[i])
    sqk_model = '''
    
        create function dwd.fun_dwd_{kpi_code}_d(v_start_date character varying, v_end_date character varying) returns character varying
        language plpgsql
    as
    
        /***
        函数名称：住院患者患者{condition_name}
            作用：统计某天住院患者{condition_name}  
          开发人：leslie 2020-08-17
        命名规范：FUN_模型层级(DWD或者DW)_KPI编码_日期类型D或者M，D表示按天统计，M表示按月统计
         KPI编码：DI1001  根据原子指标编码规划来的
            入参：v_start_date，v_end_date  格式均为yyyymmdd，可以一次运行多天的数据
        ***/
        
        DECLARE
          v_StDate_to   DATE;
          v_date_f DATE;
          v_date_t DATE;
         BEGIN
            v_date_f := to_date(v_start_date, 'yyyymmdd');
            v_date_t := to_date(v_end_date, 'yyyymmdd'); 
         WHILE v_date_f <= v_date_t LOOP
           v_date_f := v_date_f +1;
           v_StDate_to := v_date_f -1;
        delete from dwd.dwd_inp_income_d where st_date = v_StDate_to and key = '{kpi_code}';
     
      INSERT into dwd.dwd_inp_income_d(key,value,patient_id,visit_id,pai_visit_id,insert_date,
                        remark,st_date) 
    {sql_context}
     
          END LOOP;
           RETURN 'SUCCESS';
        END;
    '''.format(sql_context=sql_context,condition_name=condition_name[i],kpi_code=kpi_code[i])

    print(sqk_model)
    d = r'D:\Sbh\十堰\job_down'
    file = '''fun_dwd_{kpi_code}_d'''.format(kpi_code=kpi_code[i])
    with open(os.path.join(d,file)+'.sql','a+', encoding='utf-8') as f:
        str = sqk_model
        f.write(str)





import os,sys

for i in os.listdir(r'D:\Sbh\十堰\job_down'):
    # print(i)
    path = r'D:\Sbh\十堰\job_down'
    # with open(r'D:\Sbh\十堰\job_down\all.sql','a+',encoding='utf-8') as f:
    with open(os.path.join(path,i),'r',encoding='utf-8') as f:
        data = f.read()
        print(data)
        with open(r'D:\Sbh\十堰\job_down\all111.sql', 'a+', encoding='utf-8') as g:
            g.write(data)
            g.close()
        f.close()

# for i in os.listdir(r'D:\Sbh\十堰\job_down'):
#     print('drop function'+i)


drop_sql = '''
drop function dwd."fun_dwd_DI0003_d";
drop function dwd."fun_dwd_DI0006_d";
drop function dwd."fun_dwd_DI0007_d";
drop function dwd."fun_dwd_DI0008_d";
drop function dwd."fun_dwd_DI0009_d";
drop function dwd."fun_dwd_DI0010_d";
drop function dwd."fun_dwd_DI0011_d";
drop function dwd."fun_dwd_DI0012_d";
drop function dwd."fun_dwd_DI0013_d";
drop function dwd."fun_dwd_DI0014_d";
drop function dwd."fun_dwd_DI0015_d";
drop function dwd."fun_dwd_DI0016_d";
drop function dwd."fun_dwd_DI0017_d";
drop function dwd."fun_dwd_DI0018_d";
drop function dwd."fun_dwd_DI0019_d";
drop function dwd."fun_dwd_DI0020_d";
drop function dwd."fun_dwd_DI0021_d";
drop function dwd."fun_dwd_DI1001_d";
drop function dwd."fun_dwd_DI1002_d";
drop function dwd."fun_dwd_DI1003_d";
drop function dwd."fun_dwd_DU9001_d";
drop function dwd."fun_dwd_DU9002_d";
drop function dwd."fun_dwd_DI0001_d";
drop function dwd."fun_dwd_DI0002_d";
drop function dwd."fun_dwd_DI1001_d";
drop function dwd."fun_dwd_DI1004_d";
drop function dwd."fun_dwd_DI1005_d";
drop function dwd."fun_dwd_DI1006_d";
drop function dwd."fun_dwd_DI1007_d";
drop function dwd."fun_dwd_DI1008_d";
drop function dwd."fun_dwd_DI1009_d";
drop function dwd."fun_dwd_DI1010_d";
drop function dwd."fun_dwd_DI1011_d";
drop function dwd."fun_dwd_DI1012_d";
'''
import os,sys
path = r'D:\Sbh\十堰\job_down'
for i in os.listdir(path):
    # print(os.path.join(path,i))
    with open(os.path.join(path, i), 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
        with PgSQLContextManager() as db_cursor:
            sql = data
            db_cursor.execute(sql)
        f.close()


import re
def replaceStr(file):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        print(str)
        old = '/***'
        new = '$$  /***'
        # str1 = re.sub('/***','$$ /***', str)
        str1 = re.sub(old,new, str)
        with open(file,'w', encoding='utf-8') as f:
            f.write(str1)
import os,sys
files = os.listdir(r'D:\Sbh\十堰\job_down')
for f in files:
    print(f)
    print(os.path.join('D:\Sbh\十堰\job_down',f))
    replaceStr(os.path.join('D:\Sbh\十堰\job_down',f))





import os,sys,re
path = r'D:\Sbh\十堰\job_down'
new_path = r'D:\Sbh\十堰\conplete'
for i in os.listdir(path):
    # print(os.path.join(path,i))
    with open(os.path.join(path, i), 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.replace('/***','$$ /***')
        data = data.replace('END;','END;    $$;')
        print(data)
        with open(os.path.join(new_path,i)+'.sql','a+', encoding='utf-8') as g:
            g.write(data)
            g.close()
        f.close()
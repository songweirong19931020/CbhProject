# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: oper.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/11 8:53
# ---
import os,sys
oper_name = ["1.髋、膝关节置换术",
"2.椎板切除术或脊柱融合相关手术",
"3.胰腺切除手术",
"4.食管切除手术",
"5.腹腔镜下胆囊切除术",
"6.冠状动脉旁路移植术（CABG）",
"7.经皮冠状动脉介入治疗（PCI）",
"8.颅、脑手术",
"9.子宫切除术",
"10.剖宫产",
"11.阴道分娩",
"12.乳腺手术",
"13.肺切除术",
"14.胃切除术",
"15.直肠切除术",
"16.肾与前列腺相关手术",
"17.血管内修补术",
"18.恶性肿瘤手术",]

oper_mini_name = ["18.1 甲状腺",
"18.2 喉",
"18.3 肺",
"18.4 食管",
"18.5 胃",
"18.6 肝",
"18.7 结肠",
"18.8 胰",
"18.9 乳腺",
"18.10 肾",
"18.11 前列腺",
"18.12 膀胱",
"18.13 输卵管-卵癌",
"18.14 子宫",
"18.15 淋巴结",]

for i in oper_name:
    sql_demo = '''
     delete from dw.dw_lv_main_oper_patient_info_m where month_id = to_char(v_StDate_to,'yyyy-mm') and drgs_name='{one_class_nam}';
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
      ---父：{one_class_nam}；子：{one_class_nam}
          select to_char(t.cyrq,'yyyy-mm')  AS month_id,
             date(cyrq) AS st_date,
             t.brxh
             '{one_class_nam}' AS drgs_name,
              '{one_class_nam}' as drgs_name_child,
             null return_in_2to15,
             null return_in_16to31,
                 null no_plan_return_oper,
             now()
      from ods.mris_patient_medical_record t
      where t.cyrq>= v_StDate_to
       AND t.cyrq < v_StDate_to  + interval '1 month'
          and  EXISTS(SELECT 1 FROM ods.mris_patient_opertion_info op
               WHERE op.brxh=t.brxh
              AND EXISTS (SELECT 1 FROM ods.dim_lv_main_oper_info h
                           WHERE h.icd_code=op.surgerycode
                                 AND h.one_class_name='{one_class_nam}'
                                 AND h.icd_type='ICD9'));
    '''.format(one_class_nam=i)
    print(sql_demo)
    with open('oper.sql','a+',encoding='utf-8') as f:
        f.write(sql_demo)
        f.close()


for i in oper_mini_name:
    sql_grgs = '''
     delete from dw.dw_lv_main_oper_patient_info_m where month_id = to_char(v_StDate_to,'yyyy-mm') and 
     and drgs_name = '18.恶性肿瘤手术' and drgs_name_child='{two_class_name}';
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
---父：18.恶性肿瘤手术；子：{two_class_name}
select
 to_char(t.cyrq,'yyyy-mm')  AS month_id,
         date(cyrq) AS st_date,
         t.brxh,
         '18.恶性肿瘤手术' AS drgs_name,
          '{two_class_name}' as drgs_name_child,
         null return_in_2to15,
         null return_in_16to31,
             null no_plan_return_oper,
         now()
FROM ods.mris_patient_medical_record t
WHERE t.cyrq>=  v_StDate_to
AND t.cyrq < v_StDate_to + interval '1 month'
and EXISTS(SELECT 1 FROM ods.mris_patient_opertion_info o
           WHERE o.brxh=t.brxh
           AND EXISTS (SELECT 1 FROM ods.dim_lv_main_oper_info h
                        WHERE h.icd_code=o.surgerycode
                             AND h.one_class_name='18.恶性肿瘤手术'
                             AND h.two_class_name='{two_class_name}'
                             AND h.icd_type='ICD9'))
AND EXISTS(SELECT 1 FROM ods.mris_patient_diag_info  dig
           WHERE dig.brxh=t.brxh
           AND dig.main_diag='1'
           AND EXISTS (SELECT 1 FROM ods.dim_lv_main_oper_info h
                       WHERE h.icd_code=dig.diagdiseasecode
                             AND h.one_class_name='18.恶性肿瘤手术'
                             AND h.icd_type='ICD10'));
    '''.format(two_class_name=i)
    print(sql_grgs)
    with open('oper_mini.sql','a+',encoding='utf-8') as f:
        f.write(sql_grgs)
        f.close()






drgs_list = ['10.结节性甲状腺肿',
'11.急性阑尾炎伴弥漫性腹膜炎及脓肿 ',
'12.前列腺增生',
'13.肾衰竭',
'14.成人败血症',]

for i in drgs_list:
    sql_drgs = '''
    delete from dw.dw_lv_main_diag_patient_info_m where month_id = to_char(v_StDate_to,'yyyy-mm') and drgs_name='{drgs}';
  INSERT INTO dw.dw_lv_main_diag_patient_info_m (
    month_id,
    st_date,
    brxh,
    drgs_name,
    return_in_2to15,
    return_in_16to31,
    insert_date
  )
  ---{drgs}
select to_char(t.cyrq,'yyyy-mm')  AS month_id,
                 date(cyrq) AS st_date,
                 t.brxh,
                 '{drgs}' AS drgs_name,
                 null return_in_2to15,
                 null return_in_16to31,
                 now()
      from ods.mris_patient_medical_record t
      where 
      t.cyrq >= v_StDate_to
  AND t.cyrq < v_StDate_to + interval '1 month'
  and EXISTS(SELECT 1 FROM ods.mris_patient_diag_info dig
               WHERE dig.brxh=t.brxh
               AND dig.main_diag='1'
               AND EXISTS (SELECT 1 FROM ods.dim_lv_main_diag_info h
                           WHERE h.icd_code=dig.diagdiseasecode
                                 AND h.one_class_name='{drgs}'
                                 AND h.icd_type='ICD10'))
              AND NOT EXISTS (select 1 from dwd.DWD_INP_MEDICAL_D med
                              where med.patient_id = t.bah 
                                    and med.visit_id = t.zycs and key in ('DI0028','DI0027');
    '''.format(drgs=i)
    print(sql_drgs)
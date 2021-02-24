# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: 7.1.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/26 9:46
# ---
level_code = [
'LV00704010104',
'LV00704010204',
'LV00704010304',
'LV00704010404',
'LV00704010504',
'LV00704010604',
'LV00704010704',
'LV00704010804',
'LV00704010904',
'LV00704011004',
'LV00704011104',
'LV00704011204',
'LV00704011304',
'LV00704011404',
'LV00704011504',
'LV00704011604',
'LV00704011704',

]
l_name = [
' 急性心肌梗死病种期内31 日内再住院率',
' 充血性心力衰竭病种期内31 日内再住院率',
' 脑出血和脑梗死病种期内31 日内再住院率',
' 创伤性颅脑损伤病种期内31 日内再住院率',
' 消化道出血（无并发症）病种期内31 日内再住院率',
' 累及身体多个部位的损伤病种期内31 日内再住院率',
' 成人细菌性肺炎（无并发症）病种期内31 日内再住院率',
' 慢性阻塞性肺疾病病种期内31 日内再住院率',
' 糖尿病伴短期与长期合并症病种期内31 日内再住院率',
'结节性甲状腺肿病种期内31 日内再住院率',
'急性阑尾炎伴弥漫性腹膜炎及脓肿 病种期内31 日内再住院率',
'前列腺增生病种期内31 日内再住院率',
'肾衰竭病种期内31 日内再住院率',
'成人败血症病种期内31 日内再住院率',
'成人高血压病病种期内31 日内再住院率',
'急性胰腺炎病种期内31 日内再住院率',
'恶性肿瘤化学治疗病种期内31 日内再住院率',
]
condition = [
'1. 急性心肌梗死',
'2. 充血性心力衰竭',
'3. 脑出血和脑梗死',
'4. 创伤性颅脑损伤',
'5. 消化道出血（无并发症）',
'6. 累及身体多个部位的损伤',
'7. 成人细菌性肺炎（无并发症）',
'8. 慢性阻塞性肺疾病',
'9. 糖尿病伴短期与长期合并症',
'10.结节性甲状腺肿',
'11.急性阑尾炎伴弥漫性腹膜炎及脓肿 ',
'12.前列腺增生',
'13.肾衰竭',
'14.成人败血症',
'15.成人高血压病',
'16.急性胰腺炎',
'17.恶性肿瘤化学治疗',
]

for index,i in enumerate(level_code):
    # print(i)
    sql = '''
    ---{name}
delete
from dw.level_master_m
where month_id = to_char(v_StDate_to, 'yyyy-mm')
  and level_code = '{code}';
insert into dw.level_master_m
select to_char(v_StDate_to, 'yyyy-mm'),
       '{code}'                                                        as level_code,
        COALESCE(round((sum(case when t1.return_in_1to31 = '1' then 1 end) /count(1))*100,5),0)  as level_value,
       now()                                                            as update_time,
        COALESCE(round((sum(case when t1.return_in_1to31 = '1' then 1 end) /count(1))*100,5),0)  as self_value,
       null                                                             as check_flag,
       null                                                             as check_comm
from dw.dw_inp_patient_info_m t1
where month_id = to_char(v_StDate_to, 'yyyy-mm')
and EXISTS (
select 1 from dw.dw_lv_main_diag_patient_info_m t2 
where t1.brxh = t2.brxh
and t2.drgs_name = '{condition}'
)
;
    '''.format(name = l_name[index],code=i,condition=condition[index])
    print(sql)
    with open('drgs_20201127.sql','a+',encoding='utf-8') as f:
        f.write(sql)
        f.close()


#重点手术
level_code = [
'LV00704020102',
'LV00704020202',
'LV00704020302',
'LV00704020402',
'LV00704020502',
'LV00704020602',
'LV00704020702',
'LV00704020802',
'LV00704020902',
'LV00704021002',
'LV00704021102',
'LV00704021202',
'LV00704021302',
'LV00704021402',
'LV00704021502',
'LV00704021602',
'LV00704021702',
'LV00704021802',
'LV00704021902',
'LV00704022002',
'LV00704022102',
'LV00704022202',
'LV00704022302',
'LV00704022402',
'LV00704022502',
'LV00704022602',
'LV00704022702',
'LV00704022802',
'LV00704022902',
'LV00704023002',
'LV00704023102',
'LV00704023202',
]
l_name = [
'髋、膝关节置换术死亡率',
'椎板切除术或脊柱融合相关手术死亡率',
'胰腺切除手术死亡率',
'食管切除手术死亡率',
'腹腔镜下胆囊切除术死亡率',
'冠状动脉旁路移植术（CABG）死亡率',
'经皮冠状动脉介入治疗（PCI）死亡率',
'颅、脑手术死亡率',
'子宫切除术死亡率',
'剖宫产死亡率',
'阴道分娩死亡率',
'乳腺手术死亡率',
'肺切除术死亡率',
'胃切除术死亡率',
'直肠切除术死亡率',
'肾与前列腺相关手术死亡率',
'血管内修补术死亡率',
'恶性肿瘤-甲状腺死亡率',
'恶性肿瘤-喉死亡率',
'恶性肿瘤-肺死亡率',
'恶性肿瘤-食管死亡率',
'恶性肿瘤-胃死亡率',
'恶性肿瘤-肝死亡率',
'恶性肿瘤-结肠死亡率',
'恶性肿瘤-胰死亡率',
'恶性肿瘤-乳腺死亡率',
'恶性肿瘤-肾死亡率',
'恶性肿瘤-前列腺死亡率',
'恶性肿瘤-膀胱死亡率',
'恶性肿瘤-输卵管-卵癌死亡率',
'恶性肿瘤-子宫死亡率',
'恶性肿瘤-淋巴结死亡率',
]
condition = [
'1.髋、膝关节置换术',
'2.椎板切除术或脊柱融合相关手术',
'3.胰腺切除手术',
'4.食管切除手术',
'5.腹腔镜下胆囊切除术',
'6.冠状动脉旁路移植术（CABG）',
'7.经皮冠状动脉介入治疗（PCI）',
'8.颅、脑手术',
'9.子宫切除术',
'10.剖宫产',
'11.阴道分娩',
'12.乳腺手术',
'13.肺切除术',
'14.胃切除术',
'15.直肠切除术',
'16.肾与前列腺相关手术',
'17.血管内修补术',
'18.1 甲状腺',
'18.2 喉',
'18.3 肺',
'18.4 食管',
'18.5 胃',
'18.6 肝',
'18.7 结肠',
'18.8 胰',
'18.9 乳腺',
'18.10 肾',
'18.11 前列腺',
'18.12 膀胱',
'18.13 输卵管-卵癌',
'18.14 子宫',
'18.15 淋巴结',
]

for index,i in enumerate(level_code):
    # print(i)
    sql = '''
    ---{name}
delete
from dw.level_master_m
where month_id = to_char(v_StDate_to, 'yyyy-mm')
  and level_code = '{code}';
insert into dw.level_master_m
select to_char(v_StDate_to, 'yyyy-mm'),
       '{code}'                                                        as level_code,
       COALESCE(round((sum(case when t1.die_flag = '1' then 1 end) /count(1))*100,5),0) as level_value,
       now()                                                            as update_time,
      COALESCE(round((sum(case when t1.die_flag = '1' then 1 end) /count(1))*100,5),0)  as self_value,
       null                                                             as check_flag,
       null                                                             as check_comm
from dw.dw_inp_patient_info_m t1
where month_id = to_char(v_StDate_to, 'yyyy-mm')
and EXISTS (
select 1 from dw.dw_lv_main_oper_patient_info_m t2 
where t1.brxh = t2.brxh
and t2.drgs_name_child = '{condition}'
)
;
    '''.format(name = l_name[index],code=i,condition=condition[index])
    print(sql)
    with open('oper_20201127.sql','a+',encoding='utf-8') as f:
        f.write(sql)
        f.close()




#特殊
level_code = [
'LV00704030106',
'LV00704030206',
'LV00704030306',
'LV00704030406',
'LV00704030506',
'LV00704030606',
'LV00704030706',
'LV00704030806',

]
l_name = [
'急性心肌梗死31日内在住院率',
'急性心力衰竭31日内在住院率',
'成人社区获得性肺炎31日内在住院率',
'脑梗死31日内在住院率',
'髋关节置换术31日内在住院率',
'膝关节置换术31日内在住院率',
'冠状动脉旁路移植术31日内在住院率',
'儿童社区获得性肺炎31日内在住院率',
]
condition = [
'1.急性心肌梗死（AMI）',
'2.急性心力衰竭（HF）',
'3.成人社区获得性肺炎（CAP）',
'4.脑梗死（STK）',
'5.膝关节置换术',
'5.髋关节置换术',
'6.冠状动脉旁路移植术 CABG',
'7.儿童社区获得性肺炎',
]

for index,i in enumerate(level_code):
    # print(i)
    sql = '''
    ---{name}
delete
from dw.level_master_m
where month_id = to_char(v_StDate_to, 'yyyy-mm')
  and level_code = '{code}';
insert into dw.level_master_m
select to_char(v_StDate_to, 'yyyy-mm'),
       '{code}'                                                        as level_code,
         COALESCE(round((sum(case when t1.return_in_1to31 = '1' then 1 end) /count(1))*100,5),0)  as level_value,
       now()                                                            as update_time,
         COALESCE(round((sum(case when t1.return_in_1to31 = '1' then 1 end) /count(1))*100,5),0) as self_value,
       null                                                             as check_flag,
       null                                                             as check_comm
from dw.dw_inp_patient_info_m t1
where month_id = to_char(v_StDate_to, 'yyyy-mm')
and EXISTS (
select 1 from dw.dw_lv_special_diag_patient_info_m t2 
where t1.brxh = t2.brxh
and t2.drgs_name = '{condition}'
)
;
    '''.format(name = l_name[index],code=i,condition=condition[index])
    print(sql)
    with open('special_20201127.sql','a+',encoding='utf-8') as f:
        f.write(sql)
        f.close()
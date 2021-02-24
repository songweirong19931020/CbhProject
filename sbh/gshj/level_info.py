# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: level_info.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/27 10:20
# ---

level_code = ['LV00702010107',
'LV00702010207',
'LV00702010307',
'LV00702010407',
'LV00702010507',
'LV00702010807',
'LV00702010907',
'LV00702011007',
'LV00702011107',
'LV00702011207',
'LV00702011307',
'LV00702011407',
'LV00702011507',
'LV00702011607',
'LV00702011707',
'LV00702011807',
'LV00702011907',
'LV00702012027',

]
condition_code = ['D00105',
'D00114',
'D00116',
'D00113',
'D00117',
'D00121',
'D00111',
'D00106',
'D00107',
'D00108',
'D00109',
'D00110',
'D00127',
'D00128',
'D00123',
'D00124',
'D00125',
'D00126',
]

for index,i in enumerate(level_code):
    sql = '''
    delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = '{level_code}';
insert into his_bi.level_master_m
select c_monthlist.month_id                                                                                          as month_id,
       '{level_code}'                                                                                    as level_code,
       case
           when count(distinct t1.pai_visit_id) = 0 then 0
           else round(coalesce((max(t2.value) * 1.00 / count(distinct t1.pai_visit_id)) * 100, 0),
                      5) end                                                                              as level_value,
       now()                                                                                              as update_time,
       case
           when count(distinct t1.pai_visit_id) = 0 then 0
           else round(coalesce((max(t2.value) * 1.00 / count(distinct t1.pai_visit_id)) * 100, 0), 5) end as self_value,
       null                                                                                               as check_flag,
       null                                                                                               as check_comm
from his_bi.dwd_inp_medical_d t1
         left join (
    select c_monthlist.month_id              as month_id,
           coalesce(count(1), 0) as value
    from his_bi.dwd_inp_medical_d a
    where a.key = '{condition_code}'
      and left(a.st_date, 6) = c_monthlist.month_id
      and exists(select 1
                 from his_bi.dwd_inp_medical_d b
                 where a.pai_visit_id = b.pai_visit_id
                   and b.key = 'D00216')
) t2 on left(t1.st_date, 6) = t2.month_id
where left(t1.st_date, 6) = c_monthlist.month_id
  and t1.key = '{condition_code}';
    '''.format(level_code = i,condition_code=condition_code[index])
    print(sql)
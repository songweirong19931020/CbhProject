# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: drgs_write.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/10/30 10:49
# ---
import os,sys

drgs_name=['急性心肌梗死',
'心力衰竭',
'肺炎（住院、成人）',
'肺炎（住院、儿童）',
'脑梗死',
'髋关节置换术',
'膝关节置换术',
'冠状动脉旁路移植术',
'剖宫产',
'慢性阻塞性肺疾病',
]

drgs_name_d = ['10.1急性心肌梗死病种例数',
'急性心肌梗死平均住院日',
'急性心肌梗死出院患者占用总床日数',
'同期急性心肌梗死总出院人数',
'急性心肌梗死次均费用',
'急性心肌梗死总出院费用',
'同期急性心肌梗死实际占用总床日数',
'急性心肌梗死病死率',
'急性心肌梗死死亡人数',
'10.2心力衰竭病种例数',
'心力衰竭平均住院日',
'心力衰竭出院患者占用总床日数',
'同期心力衰竭总出院人数',
'心力衰竭次均费用',
'心力衰竭总出院费用',
'同期心力衰竭实际占用总床日数',
'心力衰竭病死率',
'心力衰竭死亡人数',
'10.3肺炎（住院、成人）病种例数',
'肺炎（住院、成人）平均住院日',
'肺炎（住院、成人）出院患者占用总床日数',
'同期肺炎（住院、成人）总出院人数',
'肺炎（住院、成人）次均费用',
'肺炎（住院、成人）总出院费用',
'同期肺炎（住院、成人）实际占用总床日数',
'肺炎（住院、成人）病死率',
'肺炎（住院、成人）死亡人数',
'10.4肺炎（住院、儿童）病种例数',
'肺炎（住院、儿童）平均住院日',
'肺炎（住院、儿童）出院患者占用总床日数',
'同期肺炎（住院、儿童）总出院人数',
'肺炎（住院、儿童）次均费用',
'肺炎（住院、儿童）总出院费用',
'同期肺炎（住院、儿童）实际占用总床日数',
'肺炎（住院、儿童）病死率',
'肺炎（住院、儿童）死亡人数',
'10.5脑梗死病种例数',
'脑梗死平均住院日',
'脑梗死出院患者占用总床日数',
'同期脑梗死总出院人数',
'脑梗死次均费用',
'脑梗死总出院费用',
'同期脑梗死实际占用总床日数',
'脑梗死病死率',
'脑梗死死亡人数',
'10.6髋关节置换术病种例数',
'髋关节置换术平均住院日',
'髋关节置换术出院患者占用总床日数',
'同期髋关节置换术总出院人数',
'髋关节置换术次均费用',
'髋关节置换术总出院费用',
'同期髋关节置换术实际占用总床日数',
'髋关节置换术病死率',
'髋关节置换术死亡人数',
'10.7膝关节置换术病种例数',
'膝关节置换术平均住院日',
'膝关节置换术出院患者占用总床日数',
'同期膝关节置换术总出院人数',
'膝关节置换术次均费用',
'膝关节置换术总出院费用',
'同期膝关节置换术实际占用总床日数',
'膝关节置换术病死率',
'膝关节置换术死亡人数',
'10.8冠状动脉旁路移植术病种例数',
'冠状动脉旁路移植术平均住院日',
'冠状动脉旁路移植术出院患者占用总床日数',
'同期冠状动脉旁路移植术总出院人数',
'冠状动脉旁路移植术次均费用',
'冠状动脉旁路移植术总出院费用',
'同期冠状动脉旁路移植术实际占用总床日数',
'冠状动脉旁路移植术病死率',
'冠状动脉旁路移植术死亡人数',
'10.9剖宫产病种例数',
'剖宫产平均住院日',
'剖宫产出院患者占用总床日数',
'同期剖宫产总出院人数',
'剖宫产次均费用',
'剖宫产总出院费用',
'同期剖宫产实际占用总床日数',
'剖宫产病死率',
'剖宫产死亡人数',
'10.10慢性阻塞性肺疾病病种例数',
'慢性阻塞性肺疾病平均住院日',
'慢性阻塞性肺疾病出院患者占用总床日数',
'同期慢性阻塞性肺疾病总出院人数',
'慢性阻塞性肺疾病次均费用',
'慢性阻塞性肺疾病总出院费用',
'同期慢性阻塞性肺疾病实际占用总床日数',
'慢性阻塞性肺疾病病死率',
'慢性阻塞性肺疾病死亡人数',
]
kpi_code = ['JX01001',
'JX0100101',
'JX0100102',
'JX0100103',
'JX0100104',
'JX0100105',
'JX0100106',
'JX0100107',
'JX0100108',
'JX01002',
'JX0100201',
'JX0100202',
'JX0100203',
'JX0100204',
'JX0100205',
'JX0100206',
'JX0100207',
'JX0100208',
'JX01003',
'JX0100301',
'JX0100302',
'JX0100303',
'JX0100304',
'JX0100305',
'JX0100306',
'JX0100307',
'JX0100308',
'JX01004',
'JX0100401',
'JX0100402',
'JX0100403',
'JX0100404',
'JX0100405',
'JX0100406',
'JX0100407',
'JX0100408',
'JX01005',
'JX0100501',
'JX0100502',
'JX0100503',
'JX0100504',
'JX0100505',
'JX0100506',
'JX0100507',
'JX0100508',
'JX01006',
'JX0100601',
'JX0100602',
'JX0100603',
'JX0100604',
'JX0100605',
'JX0100606',
'JX0100607',
'JX0100608',
'JX01007',
'JX0100701',
'JX0100702',
'JX0100703',
'JX0100704',
'JX0100705',
'JX0100706',
'JX0100707',
'JX0100708',
'JX01008',
'JX0100801',
'JX0100802',
'JX0100803',
'JX0100804',
'JX0100805',
'JX0100806',
'JX0100807',
'JX0100808',
'JX01009',
'JX0100901',
'JX0100902',
'JX0100903',
'JX0100904',
'JX0100905',
'JX0100906',
'JX0100907',
'JX0100908',
'JX01010',
'JX0101001',
'JX0101002',
'JX0101003',
'JX0101004',
'JX0101005',
'JX0101006',
'JX0101007',
'JX0101008',
]


condition = ['COALESCE(count(distinct t1.pai_visit_id),0)',
'COALESCE(round(avg(t1.in_days),5),0)',
'COALESCE(sum(t1.in_days),0)',
'COALESCE(count(distinct t1.pai_visit_id),0)',
'case when count(distinct t1.pai_visit_id) = 0 then 0 else COALESCE(round(sum(t1.total_fees)/count(distinct t1.pai_visit_id),2),0) end',
'COALESCE(sum(t1.total_fees),0)',
'COALESCE(sum(t1.in_days),0)',
'case when count(distinct t1.pai_visit_id)=0 then 0 else count(distinct(case when t1.out_hos_way = "5" then t1.pai_visit_id end))/count(distinct t1.pai_visit_id)end ',
"max(case when t1.out_hos_way = '5' then t1.pai_visit_id end)",
]*10

n = 9
list_result = [kpi_code[i:i + n] for i in range(0, len(kpi_code), n)]
drgs_name_list = [drgs_name_d[i:i + n] for i in range(0, len(drgs_name_d), n)]
cn_list_result = [condition[i:i + n] for i in range(0, len(condition), n)]
#批量

for index,i in enumerate(list_result):
    for _ in range(0,9):
        print(i[_])
        drgs_sql = '''
             ---{drgs_name_d}
              delete from dw.kpi_master_m where month_id = to_char(v_StDate_to,'yyyy-mm') and kpi_code = '{kpi_code}';
              insert into dw.kpi_master_m  
            select
                    to_char(v_StDate_to,'yyyy-mm'),
                    '{kpi_code}' as kpi_code,
                    {condition} as kpi_value,
                    now() as update_time,
                    {condition} as self_value,
                    null as check_flag,
                    null as check_comm
                    from
                    dw.dw_inp_patient_info_m t1 
                            where 
                        month_id =  to_char(v_StDate_to,'yyyy-mm')
                        and EXISTS (
                        select 1 from dw.dw_kpi_drgs_patient_info_m t2 
                        where t1.brxh = t2.brxh
                        and 	t2.drgs_name = '{drgs_name}'
                        )
                    group by 
                    to_char(v_StDate_to,'yyyy-mm');'''.format(drgs_name=drgs_name[index],
                                                              kpi_code=list_result[index][_],
                                                              condition=cn_list_result[index][_],
                                                              drgs_name_d=drgs_name_list[index][_])
        print(drgs_sql)
        with open('drgs.txt','a+',encoding='utf-8') as f:
            f.write(drgs_sql)
            f.close()





#个性化

kpi_code=['JX04001',
'JX04002',
'JX04003',
'JX04004',
'JX04005',
'JX04101',
'JX04102',
'JX04103',
'JX04104',
'JX04105',

]
kpi_name = ['出院患者次均医药费用',
'住院收入',
'实际占用总床日数',
'出院者占用总床日',
'出院人数',
'出院患者次均药品费用',
'出院患者药品费用',
'实际占用总床日数',
'出院者占用总床日',
'出院人数',

]
condition = ['sum(total_fees)/count(1)',
'round(sum(total_fees),5)',
'round(sum(in_days),5)',
'round(sum(in_days),5)',
'COALESCE(count(DISTINCT t1.pai_visit_id),0) ',
'COALESCE(round(sum(pham_fees)/count(1),5),0)',
'round(sum(pham_fees),5)',
'round(sum(in_days),5)',
'round(sum(in_days),5)',
'COALESCE(count(DISTINCT t1.pai_visit_id),0) ',
]
for index,i in enumerate(kpi_code):
    sql = '''
     ---{name_d}
                  delete from dw.kpi_master_m where month_id = to_char(v_StDate_to,'yyyy-mm') and kpi_code = '{kpi_code}';
                  insert into dw.kpi_master_m  
    select
                        to_char(v_StDate_to,'yyyy-mm'),
                        '{kpi_code}' as kpi_code,
                       {condition}  as kpi_value,
                        now() as update_time,
                       {condition} as self_value,
                        null as check_flag,
                        null as check_comm
                        from
                        dw.dw_inp_patient_info_m t1 
                                where 
                            month_id =  to_char(v_StDate_to,'yyyy-mm');
    '''.format(name_d=kpi_name[index],kpi_code = i,condition=condition[index])
    print(sql)
    with open('other.txt', 'a+', encoding='utf-8') as f:
        f.write(sql)
        f.close()





#门诊量
kpi_code=['JX0070201',
'JX01802',
'JX02202',

]
kpi_name = ['门诊诊疗工作的总人次数（急诊、健康体检者不计入）',
'同期门诊诊疗总人次数（不包括健康体检者及未开具药物处方患者）',
'总诊疗人次数（不含急诊人次数，健康体检）',

]
condition = ['count(distinct t1.outp_visit_id)',
'count(distinct t1.outp_visit_id)',
'count(distinct t1.outp_visit_id)',

]
for index,i in enumerate(kpi_code):
    sql = '''
    ---{name_d}
                      delete from dw.kpi_master_m where month_id = to_char(v_StDate_to,'yyyy-mm') and kpi_code = '{kpi_code}';
                      insert into dw.kpi_master_m    
             select
            t1.month_id,
            '{kpi_code}' as kpi_code,
            count(distinct t1.outp_visit_id) as kpi_value,
            now() as update_time,
            count(distinct t1.outp_visit_id) as self_value,
            null as check_flag,
            null as check_comm
            from
            dw.dw_outp_patient_info_m t1
            where
                    month_id=to_char(v_StDate_to,'yyyy-mm')
                    and t1.outp_type_code not in ('2','22')
            group by 
            t1.month_id;
    '''.format(kpi_code = i,name_d=kpi_name[index])
    print(sql)



#费用写入
kpi_code=['JX03101',
'JX03102',
'JX03103',
'JX03104',
'JX03105',
'JX03106',
'JX03200',
'JX03201',

]
kpi_name = ['医疗服务收入',
'药品收入',
'卫生材料收入',
'检查收入',
'化验收入',
'医疗收入',
'辅助用药收入(省)',
'辅助用药收入(国家)',
]
condition = ['service_fees',
'pham_fees',
'material_fees',
'check_fees',
'inspect_fees',
'total_fees',
'assist_pham_fees',
'assist_pham_fees',
]
for index,i in enumerate(kpi_code):
    sql = '''
        ---{name_d}
                          delete from dw.kpi_master_m where month_id = to_char(v_StDate_to,'yyyy-mm') and kpi_code = '{kpi_code}';
                          insert into dw.kpi_master_m    
    SELECT
    foo.month_id,
    '{kpi_code}' as kpi_code,
    coalesce(round(sum(foo.o_total_fees)+sum(i_total_fees),5),0) as kpi_value,
    now(),
    coalesce(round(sum(foo.o_total_fees)+sum(i_total_fees),5),0) as self_value,
    null as check_flag,
    null as check_comm
    from
    (SELECT
    month_id,
    sum({condition}) as o_total_fees,
    0 as i_total_fees
    from 
    dw.dw_outp_patient_info_m t1 
    WHERE
    t1.month_id = to_char(v_StDate_to,'yyyy-mm')
    GROUP BY
    t1.month_id
    union all 
    select
    to_char(st_date,'yyyy-mm') as month_id,
    0 as o_total_fees,
    sum({condition}) as i_total_fees
    from 
    dw.dw_inp_patient_info_m
    WHERE
    to_char(st_date,'yyyy-mm') = to_char(v_StDate_to,'yyyy-mm')
    GROUP BY
    to_char(st_date,'yyyy-mm'))foo
    GROUP BY foo.month_id;
    '''.format(kpi_code = i,name_d=kpi_name[index],condition=condition[index])
    print(sql)



txt = ['JX00101/JX00102',
'JX00301/JX00302',
'JX00401/JX00402',
'JX00501/JX00502',
'JX00601/JX00602',
'JX00801/JX00802',
'JX00901/JX00902',
'JX01801/JX01802',
'JX01901/JX01902',
'JX02201/JX02202',
'JX02701/JX02702',
'JX02901/JX02902',
'JX03101/JX03106',
'JX03200/JX03202',
'JX03802/JX03803',
]

for i in txt:
    print(i.split("/")[1])


kpi_code=[
'JX003',
'JX004',
'JX005',
'JX006',
'JX008',
'JX009',
'JX018',
'JX019',
'JX022',
'JX027',
'JX029',
'JX031',
'JX032',

]
kpi_name = [
'3.日间手术占择期手术比例',
'4.出院患者手术占比▲',
'5.出院患者微创手术占比▲',
'6.出院患者四级手术比例▲',
'8.手术患者并发症发生率▲',
'9.I类切口手术部位感染率▲',
'18.门诊患者基本药物处方占比',
'19.住院患者基本药物使用率',
'22.门诊患者平均预约诊疗率',
'27.门诊收入占医疗收入比例',
'29.住院收入占医疗收入比例',
'31.医疗服务收入（不含药品、耗材、检查检验收入）占医疗收入比例▲',
'32.辅助用药收入占比',

]
code_1 = ['JX00301',
'JX00401',
'JX00501',
'JX00601',
'JX00801',
'JX00901',
'JX01801',
'JX01901',
'JX02201',
'JX02701',
'JX02901',
'JX03101',
'JX03200',
]
code_2 = ['JX00302',
'JX00402',
'JX00502',
'JX00602',
'JX00802',
'JX00902',
'JX01802',
'JX01902',
'JX02202',
'JX02702',
'JX02902',
'JX03106',
'JX03202',
]

for index,i in enumerate(kpi_code):
    sql = '''
    ---{name_d}
    delete from dw.kpi_master_m where month_id = to_char(v_StDate_to,'yyyy-mm') and kpi_code = '{kpi_code}';
                  insert into dw.kpi_master_m  
    select
                to_char(v_StDate_to,'yyyy-mm'),
                '{kpi_code}' as kpi_code,
                coalesce(round(COALESCE(max(t2.kpi_value),0)/max(t1.kpi_value),5)*100,0) as kpi_value,
                now() as update_time,
                coalesce(round(COALESCE(max(t2.kpi_value),0)/max(t1.kpi_value),5)*100,0) as self_value,
                null as check_flag,
                null as check_comm
                from
                dw.kpi_master_m t1
                left join dw.kpi_master_m t2 on t1.kpi_code = t2.kpi_code and t1.month_id = t2.month_id 
                and t2.kpi_code='{code1}'
                where
                t1.month_id=to_char(v_StDate_to,'yyyy-mm')
                and t1.kpi_code in('{code1}','{code2}');
    '''.format(kpi_code = i,name_d=kpi_name[index],code1=code_1[index],code2=code_2[index])
    print(sql)






kpi_code=['JX037',
'JX038',
'JX039',
'JX040',
'JX041',


]
kpi_name = ['37.医疗收入增幅',
'38.门诊次均费用增幅▲',
'39.门诊次均药品费用增幅▲',
'40.住院次均费用增幅▲',
'41.住院次均药品费用增幅▲',

]
condition = ['JX03701',
'JX03801',
'JX03901',
'JX04001',
'JX04101',

]


for index,i in enumerate(kpi_code):
    sql = '''
        ---{name_d}
        delete from dw.kpi_master_m where month_id = to_char(v_StDate_to,'yyyy-mm') and kpi_code = '{kpi_code}';
                      insert into dw.kpi_master_m  
    select
        to_char(v_StDate_to,'yyyy-mm'),
        '{kpi_code}' as kpi_code ,
        coalesce(round(((sum(case when t1.month_id =  to_char(v_StDate_to,'yyyy-mm') then t1.kpi_value end)-
                         sum(case when t1.month_id = to_char(to_date(left(to_char(v_StDate_to,'yyyy-mm'),4), 'yyyy') -  interval '1' year,'yyyy')||right( to_char(v_StDate_to,'yyyy-mm'),2) then t1.kpi_value end))/
                        sum(case when t1.month_id =  to_char(to_date(left( to_char(v_StDate_to,'yyyy-mm'),4), 'yyyy') -  interval '1' year,'yyyy')||right( to_char(v_StDate_to,'yyyy-mm'),2) then t1.kpi_value end))*100,5),0) as kpi_value,
        now() as update_time ,
        coalesce(round(((sum(case when t1.month_id =  to_char(v_StDate_to,'yyyy-mm') then t1.kpi_value end)-
                         sum(case when t1.month_id = to_char(to_date(left(to_char(v_StDate_to,'yyyy-mm'),4), 'yyyy') -  interval '1' year,'yyyy')||right( to_char(v_StDate_to,'yyyy-mm'),2) then t1.kpi_value end))/
                        sum(case when t1.month_id =  to_char(to_date(left( to_char(v_StDate_to,'yyyy-mm'),4), 'yyyy') -  interval '1' year,'yyyy')||right( to_char(v_StDate_to,'yyyy-mm'),2) then t1.kpi_value end))*100,5),0) as self_value,
        null as check_flag  ,
        null as check_comm
    from dw.kpi_master_m t1
    where t1.kpi_code='{condition}'
      and  to_date(left(t1.month_id,4),'yyyy')>= to_date(left(to_char(v_StDate_to,'yyyy-mm'),4), 'yyyy') -  interval '1' year
      and to_date(left(t1.month_id,4),'yyyy')< to_date(left(to_char(v_StDate_to,'yyyy-mm'),4), 'yyyy') +  interval '1' year;
    
    '''.format(kpi_code = i,name_d=kpi_name[index],condition=condition[index])
    print(sql)
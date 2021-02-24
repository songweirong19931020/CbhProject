# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: dingtalk_mionitor.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/17 11:28
# ---
import json
import requests
import sys
import datetime
import pandas as pd
from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.LogUitl import *
with PgSQLContextManager() as db_cursor:
    count_sql = '''
SELECT
table_name,
pg_size_pretty(table_size) AS table_size,
pg_size_pretty(indexes_size) AS indexes_size,
pg_size_pretty(total_size) AS total_size
FROM (
SELECT
table_name,
pg_table_size(table_name) AS table_size,
pg_indexes_size(table_name) AS indexes_size,
pg_total_relation_size(table_name) AS total_size
FROM (
SELECT ('' || table_schema || '.' || table_name || '') AS table_name
FROM information_schema.tables 
) AS all_tables
ORDER BY total_size DESC
) AS pretty_sizes
limit 10;  
    '''
    db_cursor.execute(count_sql)
    result = db_cursor.fetchall()
    pc = pd.DataFrame(result,columns=['table_name','table_size','indexes_size','total_size'])
    total_txt = 'text:{}'.format(pc)
    # total_txt = '''运行任务总数：{}，成功任务数：{}，失败任务数：{}'''.format(result[0][0],result[0][1],result[0][2])
    total_txt=[]
    for g in range(0,5):
        print(pc['table_name'][g]+":"+pc['total_size'][g]+"\n")
        total_txt.append(pc['table_name'][g]+":"+pc['total_size'][g])
    a = ';'.join(total_txt)
    faile_sql = '''
    select
function_name
from dwd.run_table_log
where
date(insert_time) = date(current_date)
and status='Failed'
    '''
    db_cursor.execute(faile_sql)
    failedresult = db_cursor.fetchall()
    f_list = []
    for index,i in enumerate(failedresult):
        # print(index,i[0])
        f_list.append(i[0])
    list3 = ';'.join(f_list)
    failed_detial_txt = '''失败任务明细：{}'''.format(list3)



today = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
def send_msg(url,con_text):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            # "title": "调度任务定时提醒",
            # "text":"调度日期：{date_now},Azkaban-leslie运行情况：{con_text}".format(date_now=today,con_text=con_text),
            "content": "调度日期：{date_now},PgFunctionJob-Leslie运行情况：\n{con_text}".format(date_now=today,con_text=con_text),
            # "title": "阿兹卡班报错汇总",
            # "picUrl": "图片连接",
            # "messageUrl": "你需要发布的连接地址"
        },
        "at": {
            "atMobiles": [
                "13871329460",
            ],
            "isAtAll": False
    }
    }
    r = requests.post(url,data = json.dumps(data),headers=headers)
    return r.text


url = 'https://oapi.dingtalk.com/robot/send?access_token=e984ae54db339ef42008d75f83e04eee19d2fdeb1c76c4fffe5917b568bfb7c7'                #此处为丁丁机器人的地址，参考技术手册创建
con_text = total_txt + '\n'+failed_detial_txt
print(send_msg(url,con_text))





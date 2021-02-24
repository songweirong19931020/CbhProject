# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Knn.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/9/19 14:59
# ---
# coding:utf-8
import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\postgres_dwd_run_table_log.csv')

#设置切分区域
listBins = [0, 50, 100, 200, 300, 400, 2000]
#设置切分后对应标签
listLabels = ['0_50','51_100','101_200','201_300','301_400','401_2000']
df['total_use_time'] = df['total_use_time'].fillna(0)
df = df.loc[(df['routine_schema']=='dwd')&(df['total_use_time']!=0.0)]

df['fenzu'] = pd.cut(df['total_use_time'], bins=listBins, labels=listLabels, include_lowest=True)

df1 = df.loc[(df['fenzu']!='401_2000')&(df['fenzu']!='301_400')]
df2 = df.loc[(df['fenzu']=='401_2000')|(df['fenzu']=='301_400')]
list_function_name=[]

for i in df1.values:
    print(i[1])
    list_function_name.append(i[1])

list_slow=[]
for i in df2.values:
    print(i[1])
    list_slow.append(i[1])



n = 5
list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]


for  i in range(len(list_result)):
    try:
    # print(list_result[i])
        list_result[i].append(list_slow[i])
    except:
        continue


for i in list_result:
    print(i)


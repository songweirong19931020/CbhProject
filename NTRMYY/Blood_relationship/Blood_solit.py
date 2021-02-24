# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Blood_solit.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/19 8:48
# ---
import pandas as pd
import re

df = pd.read_csv(r"C:\Users\CBH\PycharmProjects\Cenboom\NTRMYY\Blood_relationship\2021-02-06.csv")


target_insert_table=[]
target_insert_key=[]
pattern_blood_table=[]
pattern_father_table=[]
pattern_all = []
for index,i in enumerate(df['detail']):
    print(index)
    pattern_blood_all = re.compile(".*from\s+(\w+.\w+)")
    print(re.findall(pattern_blood_all, i))
    pattern_all.append(re.findall(pattern_blood_all, i))
    i = i.replace('\n', '')
    # i = i.strip()
    # print(i)
    pattern_yl = re.compile('delete from\s+(\w+.\w+)',
        re.IGNORECASE | re.M)
    # print(target_insert_table)
    target_insert_table.append(str(re.findall(pattern_yl, i)).replace("[","").replace("]",""))
    #delete from dwd.dwd_inp_income_d where st_date = v_StDate_to and key = 'DI1021';
    pattern_key = re.compile("delete from\s+.*key\s+=\s+'(\w+\d{4})';")
    # print(target_insert_key.append(re.findall(pattern_key, i)))
    target_insert_key.append(str(re.findall(pattern_key, i)).replace("[","").replace("]",""))
    pattern_blood = re.compile("join\s+(\w+.\w+)")
    # print(re.findall(pattern_blood,i))
    pattern_blood_table.append(str(re.findall(pattern_blood,i)).replace("[","").replace("]",""))
    pattern_father = re.compile("AS\s\S+.*from\s+(\w+.\w+)")
    print(re.findall(pattern_father,i))
    pattern_father_table.append(str(re.findall(pattern_father,i)).replace("[","").replace("]",""))


df_result = pd.DataFrame()
df_result['target_insert_table'] = target_insert_table
df_result['target_insert_key'] = target_insert_key
df_result['pattern_blood_table'] = pattern_blood_table
df_result['pattern_father_table'] = pattern_father_table
df_result['pattern_all'] = pattern_all

dataframe_a = pd.DataFrame()
dataframe_a['target_insert_table'] = target_insert_table
dataframe_b = pd.DataFrame()
dataframe_b['pattern_all'] = str(pattern_all).replace('[','').replace(']','')

dataframe_a = dataframe_a.append(dataframe_b)
dataframe_a = dataframe_a.append(dataframe_b)

result = dataframe_a.drop_duplicates(subset=['target_insert_table','pattern_all'],keep=False)


for index,value in enumerate(df_result['pattern_all']):
    # print(index,value)
    if df_result['target_insert_table'][index] in value:
        print(value.remove(df_result['target_insert_table'][index]))
df_result.to_csv("result_blddotable_20210206.csv")

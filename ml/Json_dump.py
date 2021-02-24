# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Json_dump.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/26 14:01
# ---
import json
import pandas as pd
data =  pd.read_excel(r'E:\echars\blood_temp_data.xlsx')
df1 = data['father_name'].duplicated()
father_name = data['father_name'].drop_duplicates()
for i in father_name:
    print(i)

list_codedic = []

a = json.dumps(list_codedic)
for index,i in  enumerate(father_name):
    print('''{ "name": "'''+i+'''",'"children":[''')
    for indexb,g in enumerate(data['kpi_code']):
        if data['father_name'][indexb] == i:
         print('''{name:"'''+g+'",'+"value:1},")
        else:
            pass
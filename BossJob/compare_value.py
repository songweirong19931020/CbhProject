# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: compare_value.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2021/1/25 10:30
# ---
import pandas as pd

df_hos = pd.read_excel(r'D:\Sbh\BossJob\pythonetl\Demo.xlsx',sheet_name='hos_value')
df_ns = pd.read_excel(r'D:\Sbh\BossJob\pythonetl\Demo.xlsx',sheet_name='ns_value')

df_union = pd.merge(left=df_ns, right=df_hos, how='left',
                   left_on='ficd10', right_on='ficd10')
df_union_result = df_union.loc[(df_union['fdesc_x'] != df_union['fdesc_y'])]  # 取不同的值

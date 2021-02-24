# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: replace_ods_medical.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/10/22 16:26
# ---

import re
import os

files = os.listdir(r'D:\Sbh\甘肃\Azkaban-甘肃\源代码包\history')

target_l = ['pg_d_100_sql.py',
'pg_d_101_sql.py',
'pg_d_102_sql.py',
'pg_d_103_sql.py',
'pg_d_104_sql.py',
'pg_d_105_sql.py',
'pg_d_106_sql.py',
'pg_d_107_sql.py',
'pg_d_108_sql.py',
'pg_d_109_sql.py',
'pg_d_110_sql.py',
'pg_d_111_sql.py',
'pg_d_112_sql.py',
'pg_d_113_sql.py',
'pg_d_114_sql.py',
'pg_d_115_sql.py',
'pg_d_116_sql.py',
'pg_d_117_sql.py',
'pg_d_118_sql.py',
'pg_d_119_sql.py',
'pg_d_120_sql.py',
'pg_d_121_sql.py',
'pg_d_122_sql.py',
'pg_d_123_sql.py',
'pg_d_124_sql.py',
'pg_d_125_sql.py',
'pg_d_126_sql.py',
'pg_d_127_sql.py',
'pg_d_128_sql.py',
'pg_d_206_sql.py',
'pg_d_207_sql.py',
'pg_d_226_sql.py',
'pg_d_227_sql.py',
'pg_d_228_sql.py',
'pg_d_229_sql.py',
'pg_d_230_sql.py',
'pg_d_231_sql.py',
'pg_d_232_sql.py',
'pg_d_233_sql.py',
'pg_d_238_sql.py',
'pg_d_239_sql.py',
'pg_d_240_sql.py',
'pg_d_242_sql.py',
'pg_d_243_sql.py',
'pg_d_244_sql.py',
'pg_d_245_sql.py',
'pg_d_246_sql.py',
'pg_d_247_sql.py',
'pg_d_41_sql.py',
'pg_d_44_sql.py',
'pg_d_45_sql.py',
'pg_d_46_sql.py',
'pg_d_48_sql.py',
'pg_d_49_sql.py',
'pg_d_50_sql.py',
'pg_d_51_sql.py',
'pg_d_52_sql.py',
]
def replaceStr(file):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        print(str)
        str1 = re.sub('list_day = Get_Time_Qj_30()', 'list_day = Get_Time_Qj_Medical', str)
        with open(file,'w', encoding='utf-8') as f:
            f.write(str1)

def addStr(file):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        print(str)
        # str1 = re.sub('Get_Last_2_Month_id()', 'Get_Last_Day_30', str)
        with open(file,'a+', encoding='utf-8') as f:
            # str1 = '\nretries=1\nretry.backoff=1800000'
            str1='\ndependencies=yl_mintor'
            f.write(str1)


print(files)
for f in target_l:
    print(os.path.join('D:\Sbh\甘肃\Azkaban-甘肃\源代码包\history',f))
    replaceStr(os.path.join('D:\Sbh\甘肃\Azkaban-甘肃\源代码包\history',f))




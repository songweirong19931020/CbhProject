# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: re_drgs.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/20 16:24
# ---
import re
re_txt = [
'18.1 甲状腺',
'18.1 甲状腺手术总例数',
'18.1 甲状腺死亡率',
'18.1 甲状腺术后非预期的重返手术室再手术率',
'18.2 喉',
'18.2 喉手术总例数',
'18.2 喉死亡率',
'18.2 喉术后非预期的重返手术室再手术率',
'18.3 肺',
'18.3 肺手术总例数',
'18.3 肺死亡率',
'18.3 肺术后非预期的重返手术室再手术率',
'18.4 食管',
'18.4 食管手术总例数',
'18.4 食管死亡率',
'18.4 食管术后非预期的重返手术室再手术率',
'18.5 胃',
'18.5 胃手术总例数',
'18.5 胃死亡率',
'18.5 胃术后非预期的重返手术室再手术率',
'18.6 肝',
'18.6 肝手术总例数',
'18.6 肝死亡率',
'18.6 肝术后非预期的重返手术室再手术率',
'18.7 结肠',
'18.7 结肠手术总例数',
'18.7 结肠死亡率',
'18.7 结肠术后非预期的重返手术室再手术率',
'18.8 胰',
'18.8 胰手术总例数',
'18.8 胰死亡率',
'18.8 胰术后非预期的重返手术室再手术率',
'18.9 乳腺',
'18.9 乳腺手术总例数',
'18.9 乳腺死亡率',
'18.9 乳腺术后非预期的重返手术室再手术率',
'18.10 肾',
'18.10 肾手术总例数',
'18.10 肾死亡率',
'18.10 肾术后非预期的重返手术室再手术率',
'18.11 前列腺',
'18.11 前列腺手术总例数',
'18.11 前列腺死亡率',
'18.11 前列腺术后非预期的重返手术室再手术率',
'18.12 膀胱',
'18.12 膀胱手术总例数',
'18.12 膀胱死亡率',
'18.12 膀胱术后非预期的重返手术室再手术率',
'18.13 输卵管-卵癌',
'18.13 输卵管-卵癌手术总例数',
'18.13 输卵管-卵癌死亡率',
'18.13 输卵管-卵癌术后非预期的重返手术室再手术率',
'18.14 子宫',
'18.14 子宫手术总例数',
'18.14 子宫死亡率',
'18.14 子宫术后非预期的重返手术室再手术率',
'18.15 淋巴结',
'18.15 淋巴结手术总例数',
'18.15 淋巴结死亡率',
'18.15 淋巴结术后非预期的重返手术室再手术率',
]
for i in re_txt:
    pattren = r'\d+.\d+.(.*)'
    print('恶性肿瘤-'+re.findall(pattren,i)[0])

di_txt = [
'1.髋、膝关节置换术',
'1.髋、膝关节置换术总台次',
'1.髋、膝关节置换术死亡例数',
'1.髋、膝关节置换术术后非预期再手术',
'1.髋、膝关节置换术术前平均住院日',
'1.髋、膝关节置换术平均住院日',
'1.髋、膝关节置换术平均住院费用',
'2.椎板切除术或脊柱融合相关手术',
'2.椎板切除术或脊柱融合相关手术总台次',
'2.椎板切除术或脊柱融合相关手术死亡例数',
'2.椎板切除术或脊柱融合相关手术术后非预期再手术',
'2.椎板切除术或脊柱融合相关手术术前平均住院日',
'2.椎板切除术或脊柱融合相关手术平均住院日',
'2.椎板切除术或脊柱融合相关手术平均住院费用',
'3.胰腺切除手术',
'3.胰腺切除手术总台次',
'3.胰腺切除手术死亡例数',
'3.胰腺切除手术术后非预期再手术',
'3.胰腺切除手术术前平均住院日',
'3.胰腺切除手术平均住院日',
'3.胰腺切除手术平均住院费用',
'4.食管切除手术',
'4.食管切除手术总台次',
'4.食管切除手术死亡例数',
'4.食管切除手术术后非预期再手术',
'4.食管切除手术术前平均住院日',
'4.食管切除手术平均住院日',
'4.食管切除手术平均住院费用',
'5.腹腔镜下胆囊切除术',
'5.腹腔镜下胆囊切除术总台次',
'5.腹腔镜下胆囊切除术死亡例数',
'5.腹腔镜下胆囊切除术术后非预期再手术',
'5.腹腔镜下胆囊切除术术前平均住院日',
'5.腹腔镜下胆囊切除术平均住院日',
'5.腹腔镜下胆囊切除术平均住院费用',
'6.冠状动脉旁路移植术（CABG）',
'6.冠状动脉旁路移植术（CABG）总台次',
'6.冠状动脉旁路移植术（CABG）死亡例数',
'6.冠状动脉旁路移植术（CABG）术后非预期再手术',
'6.冠状动脉旁路移植术（CABG）术前平均住院日',
'6.冠状动脉旁路移植术（CABG）平均住院日',
'6.冠状动脉旁路移植术（CABG）平均住院费用',
'7.经皮冠状动脉介入治疗（PCI）',
'7.经皮冠状动脉介入治疗（PCI）总台次',
'7.经皮冠状动脉介入治疗（PCI）死亡例数',
'7.经皮冠状动脉介入治疗（PCI）术后非预期再手术',
'7.经皮冠状动脉介入治疗（PCI）术前平均住院日',
'7.经皮冠状动脉介入治疗（PCI）平均住院日',
'7.经皮冠状动脉介入治疗（PCI）平均住院费用',
'8.颅、脑手术',
'8.颅、脑手术总台次',
'8.颅、脑手术死亡例数',
'8.颅、脑手术术后非预期再手术',
'8.颅、脑手术术前平均住院日',
'8.颅、脑手术平均住院日',
'8.颅、脑手术平均住院费用',
'9.子宫切除术',
'9.子宫切除术总台次',
'9.子宫切除术死亡例数',
'9.子宫切除术术后非预期再手术',
'9.子宫切除术术前平均住院日',
'9.子宫切除术平均住院日',
'9.子宫切除术平均住院费用',
'10.剖宫产',
'10.剖宫产总台次',
'10.剖宫产死亡例数',
'10.剖宫产术后非预期再手术',
'10.剖宫产术前平均住院日',
'10.剖宫产平均住院日',
'10.剖宫产平均住院费用',
'11.阴道分娩',
'11.阴道分娩总台次',
'11.阴道分娩死亡例数',
'11.阴道分娩术后非预期再手术',
'11.阴道分娩术前平均住院日',
'11.阴道分娩平均住院日',
'11.阴道分娩平均住院费用',
'12.乳腺手术',
'12.乳腺手术总台次',
'12.乳腺手术死亡例数',
'12.乳腺手术术后非预期再手术',
'12.乳腺手术术前平均住院日',
'12.乳腺手术平均住院日',
'12.乳腺手术平均住院费用',
'13.肺切除术',
'13.肺切除术总台次',
'13.肺切除术死亡例数',
'13.肺切除术术后非预期再手术',
'13.肺切除术术前平均住院日',
'13.肺切除术平均住院日',
'13.肺切除术平均住院费用',
'14.胃切除术',
'14.胃切除术总台次',
'14.胃切除术死亡例数',
'14.胃切除术术后非预期再手术',
'14.胃切除术术前平均住院日',
'14.胃切除术平均住院日',
'14.胃切除术平均住院费用',
'15.直肠切除术',
'15.直肠切除术总台次',
'15.直肠切除术死亡例数',
'15.直肠切除术术后非预期再手术',
'15.直肠切除术术前平均住院日',
'15.直肠切除术平均住院日',
'15.直肠切除术平均住院费用',
'16.肾与前列腺相关手术',
'16.肾与前列腺相关手术总台次',
'16.肾与前列腺相关手术死亡例数',
'16.肾与前列腺相关手术术后非预期再手术',
'16.肾与前列腺相关手术术前平均住院日',
'16.肾与前列腺相关手术平均住院日',
'16.肾与前列腺相关手术平均住院费用',
'17.血管内修补术',
'17.血管内修补术总台次',
'17.血管内修补术死亡例数',
'17.血管内修补术术后非预期再手术',
'17.血管内修补术术前平均住院日',
'17.血管内修补术平均住院日',
'17.血管内修补术平均住院费用',

]
for i in di_txt:
    pattren = r'\d+.(.*)'
    print(re.findall(pattren,i)[0])




total_name=['急性心肌梗死',
'急性心力衰竭',
'成人社区获得性肺炎',
'脑梗死',
'髋关节置换术',
'膝关节置换术',
'冠状动脉旁路移植术',
'儿童社区获得性肺炎',]

loop_r = ['总例数',
'死亡例数',
'平均住院日',
'平均住院费用',
'15日内再住院率',
'31日内在住院率',]

for i in total_name:
    print(i)
    for g in loop_r:
        print(i+g)
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: function_re.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/18 10:51
# ---
import re

name_list = [
'pg_d_230',
'pg_d_123',
'pg_d_148',
'pg_d_140',
'pg_d_89',
'pg_d_5007',
'pg_d_104',
'pg_d_186',
'pg_d_221',
'pg_d_202',
'pg_d_244',
'pg_d_195',
'pg_d_5017',
'pg_d_23',
'pg_d_209',
'pg_d_157',
'pg_d_133',
'pg_d_5015',
'pg_d_31',
'pg_d_166',
'pg_d_132',
'pg_d_188',
'pg_d_105',
'pg_d_126',
'pg_d_5001',
'pg_d_181',
'pg_d_174',
'pg_d_5022',
'pg_d_01001',
'pg_d_112',
'pg_d_139',
'pg_d_119',
'pg_d_48',
'pg_d_24',
'pg_d_39',
'pg_d_238',
'pg_d_250',
'pg_d_236',
'pg_d_189',
'pg_d_203',
'pg_d_222',
'pg_d_18',
'pg_d_92',
'pg_d_5014',
'pg_d_5008',
'pg_d_175',
'pg_d_145',
'pg_d_159',
'pg_d_134',
'pg_d_138',
'pg_d_5023',
'pg_d_120',
'pg_d_25',
'pg_d_91',
'pg_d_152',
'pg_d_106',
'pg_d_183',
'pg_d_30',
'pg_d_173',
'pg_d_5020',
'pg_d_125',
'pg_d_53',
'pg_d_237',
'pg_d_5013',
'pg_d_235',
'pg_d_17',
'pg_d_190',
'pg_d_40',
'pg_d_180',
'pg_d_5002',
'pg_d_201',
'pg_d_111',
'pg_d_172',
'pg_d_37',
'pg_d_107',
'pg_d_5024',
'pg_d_151',
'pg_d_26',
'pg_d_100',
'pg_d_245',
'pg_d_137',
'pg_d_242',
'pg_d_216',
'pg_d_208',
'pg_d_146',
'pg_d_135',
'pg_d_215',
'pg_d_182',
'pg_d_29',
'pg_d_41',
'pg_d_117',
'pg_d_52',
'pg_d_191',
'pg_d_128',
'pg_d_243',
'pg_d_160',
'pg_d_110',
'pg_d_154',
'pg_d_223',
'pg_d_136',
'pg_d_94',
'pg_d_171',
'pg_d_108',
'pg_d_200',
'pg_d_5021',
'pg_d_127',
'pg_d_225',
'pg_d_5003',
'pg_d_19',
'pg_d_162',
'pg_d_153',
'pg_d_161',
'pg_d_109',
'pg_d_5012',
'pg_d_93',
'pg_d_38',
'pg_d_42',
'pg_d_118',
'pg_d_28',
'pg_d_143',
'pg_d_226',
'pg_d_14',
'pg_d_192',
'pg_d_5004',
'pg_d_44',
'pg_d_199',
'pg_d_178',
'pg_d_170',
'pg_d_185',
'pg_d_218',
'pg_d_95',
'pg_d_144',
'pg_d_206',
'pg_d_234',
'pg_d_224',
'pg_d_149',
'pg_d_20',
'pg_d_5011',
'pg_d_5005',
'pg_d_5018',
'pg_d_51',
'pg_d_142',
'pg_d_163',
'pg_d_101',
'pg_d_241',
'pg_d_27',
'pg_d_198',
'pg_d_34',
'pg_d_210',
'pg_d_156',
'pg_d_88',
'pg_d_169',
'pg_d_232',
'pg_d_227',
'pg_d_45',
'pg_d_96',
'pg_d_179',
'pg_d_5010',
'pg_d_207',
'pg_d_217',
'pg_d_5025',
'pg_d_50',
'pg_d_246',
'pg_d_129',
'pg_d_233',
'pg_d_5000',
'pg_d_36',
'pg_d_228',
'pg_d_116',
'pg_d_5019',
'pg_d_115',
'pg_d_193',
'pg_d_239',
'pg_d_102',
'pg_d_141',
'pg_d_204',
'pg_d_197',
'pg_d_176',
'pg_d_21',
'pg_d_130',
'pg_d_184',
'pg_d_35',
'pg_d_46',
'pg_d_187',
'pg_d_5016',
'pg_d_5009',
'pg_d_194',
'pg_d_16',
'pg_d_49',
'pg_d_121',
'pg_d_150',
'pg_d_114',
'pg_d_33',
'pg_d_168',
'pg_d_164',
'pg_d_248',
'pg_d_22',
'pg_d_231',
'pg_d_229',
'pg_d_103',
'pg_d_155',
'pg_d_131',
'pg_d_90',
'pg_d_220',
'pg_d_5006',
'pg_d_196',
'pg_d_205',
'pg_d_167',
'pg_d_219',
'pg_d_165',
'pg_d_177',
'pg_d_158',
'pg_d_113',
'pg_d_32',
'pg_d_15',
'pg_d_122',
'pg_d_240',
'pg_d_124',
'pg_d_5026',
'pg_d_1002',
'pg_d_147',
'pg_d_5037',
'pg_d_1003',
'pg_d_1004',
'pg_d_1005',
'pg_d_1006',
'pg_d_1007',
'pg_d_1008',
'pg_d_1009',
'pg_d_5027',
'pg_d_5028',
'pg_d_5029',
'pg_d_5030',
'pg_d_5031',
'pg_d_5032',
'pg_d_5033',
'pg_d_5034',
'pg_d_5035',
'pg_d_5036',
]
for i in name_list:
    # print(i)
    pattern = r'\d+'
    # print(re.findall(pattern,i)[0])
    if len(re.findall(pattern,i)[0]) == 2:
        print("fun_dwd_D000" + re.findall(pattern, i)[0] + "_d")
    elif len(re.findall(pattern,i)[0]) == 3:
        print("fun_dwd_D00"+re.findall(pattern,i)[0]+"_d")
    else:
        print("fun_dwd_D0" + re.findall(pattern, i)[0] + "_d")



#重点疾病编码
drgs_name = ['1. 急性心肌梗死',
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
eg_list = [
'病种期内总例数',
'病种期内死亡例数',
'病种期内15 日内再住院率',
'病种期内31 日内再住院率',
]

for index,i in enumerate(drgs_name):
    # print(i)
    if index + 1 >= 10:
        # print(i)
        # print('LV0070401'+str(index+1))
        print("LV0070401")
        for indexe,e in enumerate(eg_list):
            print('LV0070401' + str(index + 1))
            # print('LV0070401'+str(index+1)+"0"+str(indexe+1))
            # print(i + e)
    else:
        # print(i)
        print("LV0070401")
        # print('LV00704010' + str(index + 1))
        for indexe, e in enumerate(eg_list):
            print('LV00704010' + str(index + 1))
            # print('LV00704010'+str(index+1)+"0"+str(indexe+1))
            # print(i + e)




oper_list = [
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
eg_list=[
'手术总例数',
'死亡率',
'术后非预期的重返手术室再手术率',
]

for index,i in enumerate(oper_list):
    # print(i)
    if index+1>=10:
        # print(i)
        print("LV0070402")
        # print('LV0070402'+str(index+1))
    # print("LV007030301")
        for indexe,e in enumerate(eg_list):
            print('LV0070402' + str(index + 1))
            # print('LV0070402'+str(index+1)+"0"+str(indexe+1))
            # print(i + e)
    else:
        # print(i)
        print("LV0070402")
        # print('LV00704020' + str(index + 1))
        for indexe,e in enumerate(eg_list):
            print('LV00704020' + str(index + 1))
            # print('LV00704020'+str(index+1)+"0"+str(indexe+1))
            # print(i + e)



rate_list = [
    ' ',
'人',
'%',
'%',
]*32
for i in rate_list:
    print(i)
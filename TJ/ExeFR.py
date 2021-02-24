# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: ExeFR.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site:
# @Time: 2020/12/17 10:41
# ---
import pandas as pd
frname = ['reagent/reagent-kysjecys.cpt',
'pts/pts-kscyhzxx.cpt',
'reagent/reagent-sjbyskswys.cpt',
'mips/mips-discharge-pat-cost-catalog.cpt',
'dms/hszzy_kjywsy.cpt',
'emr/zy_hz_Detail.cpt',
'H0001/bms_lfyjstyjj.cpt',
'inp/sxk_kstfqkcx.cpt',
'reagent/reagent-ticket_ky.cpt',
'emr/mr_qc_detail.cpt',
'cdt/OPS.cpt',
'dms/dms_pham_purchase_percent.cpt',
'daily/patient_jzk.cpt',
'mips/mips-mzyb_settle-info.cpt',
'outp/mzghsrbb_mzfzz.cpt',
'info/Dept_exec_clinical.cpt',
'materi/materi_hmcs_zhuisu.cpt',
'mips/mips-employee-non-realtime.cpt',
'dms/zy_kjywsyqd_link.cpt',
'bms/sari_refund_flag.cpt',
'mips/mips-chi-fine-detail.cpt',
'mips/mips-phi-fine-detail.cpt',
'outp/check_reg_select.cpt',
'emr/emr_ggwsk.cpt',
'daily/diag_search.cpt',
'inp/icu_workload.cpt',
'emr/phyexam_F137_result.cpt',
'inp/CRE_xdfc_two_weeks.cpt',
'pts/pts-019.cpt',
'inp/inp_cp_pathway_info_ysz.cpt',
'outp/outp_mzhylxcx.cpt',
'materi/materi-017.cpt',
'emr/good_room.cpt',
'reagent/reagent-ktlsjqd_ky.cpt',
'H0001/bms_yjcx.cpt',
'outp/outp-31.cpt',
'info/jjxm_vs_zlxm.cpt',
'inp/zy_hzType_Amount.cpt',
'reagent/reagent-rkqd_ky.cpt',
'H0001/part_mixture_summary.cpt',
'info/_jbxx_info_.cpt',
'outp/outp_dept_ghlcx.cpt',
'mips/pre_surgery_lab_medicine_critical_info.cpt',
'dms/dms_supplier_supply_situation.cpt',
'reagent/reagent-ckqd_ky.cpt',
'H0001/jsy_workload.cpt',
'ers/H0004_CT_info.cpt',
'inp/H0004_patient_detail.cpt',
'daily/mr_qc_stat.cpt',
'emr/mr_qc_result.cpt',
'mips/mips-multi-mat-info.cpt',
'inp/H0004_F137_info.cpt',
'pts/pts-hzthcx.cpt',
'mips/mips-inp-patient-stat.cpt',
'mips/mips-insur-pat-derate.cpt',
'inp/organ_transplantation_donors.cpt',
'inp/inp_cre_xdscsc_pati.cpt',
'outp/mz_ysgrzxgzltj.cpt',
'dms/DMS_YK_repire_date.cpt',
'emr/emr_mzbldy.cpt',
'emr/emr_ypfl.cpt',
'info/_pham_info_.cpt',
'mips/mips-ybhzxf.cpt',
'materi/materi_hm_ejkcrkcx.cpt',
'dms/zy_kjywsyqd_link_doctor.cpt',
'H0001/bms_ybjsrcjfytj.cpt',
'inp/CRE_mcsc_ymjg.cpt',
'ers/blood_search_nursing.cpt',
'outp/wkmz_qtejfz.cpt',
'outp/jz_zdqktj.cpt',
'materi/goods_baseinfo.cpt',
'dms/dms-zzzjcx_zhcx.cpt',
'dms/DMS_YF_pham_inout_sub.cpt',
'mips/mips_upload_server.cpt',
'mips/mips-hzfbxg.cpt',
'mips/whsyb_jsjb_hzfy.cpt',
'outp/outp_jzk_result.cpt',
'outp/outp_0fee_tj.cpt',
'mips/mips-daily-w055-search.cpt',
'outp/terstfzbtjc_wcyx.cpt',
'daily/terstfzbtjc_hz.cpt',
'daily/dl_business_data.cpt',
'reagent/reagent-rkhz_ky.cpt',
'reagent/reagent-in-dept-total_ky.cpt',
'dms/dms-pharm-budget-bill-search.cpt',
'H0001/bms_jbyjjzjjzfqktjb.cpt',
'inp/inp_nursing_level_count.cpt',
'inp/zyzgfymx.cpt',
'outp/outp-opcancel.cpt',
'H0001/bms_mzbrgfylrb.cpt',
'mips/mips-mzzz_settle-info-with-catalogue.cpt',
'inp/inp_cp_pathway_info_ysz2.cpt',
'outp/cpoe_outp_kjywbl.cpt',
'inp/kstfmxcx.cpt',
'daily/hzfymxqkcx.cpt',
'ers/ers-jcyyxzgzltj-ex.cpt',
'emr/emr-brhzxib.cpt',
'emr/vte_pat_count.cpt',
'inp/inp_crbbgk.cpt',
'reagent/reagent-goodscode-total_ky.cpt',
'dms/Dms_goods_supplier_catalog_ky.cpt',
'H0001/bms_tkyecx.cpt',
'H0001/outp_yggzlzhtj.cpt',
'H0001/pca_brczfs_hz.cpt',
'bms/tzfb_amount_cx.cpt',
'mips/mips-yb-ysy-wdz.cpt',
'mips/mips-chi-non-realtime-error.cpt',
'isms/isms_Ticket_receive.cpt',
'inp/H0004_blood_info.cpt',
'inp/H0004_bed_info.cpt',
'daily/cpoe_search_szyxzx.cpt',
'inp/lcyykfytj.cpt',
'mips/mips-pat-w055-search.cpt',
'daily/xerjz_ndt.cpt',
'ers/med-lab-yygzltj.cpt',
'materi/materi_hmcs_gzhcdzjf.cpt',
'pts/zbpb_ywgzz.cpt',
'dms/DMS_YK_pham_inout_account_zhcx.cpt',
'dms/zy_kjywsy_link.cpt',
'eif/eifservice.cpt',
'ers/ers-jcyymx-wzx.cpt',
'H0001/bms_jzbrsrtj.cpt',
'H0001/bms_zyjsygzlcx.cpt',
'H0001/cwtftj_link.cpt',
'H0001/outp_in_out_total.cpt',
'H0001/pca_mzyjjjzcx.cpt',
'H0001/pca_operatordetail2.cpt',
'inp/CRE_lcscjg1.cpt',
'inp/inp_ljzdmc.cpt',]
scname=[]
pathname=[]
for i in frname:
    print(i.split("/")[0])
    scname.append(i.split("/")[0])
    pathname.append(i.split("/")[1])

df = pd.DataFrame()
df['scname'] = scname
df['pathname'] = pathname
df.to_csv('scname.csv',index=False)


import  os
import  time
import pyautogui as pag
#打开文件夹
def openfr(frname):
    time.sleep(2)
    pag.click(25,133)
    #输入文件名
    pag.click(1363,320)
    time.sleep(2)
    pag.typewrite(frname)
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.doubleClick(965,379)
    time.sleep(1)
    pag.doubleClick(1363, 320)
    time.sleep(1)
    pag.hotkey('ctrl', 'a')
    time.sleep(3)
    pag.hotkey('Backspace')
    time.sleep(1)
    pag.click(1425, 241)
frnamelist = [
'Dept_exec_clinical.cpt',
'jjxm_vs_zlxm.cpt',
'_jbxx_info_.cpt',
'_pham_info_.cpt',
]
fig = 255
for i in frnamelist:
    print(i)
    openfr(i)
    time.sleep(20)
    #打开FR
    pag.click(51,444)
    time.sleep(1)
    pag.click(399,230)
    time.sleep(1)
    pag.hotkey('ctrl', 'c')
    pag.click(48,361)
    time.sleep(1)
    pag.click(199,542)
    time.sleep(1)
    pag.click(325,fig)
    time.sleep(1)
    pag.hotkey('ctrl','v')
    time.sleep(1)
    pag.click(51,444)
    time.sleep(1)
    pag.click(703,90)
    time.sleep(1)
    fig += 21


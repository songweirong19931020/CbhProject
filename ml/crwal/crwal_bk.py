# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: crwal_bk.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/10/28 9:11
# ---
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import os, sys
import pandas as pd
url = r'https://wh.fang.ke.com/loupan'
driver_path = r'C:\Users\CBH\AppData\Local\Google\Chrome\Application\chromedriver.exe'

driver = webdriver.Chrome(driver_path)
driver.get(url)
driver.find_element_by_xpath("//*[@class='district-wrapper']/li[7]").click()

# #获取价钱范围10000-15000元/m²
# driver.find_element_by_xpath\
#     ("//*[@class='common-filter price-filter-container price-filter-sign price-filter-single clearfix post_ulog_exposure_scroll']/ul/li[3]").click()
#
# #面积110-130㎡
# driver.find_element_by_xpath\
#     ("//*[@class='common-filter area-filter-container clearfix post_ulog_exposure_scroll']/ul/li[5]").click()
title_list=[]
adress_list=[]
model_class_list=[]
money_list=[]
link_href_list=[]
for g in range(0,15):
    for i in range(1,11):
        # print(i)
        time.sleep(1)
        title = driver.find_element_by_xpath("//*[@class='resblock-list-container clearfix']/ul[2]/li[{}]/div/div/a".format(i)).text
        title_list.append(title)
        #获取地理位置
        time.sleep(1)
        adress = driver.find_element_by_xpath("//*[@class='resblock-list-container clearfix']/ul[2]/li[{}]/div/a[1]".format(i)).text
        adress_list.append(adress)
        #获取户型
        time.sleep(1)
        model_class = driver.find_element_by_xpath("//*[@class='resblock-list-container clearfix']/ul[2]/li[{}]/div/a[2]".format(i)).text
        model_class_list.append(model_class)
        #获取价格
        time.sleep(1)
        money = driver.find_element_by_xpath("//*[@class='resblock-list-container clearfix']/ul[2]/li[{}]/div/div[3]/div/span[1]".format(i)).text
        money_list.append(money)
        time.sleep(1)
        link = driver.find_element_by_xpath("//*[@class='resblock-list-container clearfix']/ul[2]/li[{}]/a".format(i))
        link_href= link.get_attribute("href") #获取链接
        link_href_list.append(link_href)
        print("执行完成第{i}条记录".format(i = i))
    df = pd.DataFrame()
    df['title'] = title_list
    df['adress'] = adress_list
    df['model_class'] = model_class_list
    df['money'] = money_list
    df['link'] = link_href_list
    df.to_csv(r'D:\colony\crawl\crawl.csv', mode='a', header=False, index=False)
    title_list = []
    adress_list = []
    model_class_list = []
    money_list = []
    link_href_list = []
    driver.find_element_by_xpath("//*[@class='next']").click()


df = pd.DataFrame()
df['title'] = title_list
df['adress'] = adress_list
df['model_class'] = model_class_list
df['money'] = money_list
df['link'] = link_href_list
df.to_csv(r'D:\colony\crawl\crawl.csv',index=False)
df.to_csv(r'D:\colony\crawl\crawl.csv',mode='a',header=False,index=False)



#安居客房屋爬虫
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import os, sys
import pandas as pd
# url = r'https://wuhan.anjuke.com/sale/hanyang/a131-d55-t49/?pi=baidu-cpc-wh-ty2&kwid=89451451936&bd_vid=7997502845828861885'
# url = r'https://wuhan.anjuke.com/sale/wuchanga/a131-d55-t49/?pi=baidu-cpc-wh-ty2&kwid=89451451936&bd_vid=7997502845828861885'
url = r'https://wuhan.anjuke.com/sale/jianghana/a131-d55-t49/?pi=baidu-cpc-wh-ty2&kwid=89451451936&bd_vid=7997502845828861885'
driver_path = r'C:\Users\CBH\AppData\Local\Google\Chrome\Application\chromedriver.exe'

driver = webdriver.Chrome(driver_path)
driver.get(url)

title_list=[]
money_list=[]
avg_money_list = []
model_list=[]
arrey_list = []
mid_level_list = []
build_date_list = []
adress_list=[]
link_href_list=[]

for g in range(20):
    for i in range(1,34):
        title = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[2]/div[1]/a".format(i)).text
        money = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[3]/span[1]".format(i)).text
        avg_money = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[3]/span[2]".format(i)).text
        model = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[2]/div[2]/span[1]".format(i)).text
        arrey = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[2]/div[2]/span[2]".format(i)).text
        mid_level = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[2]/div[2]/span[3]".format(i)).text
        build_date = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[2]/div[2]/span[4]".format(i)).text
        adress = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[2]/div[3]/span[1]".format(i)).text
        link = driver.find_element_by_xpath("//*[@id='houselist-mod-new']/li[{}]/div[2]/div/a".format(i))
        link_href= link.get_attribute("href")
        title_list.append(title)
        money_list.append(money)
        avg_money_list.append(avg_money)
        model_list.append(model)
        arrey_list.append(arrey)
        mid_level_list.append(mid_level)
        build_date_list.append(build_date)
        adress_list.append(adress)
        link_href_list.append(link_href)
        print('执行完成第{}条'.format(i))
    time.sleep(2)
    df = pd.DataFrame()
    df['title'] = title_list
    df['money'] = money_list
    df['avg_money'] = avg_money_list
    df['model'] = model_list
    df['arrey'] = arrey_list
    df['mid_level'] = mid_level_list
    df['build_date'] = build_date_list
    df['adress'] = adress_list
    df['link_href'] = link_href_list
    df.to_csv(r'D:\colony\crawl\crawl.csv', mode='a', header=False, index=False)
    driver.find_element_by_xpath("//*[@class='aNxt']").click()
    title_list = []
    money_list = []
    avg_money_list = []
    model_list = []
    arrey_list = []
    mid_level_list = []
    build_date_list = []
    adress_list = []
    link_href_list = []
    print('执行完成第{}页'.format(g))
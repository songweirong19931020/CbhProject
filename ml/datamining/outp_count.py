# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: outp_count.py
# @Author: Leslie Cheung
# @E-mail: leslieswr0820@gmail.com
# @Site: 
# @Time: 2020/11/19 15:40
# ---
from fbprophet import Prophet
import numpy as np
import pandas as pd
sales_df = pd.read_csv(r'D:\Result_2.csv')
sales_df['y_orig'] = sales_df['count']
sales_df['count'] = np.log(sales_df['count'])

#开始建立模型
model = Prophet()
model.fit(sales_df)
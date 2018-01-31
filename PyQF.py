# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:23:36 2018

@author: gyouth
"""

# 获取历史K线和成交额数据
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import tushare as ts

codes = input('Input the stock codes you want to query,spliting with comma:\n').split(',')
StartDate = input('Input the start date to query, format YYYY-MM-DD:\n')
EndDate = input('Input the end date to query, format YYYY-MM-DD:\n')

for code in codes:
    df = ts.get_h_data(code, start=StartDate, end=EndDate)
    date_raw = df.index
    date = [d.date() for d in date_raw]
    close = df['close'].values
    amount = df['amount'].values
  
    datefmter = mdates.DateFormatter('%Y%m%d')
    datelocator = mdates.AutoDateLocator()
    
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(date, close, color='r', linewidth=1.3, label='close price')
    ax1.set(ylabel='price', title=code)
    ax1.set_xticklabels(['']*len(date))
    plt.legend()
    
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.bar(date, amount/100000000, color='r', linewidth=1.3, label='amount')
    ax2.set(xlabel='date', ylabel='amount(0.1 billion)')
    ax2.set_xticklabels(date)
    ax2.xaxis.set_major_locator(datelocator)
    ax2.xaxis.set_major_formatter(datefmter)
    plt.legend()
    
    fig.autofmt_xdate()    #设置x轴时间外观
    
    df.to_excel(code+'.xlsx', 'Sheet1')
    
    plt.show()
    
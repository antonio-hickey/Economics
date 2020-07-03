#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:43:40 2020

@author: Antonio Hickey
"""
#--------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
#--------------------------------------------------------------------------
data = pd.read_csv('/home/sratus/Desktop/Data_Science/Yeild_Curve/Yeild Curve.csv')
#--------------------------------------------------------------------------
row = data.iloc[-1]
x = ['1mo', '2mo', '3mo', '6mo', '1yr', '2yr', '3yr', '5yr', '7yr', '10yr', '20yr', '30yr']
y = row.values[1:]
#--------------------------------------------------------------------------
# Defining x date
date_string = datetime.datetime.now().strftime("%Y-%m-%d")
fig = plt.figure()
txt = "Created By Antonio Hickey, Data Sourced from www.treasury.gov"
plt.plot(x, y, color='cadetblue', label=date_string, lw=5)
plt.legend()
fig.text(.132, .02, txt, c='black')
plt.ylabel("Interest Rate %")
plt.title(date_string + " Yeild Curve")
plt.show()
#--------------------------------------------------------------------------
fig.savefig('/home/sratus/Desktop/Data_Science/Yeild_Curve/' + date_string +'.png')
#--------------------------------------------------------------------------

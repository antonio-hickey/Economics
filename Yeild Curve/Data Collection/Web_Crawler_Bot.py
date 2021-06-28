#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:16:19 2020

@author: Antonio Hickey
"""
#-------------------------------------------------------------------
# Importing Modules
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import csv
#-------------------------------------------------------------------
# Config
url =  'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield'
uClient = uReq(url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()
# Defining Elements
Elements = page_soup.findAll("td", {"class" : "text_view_data"})
# Splitting most recent elements
date = Elements[-13].text
mo1 = Elements[-12].text
mo2 = Elements[-11].text
mo3 = Elements[-10].text
mo6 = Elements[-9].text
yr1 = Elements[-8].text
yr2 = Elements[-7].text
yr3 = Elements[-6].text
yr5 = Elements[-5].text
yr7 = Elements[-4].text
yr10 = Elements[-3].text
yr20 = Elements[-2].text
yr30 = Elements[-1].text

# Defining New Data
data = (date, mo1, mo2, mo3, mo6, yr1, yr2, yr3, yr5, yr7, yr10, yr20, yr30)

# Appending Dataset with New Elements
with open(r'Yeild Curve.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)







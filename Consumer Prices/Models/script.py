import pandas as pd
import numpy as np

cpi = pd.read_csv('../Data/CPI.csv')
oil = pd.read_csv('../Data/Oil_Prices.csv')
dates_l = []
oil_test = []
for date in cpi['DATE']:
    dates_l.append(date)
    oil_test.append(oil[oil["DATE"]==date])
print(oil_test)
cpi["Oil"] = oil_test["DCOILWTICO_PC1"]
print(cpi)

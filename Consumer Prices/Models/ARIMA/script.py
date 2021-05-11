#-----------------------------
# Import Modules
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#-------------------------------

# Data
df = pd.read_csv('https://raw.githubusercontent.com/antonio-hickey/Economics/master/Consumer%20Prices/Data/PCETRIM12M159SFRBDAL.csv', parse_dates=['Date'],index_col=['Date'])

plt.plot(df)
plt.show()

rolling_mean = df.rolling(window=12).mean()
rolling_std = df.rolling(window=12).std()

plt.plot(df, color='blue',label='Original')
plt.plot(rolling_mean, color='red',label='Rolling Mean')
plt.plot(rolling_std,color='black',label='Rolling Std')
plt.legend(loc='best')
plt.show()



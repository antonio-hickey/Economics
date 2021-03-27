#-------------------------------
# Import Modules		#
#-------------------------------
import pandas as pd
import csv
#-------------------------------
# Import Data			#
#-------------------------------
mkt_cap = pd.read_csv("market-cap.csv")
mkt_cap = mkt_cap.set_index('Date')
tx_vol = pd.read_csv("transaction-volume.csv")
tx_vol = tx_vol.set_index('Date')
#-------------------------------
# Data prep			#
#-------------------------------
# Matching Dates & Values
matched_dates = []
matched_mkt_cap = []
matched_tx_vol = []
for date in mkt_cap.index:
    if date in tx_vol.index:
        matched_dates.append(date)
        matched_tx_vol.append(tx_vol['Volume'].loc[date])
        matched_mkt_cap.append(mkt_cap['market-cap'].loc[date])
# New dataframe with matched dates & values
cleaned_list = pd.DataFrame({
    'Date': matched_dates,
    'Volume': matched_tx_vol,
    'Market Cap': matched_mkt_cap
})
#-------------------------------
# Deriving Velocity		#
#-------------------------------
velocity = []
for val in range(len(cleaned_list['Date'])):
    velocity.append((cleaned_list['Volume'].loc[val] / cleaned_list['Market Cap'].loc[val])*100)
#-------------------------------
# Output to velocity.csv	#
#-------------------------------
filename = "velocity.csv"
# Column
columns = ["Dates","Velocity"]
# Rows
rows = []
for row in range(len(cleaned_list)):
	rows.append([matched_dates[row],velocity[row]])
# Csv output
with open(filename,'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(columns)
	for row in rows:
		csvwriter.writerow(row)
#-------------------------------


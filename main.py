import csv
import pandas as pd

data = pd.read_csv('main.csv', index_col=0)
columns = data.columns.values.tolist()

new_df = pd.DataFrame()

USA_data  = []
for index, row in data.iterrows():
 	if("USA" in row['COUNTRY']):
 		USA_data.append(row)

new_df = new_df.append(USA_data)
new_df.to_csv('filteredCountry.csv')
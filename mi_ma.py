import pandas as pd

df = pd.read_csv('filteredCountry.csv', index_col=0)

dup_index = None
min_rate = []

final_data = []

for index, row in df.iterrows():
	if index == dup_index:
		min_rate.append(row["PRICE"])
		
	else:
		if dup_index is None:
			pass
		else:
			final_data.append([dup_index, min_rate])
			min_rate = []
		
		dup_index = index
		min_rate.append(row["PRICE"])
		

final_values = []
final_df = pd.DataFrame()

for entry in final_data:
	if(len(entry[1]) > 1):
		df = pd.DataFrame({'SKU':entry[0], 'FIRST_MINIMUM_PRICE':entry[1][0], 'SECOND_MINIMUM_PRICE':entry[1][1]}, index=[0])
		final_values.append(df)


final_df = pd.concat(final_values)
final_df.to_csv('lowestPrice.csv', index=False)
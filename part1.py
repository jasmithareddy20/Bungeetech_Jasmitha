#!/usr/bin/env python
# coding: utf-8
import pandas as pd
df = pd.read_csv(r"C:\Users\jasmitha\Downloads\intership-test-master\intership-test-master\input\main.csv", header=0)
df1 = df[df['COUNTRY'].str.contains("USA")]
#print(df1)
df1.to_csv(r"C:\Users\jasmitha\Downloads\intership-test-master\intership-test-master\output\filteredCountry.csv" , index=False)




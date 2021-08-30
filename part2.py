#!/usr/bin/env python
# coding: utf-8
import pandas as pd
df =pd.read_csv(r"C:\Users\bhaga\Downloads\intership-test-master\intership-test-master\output\filteredCountry.csv")
df1=df.iloc[:,[0,5]]
allDuplicateExceptLast=df1.loc[df1.SKU.duplicated(keep="last"),]
firstDuplicate=allDuplicateExceptLast.drop_duplicates(subset=["SKU"])
firstDuplicate.reset_index(drop=True, inplace=True)
firstDuplicate.columns=["SKU","FIRST_MINIMUM_PRICE"]
#print(firstDuplicate)
allDuplicateExceptFirst=df1.loc[df1.SKU.duplicated(keep="first"),]
secondDuplicate=allDuplicateExceptFirst.drop_duplicates(subset=["SKU"])
secondDuplicateColumn=secondDuplicate.iloc[:,[1]]
secondDuplicateColumn.reset_index(drop=True, inplace=True)
secondDuplicateColumn.columns=["SECOND_MINIMUM_PRICE"]
final=pd.concat([firstDuplicate,secondDuplicateColumn],axis=1)
final.to_csv(r"C:\Users\bhaga\Downloads\intership-test-master\intership-test-master\output\lowestPrice.csv")
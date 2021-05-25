# coding=utf-8
import io
import csv
import codecs
import pandas as pd
df = pd.read_csv(open('test2.csv'),index_col=0, encoding = 'utf-8')
#df.loc[-1] = ["Org_Cn_Name", "Address1_Cn"Phone, ]
#df.insert(0, "OrgID", "N/A")
print(df)
df.dropna(inplace = True)
sub ='联系电话'
if df.str.find(sub) == -1:
    
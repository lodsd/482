import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("tags.csv",index_col=0)
print(df.head(3),"\n")
print(df.shape,"\n")
df.info()
print("\n")
print(df.describe())
col=df.columns.values
print(col)
print(df.duplicated())
print(df[df.duplicated()])
#df.drop_duplicates(inplace=True)
#print(df.shape,"\n")
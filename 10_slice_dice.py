import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/P3PenguinData.csv')

filtered_df = df.filter(['bill_depth_mm', 'bill_length_mm'])
print(filtered_df.head())

sorted_filtered_df = filtered_df.sort_values(by=['bill_depth_mm', 'bill_length_mm'])
print(sorted_filtered_df.head())

in_sorted_filtered_df = sorted_filtered_df.apply(lambda mm : mm / 25.4)
print(in_sorted_filtered_df.head())

filtered_df2 = df.filter(['species', 'bill_depth_mm', 'bill_length_mm'])
print(filtered_df2.head())

crosstabbed_filtered_df2 = pd.crosstab(df['species'], df['bill_depth_mm'], margins=True)
print(crosstabbed_filtered_df2.head())

deep_bill_filtered_df2 = filtered_df2[filtered_df2['bill_depth_mm'] > 20.5]
print(deep_bill_filtered_df2.head(10))
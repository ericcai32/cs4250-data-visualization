import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/P3PenguinData.csv')

filtered_df = df.filter(['species', 'bill_depth_mm', 'bill_length_mm'])
adelie_filtered_df = filtered_df[filtered_df['species'] == 'Adelie']
chinstrap_filtered_df = filtered_df[filtered_df['species'] == 'Chinstrap']
final_df = pd.concat([chinstrap_filtered_df, adelie_filtered_df])
final_df.reset_index(drop=True, inplace=True)

print(final_df.head())
print(final_df.tail())

ax = sns.barplot(data=final_df, x='species', y='bill_length_mm', errorbar=None)

for bar in ax.containers:
    ax.bar_label(bar, padding=-20)

plt.figure()

ax = sns.histplot(data=final_df, x='bill_length_mm', hue='species')
for bar in ax.containers:
    ax.bar_label(bar)

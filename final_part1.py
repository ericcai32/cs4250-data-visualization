import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.options.display.max_columns = None

df = pd.read_csv('data/eod_2023_burke_county_nc.csv', sep='\t')
print(df.columns)
print(df.head)

print(df['elevation'].sum())

relevant_columns = ['order',
                    'family',
                    'genus',
                    'species',
                    'decimalLatitude',
                    'decimalLongitude',
                    'day',
                    'month'
                    ]
df = df[relevant_columns]
print(df)

ax = sns.countplot(data=df, y='order', order = df['order'].value_counts().index)
labels = df['order'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0], labels=labels)

plt.xlim(0, 8300)
plt.xlabel("Count")
plt.ylabel("Order")
plt.title("2023 Bird Observations by Order in Burke County, NC")

plt.figure()

no_pass_df = df[df['order'] != 'Passeriformes']

ax = sns.countplot(data=no_pass_df, y='order', order = no_pass_df['order'].value_counts().index)
labels = no_pass_df['order'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0], labels=labels)

plt.xlim(0, 830)
plt.xlabel("Count")
plt.ylabel("Order")
plt.title("2023 Bird Observations by Order in Burke County, NC")
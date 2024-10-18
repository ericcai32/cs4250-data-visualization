import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = None

df = pd.read_csv('data/eod_2023_burke_county_nc.csv', sep='\t')
relevant_columns = ['order',
                    'family',
                    'genus',
                    'species',
                    'decimalLatitude',
                    'decimalLongitude',
                    'day',
                    'month',
                    'individualCount'
                    ]

df = df[relevant_columns]

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

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_days_total = np.cumsum(month_days)

"""
num_birds_df = pd.DataFrame()
num_birds_df['day'] = np.arange(1, 366)
num_birds_df['count'] = np.zeros(365)

for i in range(len(df)):
    if df['month'][i] ==x 1:
        day = df['day'][i]
    else:
        day = month_days_total[df['month'][i] - 2] + df['day'][i]
    
    num_birds_df['count'][day - 1] += 1

plt.figure()
sns.scatterplot(data=num_birds_df, x='day', y='count')
"""
plt.figure()
sns.countplot(data=df, x='month', color="lightblue")
sns.countplot(data=no_pass_df, x='month', color="orange")

"""
plt.figure(figsize=(10, 50))
sns.countplot(data=df, y='species', hue='family', dodge=False, palette='Set3', order=df['species'].value_counts().index)

plt.figure(figsize=(10, 15))
sns.countplot(data=df, y='family', order=df['family'].value_counts().index)
"""

"""
plt.figure(figsize=(10, 50))
sns.countplot(data=df, y='species', hue='order', dodge=False, palette='Set3', order=df['species'].value_counts().index)
"""
plt.figure(figsize=(10, 10))
sns.scatterplot(data=df[df['order']=='Passeriformes'], x='decimalLongitude', y='decimalLatitude', hue='order')
plt.ylim(35.4, 36.1)
plt.xlim(-82, -81.3)

plt.figure()
sns.barplot(data=df, x='individualCount', y='order')
"""
for order in df['order'].unique():
    plt.figure(figsize=(10, 10))
    sns.scatterplot(data=df[df['order']==order], x='decimalLongitude', y='decimalLatitude')
    plt.ylim(35.4, 36.1)
    plt.xlim(-82.02, -81.32)
    plt.title(order)
"""

for order in df['order'].unique():
    plt.figure()
    ax = sns.countplot(data=df[df['order']==order], x='month', color="lightblue")
    plt.title(order)

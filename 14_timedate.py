import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('Data/Birthdays.csv')

df["Born"] = pd.to_datetime(df["Born"])
df["Died"] = pd.to_datetime(df["Died"])
df['Age'] = (df['Died'] - df['Born']) / np.timedelta64(1,'D') / 365.2425
df['Weeday_born'] = df['Born'].dt.day_name()
df['Month_born'] = df['Born'].dt.month
df['Months_age'] = df['Age'] * 12


df.sort_values(by='Age', inplace=True)

print(df)

ax = sns.barplot(data=df, y='Name', x='Age')
ax.bar_label(container=ax.containers[0], labels=df['Age'].astype(int))
plt.xlim(0, 90)

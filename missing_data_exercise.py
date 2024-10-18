import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
import pandas as pd
import seaborn as sns

pd.options.display.max_columns = None

df = pd.read_csv('data/HousePrice.csv')

df_shape = df.shape
print(f"There are {df_shape[0]} rows of data in the dataset.")
print(f"There are {df_shape[1]} rows of data in the dataset.")

num_nulls = df.isnull().sum()
num_null_cols = (num_nulls > 0).sum()
print(f"There are {num_null_cols} columns with missing data.")

sorted_nulls = num_nulls[num_nulls > 0].sort_values()
print(f"The feature with the most missing data is '{sorted_nulls.index[-1]}'.")
print(f"The feature with the least missing data is '{sorted_nulls.index[0]}'.")

short_df = df[['MasVnrArea', 'LotFrontage', 'FireplaceQu', 'BsmtExposure']]

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.histplot(data=short_df, x='MasVnrArea', bins=20)
zeroless_masvnrarea = short_df[short_df['MasVnrArea'] > 0]
plt.subplot(2, 2, 2)
sns.histplot(data=zeroless_masvnrarea, x='MasVnrArea', bins=20)

print(f"The mean value of LotFrontage is {short_df['LotFrontage'].mean()}.")

plt.subplot(2, 2, 3)
sns.histplot(data=short_df, x='LotFrontage', bins=20)

short_df['FireplaceQu'].fillna('Missing', inplace=True)
plt.subplot(2, 2, 4)
ax = sns.countplot(data=short_df, x='FireplaceQu')
ax.bar_label(ax.containers[0])

print("\n\n")
# Plot a bubble plot to display the latitude, longitude, and rain for each of
# the explored counties in North Carolina.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/joint_nc_weather.csv')
print(df.columns)

plt.rcParams['figure.figsize']=[10, 6]

plt.subplot(2, 1, 1)

sns.scatterplot(
    data=df,
    x='LONGITUDE',
    y='LATITUDE',
    size='TOTAL PRCP 2022',
    sizes=(100, 600),
    hue='COUNTY',
    palette='tab20',)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.subplot(2, 1, 2)

sns.scatterplot(
    data=df,
    x='LONGITUDE',
    y='LATITUDE',
    size='TOTAL PRCP 2003',
    sizes=(100, 600),
    hue='COUNTY',
    palette='tab20',)

plt.legend([], [], loc='upper left', bbox_to_anchor=(1, 1))

plt.figure(figsize=[8,6])
plt.subplot(2, 1, 1)
sns.scatterplot(
    data=df,
    x='AVG TMAX 2003',
    y='AVG TMIN 2003',
    size='TOTAL PRCP 2022',
    sizes=(100, 600),
    hue='COUNTY',
    palette='tab20',)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xlabel("")

plt.subplot(2, 1, 2)
sns.scatterplot(
    data=df,
    x='AVG TMAX 2003',
    y='AVG TMIN 2003',
    size='TOTAL PRCP 2022',
    sizes=(100, 600),
    hue='COUNTY',
    palette='tab20',)
plt.legend([], [])

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_03 = pd.read_csv('data/pasquotank_2003.csv')
df_22 = pd.read_csv('data/pasquotank_2022.csv')

plt.rcParams['figure.figsize'] = (10, 5)

plt.plot(df_03['PRCP'])
plt.plot(df_22['PRCP'])

print(np.sum(df_03['PRCP']))
print(np.sum(df_22['PRCP']))

print(np.mean(df_03['PRCP']))
print(np.mean(df_22['PRCP']))

pd.set_option('display.max_rows', None)


# print(df_03[df_03['PRCP'] > 0]['PRCP'])
print(len(df_03[df_03['PRCP'] > 0]['PRCP']))
print(len(df_22[df_22['PRCP'] > 0]['PRCP']))

print(np.sum(df_03[df_03['PRCP'] > 0]['PRCP']))
print(np.sum(df_22[df_22['PRCP'] > 0]['PRCP']))

plt.figure()

plt.plot(np.cumsum(df_03['PRCP']))
plt.plot(np.cumsum(df_22['PRCP']))

plt.figure()
sns.violinplot(y=df_03[df_03['PRCP'] > 0]['PRCP'])
sns.violinplot(y=df_22[df_22['PRCP'] > 0]['PRCP'])

# print(df_03[df_03['PRCP'] > 0]['PRCP'])


combined_df = pd.DataFrame()
combined_df['PRCP_03'] = df_03[df_03['PRCP'] > 0].reset_index()['PRCP']
combined_df['PRCP_22'] = df_22[df_22['PRCP'] > 0].reset_index()['PRCP']

# print(combined_df)

plt.figure()
sns.boxplot(data=combined_df)

plt.figure()
sns.violinplot(data=combined_df)

# print(df_03)

print(df_03['PRCP'].quantile([0, 0.25, 0.5, 0.75, 1]))
print(df_22['PRCP'].quantile([0, 0.25, 0.5, 0.75, 1]))

print(df_03['PRCP'].quantile(np.arange(0, 1.1, 0.1)))
print(df_22['PRCP'].quantile(np.arange(0, 1.1, 0.1)))

months =  ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
months_row = []
month_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in df_03.index:
    month = int(df_03['DATE'][i][5:7])
    month_sum[month - 1] += df_03['PRCP'][i]

plt.figure()
plt.bar(months, month_sum, alpha=0.8)

month_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in df_22.index:
    month = int(df_22['DATE'][i][5:7])
    month_sum[month - 1] += df_22['PRCP'][i]

plt.bar(months, month_sum, alpha=0.8)

plt.figure()

plt.hist(df_03['PRCP'], bins=np.arange(0.01, 1, 0.1), alpha=0.8)
plt.hist(df_22['PRCP'], bins=np.arange(0.01, 1, 0.1), alpha=0.8)

plt.figure()
plt.scatter(df_03['TMAX'], df_03.index)
plt.scatter(df_22['TMAX'], df_22.index)

plt.figure()
plt.plot(np.cumsum(df_03['TMAX']))
plt.plot(np.cumsum(df_22['TMAX']))

print(np.mean(df_03['TMAX']))
print(np.mean(df_22['TMAX']))

print(np.mean(df_03['TMIN']))
print(np.mean(df_22['TMIN']))

plt.figure()
plt.hist(df_03['TMAX'], bins=np.arange(20, 110, 10), alpha=0.7)
plt.hist(df_22['TMAX'], bins=np.arange(20, 110, 10), alpha=0.7)

plt.figure()
plt.hist(df_03['TMIN'], bins=np.arange(0, 110, 10), alpha=0.7)
plt.hist(df_22['TMIN'], bins=np.arange(0, 110, 10), alpha=0.7)

plt.figure()
plt.plot(df_03['TMAX'] - df_03['TMIN'])
plt.plot(df_22['TMAX'] - df_22['TMIN'])

print(np.mean(df_03['TMAX'] - df_03['TMIN']))
print(np.mean(df_22['TMAX'] - df_22['TMIN']))

plt.figure()

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_03.index:
    month = int(df_03['DATE'][i][5:7])
    month_lists[month - 1].append(df_03['TMAX'][i])
month_averages = [np.mean(i) for i in month_lists]
# print(month_averages)
plt.bar(months, month_averages, alpha=0.8)

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_22.index:
    month = int(df_22['DATE'][i][5:7])
    month_lists[month - 1].append(df_22['TMAX'][i])
month_averages = [np.mean(i) for i in month_lists]
# print(month_averages)
plt.bar(months, month_averages, alpha=0.8)

plt.figure()

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_03.index:
    month = int(df_03['DATE'][i][5:7])
    month_lists[month - 1].append(df_03['TMIN'][i])
month_averages = [np.mean(i) for i in month_lists]
# print(month_averages)
plt.bar(months, month_averages, alpha=0.8)

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_22.index:
    month = int(df_22['DATE'][i][5:7])
    month_lists[month - 1].append(df_22['TMIN'][i])
month_averages = [np.mean(i) for i in month_lists]
# print(month_averages)
plt.bar(months, month_averages, alpha=0.8)

plt.figure()

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_03.index:
    month = int(df_03['DATE'][i][5:7])
    month_lists[month - 1].append(df_03['TMAX'][i] - df_03['TMIN'][i])
month_averages = [np.mean(i) for i in month_lists]
# print(month_averages)
plt.bar(months, month_averages, alpha=0.7)

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_22.index:
    month = int(df_22['DATE'][i][5:7])
    month_lists[month - 1].append(df_03['TMAX'][i] - df_22['TMIN'][i])
month_averages = [np.mean(i) for i in month_lists]
# print(month_averages)
plt.bar(months, month_averages, alpha=0.7)

combined_df = pd.DataFrame()
combined_df['TMAX_03'] = df_03['TMAX']
combined_df['TMAX_22'] = df_22['TMAX']
combined_df['TMIN_03'] = df_03['TMIN']
combined_df['TMIN_22'] = df_22['TMIN']

# print(combined_df)

plt.figure()
sns.boxplot(data=combined_df)


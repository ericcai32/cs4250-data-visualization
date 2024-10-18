import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_03 = pd.read_csv('data/pasquotank_2003.csv')
df_22 = pd.read_csv('data/pasquotank_2022.csv')

# Claim #1: Although 2003 and and 2022 initially display similar precipitation
# trends, 2003 had more light rain while 2022 had more moderate to heavy rain.
# Source: https://weatherins.com/rain-guidelines/

# These values are pretty similar for both years.
print("\nTotal Precipitation")
print(np.sum(df_03['PRCP']))
print(np.sum(df_22['PRCP']))

print("\nMean Daily Precipitation")
print(np.mean(df_03['PRCP']))
print(np.mean(df_22['PRCP']))

print("\nNumber of Rainy Days")
print(len(df_03[df_03['PRCP'] > 0]['PRCP']))
print(len(df_22[df_22['PRCP'] > 0]['PRCP']))

# The cumulative sum plot shows that the total precipitation is pretty
# intertwined throughout the length of the years.
plt.figure(figsize=(10, 5))
plt.plot(np.cumsum(df_03['PRCP']), color='teal', label="2003")
plt.plot(np.cumsum(df_22['PRCP']), color='orangered', label="2022")
plt.title("Cumulative Total Precipitation in 2003 and 2022")
plt.xlabel("Time")
plt.ylabel("Precipitation (Inches)")
plt.xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365], ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN"])
plt.grid()
plt.legend()

# However, 2003 has fewer days with light rain, but more than makes up for that
# in moderate to heavy rain.
print("\nNumber and Count of Light and Heavy Rainy Days")
light = .25
print(len(df_03[df_03['PRCP'] <= light]['PRCP']) - len(df_03[df_03['PRCP'] == 0]['PRCP']))
print(len(df_22[df_22['PRCP'] <= light]['PRCP']) - len(df_03[df_03['PRCP'] == 0]['PRCP']))
print(len(df_03[df_03['PRCP'] > light]['PRCP']))
print(len(df_22[df_22['PRCP'] > light]['PRCP']))
print(np.sum(df_03[df_03['PRCP'] <= light]['PRCP']))
print(np.sum(df_22[df_22['PRCP'] <= light]['PRCP']))
print(np.sum(df_03[df_03['PRCP'] > light]['PRCP']))
print(np.sum(df_22[df_22['PRCP'] > light]['PRCP']))

plt.figure(figsize=(5, 8))
bar_heights = [3.95, 6.82]
bar_labels = ["2003", "2022"]
fig = plt.bar(bar_labels, bar_heights)
fig[0].set_color('teal')
fig[1].set_color('orangered')
plt.title("Precipitation From Light Rain")
plt.ylabel("Precipitation (Inches)")
plt.yticks(np.arange(0, 60, 5))
plt.ylim(top=55)
plt.grid(axis="y")

plt.figure(figsize=(5, 8))
bar_heights = [54.22, 49.43]
bar_labels = ["2003", "2022"]
fig = plt.bar(bar_labels, bar_heights)
fig[0].set_color('teal')
fig[1].set_color('orangered')
plt.title("Precipitation From Moderate to Heavy Rain")
plt.ylabel("Precipitation (Inches)")
plt.yticks(np.arange(0, 60, 5))
plt.ylim(top=55)
plt.grid(axis="y")

# Claim #2: 2003 was generally cooler than 2022. One reason for this is
# because their daily minimum temperatures were fairly similar (with 2003
# being slightly more variable) but 2003 had far more days with a high
# temperature below 60 degrees.

print("\nMean Maximum Temperature")
print(np.mean(df_03['TMAX']))
print(np.mean(df_22['TMAX']))
print("\nMean Minimum Temperature")
print(np.mean(df_03['TMIN']))
print(np.mean(df_22['TMIN']))

plt.figure(figsize=(10, 3))
plt.hist(df_03['TMAX'], bins=np.arange(0, 110, 10), color='teal', label='2003', alpha=0.7)
plt.hist(df_22['TMAX'], bins=np.arange(0, 110, 10), color='orangered', label='2022', alpha=0.7)
plt.title("Maximum Daily Temperatures in 2003 and 2022")
plt.ylabel("Days")
plt.xlabel("Temperature (F)")
plt.xticks(np.arange(0, 110, 10))
plt.grid(axis="y")
plt.legend()

plt.figure(figsize=(10, 3))
plt.hist(df_03['TMIN'], bins=np.arange(0, 110, 10), color='teal', label='2003', alpha=0.7)
plt.hist(df_22['TMIN'], bins=np.arange(0, 110, 10), color='orangered', label='2022', alpha=0.7)
plt.title("Maximum Daily Temperatures in 2003 and 2022")
plt.ylabel("Days")
plt.xlabel("Temperature (F)")
plt.xticks(np.arange(0, 110, 10))
plt.grid(axis="y")
plt.legend()

# This is even easier to see with boxplots.
combined_df = pd.DataFrame()
combined_df['2003 Maximums'] = df_03['TMAX']
combined_df['2022 Maximums'] = df_22['TMAX']
combined_df['2003 Minimums'] = df_03['TMIN']
combined_df['2022 Minimums'] = df_22['TMIN']

plt.figure()
sns.boxplot(data=combined_df, palette=['teal', 'orangered', 'teal', 'orangered'])
plt.title("Distributions of Maximum and Minimum Daily Temperatures in 2003 and 2022")
plt.ylabel("Temperature (F)")

# Claim #3: Another major factor that caused 2022 to be generally warmer is
# that it had significantly warmer winters.
months =  ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

plt.figure(figsize=(10,7))

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_03.index:
    month = int(df_03['DATE'][i][5:7])
    month_lists[month - 1].append(df_03['TMAX'][i])
month_averages = [np.mean(i) for i in month_lists]
plt.bar(months, month_averages, color='teal', label="2003", alpha=0.7)

winter = month_averages[-1] + month_averages[0] + month_averages[1]
print(winter / 3)
print((np.sum(month_averages) - winter) / 9)

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_22.index:
    month = int(df_22['DATE'][i][5:7])
    month_lists[month - 1].append(df_22['TMAX'][i])
month_averages = [np.mean(i) for i in month_lists]
plt.bar(months, month_averages, color='orangered', label="2022", alpha=0.7)

print()
winter = month_averages[-1] + month_averages[0] + month_averages[1]
print(winter / 3)
print((np.sum(month_averages) - winter) / 9)

plt.title("Mean Maximum Daily Temperatures")
plt.ylabel("Temperature (F)")
plt.xlabel("Month")
plt.yticks(np.arange(0, 110, 10))
plt.grid(axis="y")
plt.legend()

plt.figure(figsize=(10,7))

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_03.index:
    month = int(df_03['DATE'][i][5:7])
    month_lists[month - 1].append(df_03['TMIN'][i])
month_averages = [np.mean(i) for i in month_lists]
plt.bar(months, month_averages, color='teal', label="2003", alpha=0.7)

month_lists = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in df_22.index:
    month = int(df_22['DATE'][i][5:7])
    month_lists[month - 1].append(df_22['TMIN'][i])
month_averages = [np.mean(i) for i in month_lists]
plt.bar(months, month_averages, color='orangered', label="2022", alpha=0.7)

plt.title("Mean Minimum Daily Temperatures")
plt.ylabel("Temperature (F)")
plt.xlabel("Month")
plt.yticks(np.arange(0, 110, 10))
plt.grid(axis="y")
plt.legend()

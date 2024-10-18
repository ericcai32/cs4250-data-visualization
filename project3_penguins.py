# Questions:
# 1.Which species of penguins has the greatest average body mass?
# 2.Which species of penguins has the longest average flipper length?
# 3.Which species of penguins has the shortest average bill length?
# 4.Which species of penguin has the smallest bill depth?
# 5.What island or islands do Gentoo penguins live on?
# 6.What island or islands do Chinstrap penguins live on?
# 7.What island or islands do Adelie penguins live on?
# 8.Which island has the most penguins living on it?
# 9.Which island has the least number of penguins living on it?
# 10.How many total Adelie penguins are in the data set?
#
# Plots:
# 1. Seaborn average bar chart for body mass: 1
# 2. Seaborn average bar chart for flipper length: 2
# 3. Seaborn average bar chart for bill length: 3
# 4. Seaborn box and whisker plot for bill depth: 4
# 5. Heatmap of penguin count to island: 5, 6, 7, 8, 9

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/P3PenguinData.csv')

sns.set_palette('terrain', n_colors=3)

plt.rcParams.update({'font.size': 8})
plt.figure(figsize=[2, 12])
# 1. Seaborn average bar chart for body mass
plt.subplot(3, 1, 1)
sns.barplot(data=df, x='species', y='body_mass_g', errorbar=None)
plt.title("Avereage Body Mass (g) vs. Species")
plt.ylabel("Avereage Body Mass (g)")
plt.xlabel("")

# 2. Seaborn average bar chart for flipper length: 2
plt.subplot(3, 1, 2)
sns.barplot(data=df, x='species', y='flipper_length_mm', errorbar=None)
plt.title("Average Flipper Length (mm) vs. Species")
plt.ylabel("Avereage Flipper Length (mm)")
plt.xlabel("")

# 3. Seaborn average bar chart for bill length: 3
plt.subplot(3, 1, 3)
sns.barplot(data=df, x='species', y='bill_length_mm', errorbar=None)
plt.title("Avereage Bill Length (mm) vs. Species")
plt.ylabel("Avereage Bill Length (mm)")
plt.xlabel("Species")

plt.subplots_adjust(hspace=0.3)

# 4. Seaborn box and whisker plot for bill depth: 4
plt.figure(figsize=[4.5, 4.5])
sns.boxplot(data=df, x='species', y='bill_depth_mm')
plt.title("Bill Depth (mm) vs. Species")
plt.ylabel("Bill Depth Length (mm)")
plt.xlabel("Species")

# 5. Heatmap of penguin count to island: 5, 6, 7, 8, 9
plt.figure(figsize=[4.5, 4.5])
island_species_df = df.pivot_table(
    values='bill_length_mm',
    index='island',
    columns='species',
    aggfunc=len,
    fill_value=0,
    margins=True,
    margins_name="Total",)
sns.heatmap(island_species_df, cmap='terrain')
for i in range(len(island_species_df)):
    for j in range(len(island_species_df.columns)):
        plt.text(i + 0.5,
                 j + 0.5,
                 island_species_df._get_value(j, i, takeable=True),
                 color='black',
                 verticalalignment='center',
                 horizontalalignment='center')
plt.title("Count of Species per Island")
plt.xlabel("Species")
plt.ylabel("Island")
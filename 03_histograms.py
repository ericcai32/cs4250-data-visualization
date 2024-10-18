import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/nfl.csv')

"""
plt.hist(df['weight_in_lbs'], edgecolor='black', color='green', bins=np.arange(150, 376, 25))
plt.xticks(np.arange(150, 376, 25))
plt.yticks(np.arange(0, 501, 50))
plt.title("Distribution of Weights of NFL Players")
plt.grid(color='gray', axis='y')

plt.figure()
plt.hist(df['weight_in_lbs'], density=True, edgecolor='black', color='#ff6600', bins=np.arange(150, 376, 25))
plt.xticks(np.arange(150, 376, 25))
plt.yticks(np.arange(0, 0.011, 0.001))
plt.title("Density Distribution of Weights of NFL Players")
plt.grid(color='gray', axis='y')


plt.hist(df['height_in_inches'], edgecolor='black', color='green', bins=np.arange(62, 84, 2))
plt.xticks(np.arange(62, 84, 2))
plt.yticks(np.arange(0, 550, 50))
plt.title("Distribution of Heights in Inches of NFL Players")
"""

df_atl = df.loc[df['team'] == 'ATL']
print(f"ATL has {len(df_atl)} players.")
df_car = df.loc[df['team'] == 'CAR']
print(f"CAR has {len(df_car)} players.")

plt.hist(df_car['weight_in_lbs'], label="CAR", edgecolor='black', alpha=0.5, bins=np.arange(175, 376, 25))
plt.hist(df_atl['weight_in_lbs'], label="ATL", edgecolor='black', alpha=0.5, bins=np.arange(175, 376, 25))
plt.legend(loc='best')
plt.title("Comparison of Player Weights: ATL vs CAR")

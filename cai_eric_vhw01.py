import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_men = pd.read_csv('data/Men100m.csv')
df_women = pd.read_csv('data/Women100m.csv')

plt.rcParams["figure.figsize"] = [10, 6]

plt.subplot(1, 2, 1)
plt.plot(df_women['Year'], df_women['Time'], 'go--', linewidth=2, markersize=5)
plt.xticks(np.arange(1900, 2021, 12), fontsize=8)
plt.yticks(np.arange(9.5, 12.35, 0.2))
plt.title("Women 100 Meter Olympic Records")
plt.xlabel("Year")
plt.ylabel("Time in Seconds")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(df_men['Year'], df_men['Time'], 'ro--', linewidth=2, markersize=5)
plt.xticks(np.arange(1900, 2021, 12), fontsize=8)
plt.yticks(np.arange(9.5, 12.35, 0.2))
plt.title("Men 100 Meter Olympic Records")
plt.xlabel("Year")
plt.ylabel("Time in Seconds")
plt.grid(True)

plt.suptitle("Plot submitted by student 441")

plt.savefig('VHWO1-441.png')
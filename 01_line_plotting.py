import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/Women100m.csv')

plt.rcParams["figure.figsize"] = [8, 4]
plt.plot(df['Year'], df['Time'], 'rx--')
plt.xticks(np.arange(1928, 2025, 8))
plt.yticks(np.arange(10.5, 12.25, 0.1))
plt.title("Women's Olympic 100 Meter Records")
plt.xlabel("Seconds")
plt.ylabel("Year")
plt.grid(True)
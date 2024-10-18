import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([99, 80, 56, 95, 45, 80, 91, 70, 70, 60, 56, 95, 100, 10, 60])
df = pd.DataFrame()
df['values'] = values

print(np.median(values))

sns.boxplot(x=values)

print(df['values'].quantile([0, 0.25, 0.5, 0.75, 1]))

plt.savefig('VHW02-S24.png')
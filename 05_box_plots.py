import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/nfl.csv')

plt.rcParams['figure.figsize'] = 15, 5
sns.boxplot(x=df['position'], y=df['weight_in_lbs'])

plt.figure()
sns.violinplot(x=df['position'], y=df['weight_in_lbs'])

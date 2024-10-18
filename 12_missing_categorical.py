import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
import pandas as pd
import seaborn as sns

pd.options.display.max_columns = None

dataset = sns.load_dataset('titanic')

dataset = dataset[['embark_town', 'age', 'fare']]

# print(dataset['embark_town'].value_counts())

ax = sns.countplot(data=dataset, x='embark_town')
ax.bar_label(ax.containers[0])

dataset['embark_town'].fillna('Southampton', inplace=True)

plt.figure()
ax = sns.countplot(data=dataset, x='embark_town')
ax.bar_label(ax.containers[0])
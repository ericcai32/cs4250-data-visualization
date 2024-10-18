import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
import pandas as pd
import seaborn as sns

pd.options.display.max_columns = None

dataset = sns.load_dataset('titanic')

dataset = dataset[['survived', 'pclass', 'age', 'fare']]

# print(dataset.isnull().mean())

plt.hist(
    dataset['age'],
    density=True,
    edgecolor='black',
    bins=np.arange(0, 85, 5),
    alpha=0.7,
    label='Original Data')

mean_age = dataset['age'].mean()
median_age = dataset['age'].median()
print(f"The mean age is: {mean_age}.")
print(f"The median age is: {median_age}")

dataset["mean_age"] = dataset['age'].fillna(mean_age)
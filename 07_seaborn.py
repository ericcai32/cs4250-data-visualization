import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams['figure.figsize'] = [8, 6]
sns.set_style("darkgrid")
sns.color_palette()

titanic_data = sns.load_dataset('titanic')

"""
sns.barplot(data=titanic_data,
            x='pclass',
            y='age',
            hue='sex',)
"""

sns.catplot(data=titanic_data,
            x='pclass',
            y='age',
            col='survived',
            hue='sex',
            kind='bar',)


plt.title("Average Age vs. Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Age")
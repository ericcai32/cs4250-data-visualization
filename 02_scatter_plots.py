import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/iris_data.csv")

plt.rcParams['figure.figsize'] = [4, 8]

"""
# Plot the sepal width vs. sepal length, with each species of flower in a
# different color.
plt.subplot(1, 2, 1)
plt.scatter(df['sepal_length'][:50], df['sepal_width'][:50], c='red', label="setosa")
plt.scatter(df['sepal_length'][50:100], df['sepal_width'][50:100], c='green', label="versicolor")
plt.scatter(df['sepal_length'][100:150], df['sepal_width'][100:150], c='orange', label="virginica")

plt.legend(loc='best')
plt.grid(True)
plt.title("Sepal Width vs. Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.xticks(np.arange(4, 9))
plt.yticks(np.arange(1.7, 4.7, .2))

# Plot the sepal width vs. petal length, with each species of flower in a
# different color.
plt.subplot(1, 2, 2)
plt.scatter(df['petal_length'][:50], df['sepal_width'][:50], c='red', label="setosa")
plt.scatter(df['petal_length'][50:100], df['sepal_width'][50:100], c='green', label="versicolor")
plt.scatter(df['petal_length'][100:150], df['sepal_width'][100:150], c='orange', label="virginica")

plt.legend(loc='best')
plt.grid(True)
plt.title("Sepal Width vs. Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.xticks(np.arange(0, 7))
plt.yticks(np.arange(1.7, 4.7, .2))
"""

# Plot the petal width vs. sepal length, with each species of flower in a
# different color.
plt.subplot(2, 1, 1)
plt.scatter(df['sepal_length'][:50], df['petal_width'][:50], c='red', label="setosa")
plt.scatter(df['sepal_length'][50:100], df['petal_width'][50:100], c='green', label="versicolor")
plt.scatter(df['sepal_length'][100:150], df['petal_width'][100:150], c='orange', label="virginica")

plt.legend(loc='best')
plt.grid(True)
plt.ylabel("Petal Width")
plt.xticks(np.arange(5, 9))
plt.yticks(np.arange(0, 3, .5))

# Plot the petal length vs. sepal length, with each species of flower in a
# different color.
plt.subplot(2, 1, 2)
plt.scatter(df['sepal_length'][:50], df['petal_length'][:50], c='red', label="setosa")
plt.scatter(df['sepal_length'][50:100], df['petal_length'][50:100], c='green', label="versicolor")
plt.scatter(df['sepal_length'][100:150], df['petal_length'][100:150], c='orange', label="virginica")

plt.legend(loc='best')
plt.grid(True)
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.xticks(np.arange(5, 9))
plt.yticks(np.arange(1, 8))
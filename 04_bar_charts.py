import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/iris_data.csv')
print(df.head)

"""
y = df['petal_length']
y_setosa = np.average(y[:50])
y_versicolor = np.average(y[50:100])
y_virginica = np.average(y[100:150])

x = np.array(["Setosa", "Versicolor", "virginica"])
y = np.array([y_setosa, y_versicolor, y_virginica])
plt.bar(x, y, color='green', width=0.75)
"""

y_values = df['petal_length']
setosa_y_median = np.median(y_values[:50])
versicolor_y_median = np.median(y_values[50:100])
virginica_y_median = np.median(y_values[100:150])
x = np.array(["Setosa", "Versicolor", "Virginica"])
y = np.array([setosa_y_median, versicolor_y_median, virginica_y_median])
plt.barh(x, y, height=0.75, color='purple')

plt.xticks(np.arange(0, 7, 0.5))
plt.grid(True, color='gray', axis='x')
plt.title("Comparison of Median Petal Lengths of Iris Flowers")
plt.ylabel("Types of Iris Flowers")
plt.xlabel("Median Petal Length")

plt.text(1.1, "Setosa", setosa_y_median, color='white')
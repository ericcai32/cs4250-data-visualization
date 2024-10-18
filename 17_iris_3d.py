import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/iris_data.csv')
gr = df.groupby('species').mean()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b']

x = [2, 4, 6]
y = [7, 7, 7]
z = [0, 0, 0]
dx = [1, 1, 1]
dy = [0.5]
dz = gr['sepal_length']
ax.bar3d(x, y, z, dx, dy, dz, color=colors)

x = [2, 4, 6]
y = [5, 5, 5]
z = [0, 0, 0]
dx = [1, 1, 1]
dy = [0.5]
dz = gr['sepal_width']
ax.bar3d(x, y, z, dx, dy, dz, color=colors)

x = [2, 4, 6]
y = [3, 3, 3]
z = [0, 0, 0]
dx = [1, 1, 1]
dy = [0.5]
dz = gr['petal_length']
ax.bar3d(x, y, z, dx, dy, dz, color=colors)

x = [2, 4, 6]
y = [1, 1, 1]
z = [0, 0, 0]
dx = [1, 1, 1]
dy = [0.5]
dz = gr['petal_width']
ax.bar3d(x, y, z, dx, dy, dz, color=colors)

ax.set_xticklabels(["", "Setosa", "", "Versicolor", "", "Virginica"])
ax.set_yticklabels(["", "", "Petal Width", "", "Petal Length", "", "Sepal Width", "", "Sepal Length"])
ax.set_yticks(np.arange(0, 9, 1))
ax.set_title("Bar Plot of Average Iris Data Parameters")
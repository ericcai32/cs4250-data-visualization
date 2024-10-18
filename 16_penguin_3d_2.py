import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/P3PenguinData.csv')
df = df.drop('island', axis=1)
gr = df.groupby('species').mean()
print(gr)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b']

x = [2, 4, 6]
y = [3, 3, 3]
z = [0, 0, 0]
dx = [1, 1, 1]
dy = [0.5]
dz = gr['bill_length_mm']

ax.bar3d(x, y, z, dx, dy, dz, color=colors)
ax.set_xticklabels(["Adelie", "Chinstrap", "Gentoo"])
ax.set_yticks(np.arange(0, 6, 1))
ax.set_title("Bar Plot of Penguin Data")

x = [2, 4, 6]
y = [1, 1, 1]
z = [0, 0, 0]
dx = [1, 1, 1]
dy = [0.5]
dz = gr['bill_depth_mm']

ax.bar3d(x, y, z, dx, dy, dz, color=colors)
ax.set_yticklabels(["", "", "Bill Depth", "Bill Length", "", ""])

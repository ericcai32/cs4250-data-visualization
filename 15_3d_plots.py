import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
df = pd.read_csv('Data/iris_data.csv')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

species_df = df[df['species'] == 'setosa']
x = species_df['sepal_length']
y = species_df['sepal_width']
z = species_df['petal_length']
ax.scatter(x, y, z, c='blue', label='Setosa')

species_df = df[df['species'] == 'versicolor']
x = species_df['sepal_length']
y = species_df['sepal_width']
z = species_df['petal_length']
ax.scatter(x, y, z, c='orange', label='Versicolor')

species_df = df[df['species'] == 'virginica']
x = species_df['sepal_length']
y = species_df['sepal_width']
z = species_df['petal_length']
ax.scatter(x, y, z, c='green', label='Virginica')

ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")
ax.set_title("3D Plot of Iris Data Set")
plt.legend()
plt.show()
"""

df = pd.read_csv('Data/P3PenguinData.csv')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

print(df.columns)

species_df = df[df['species'] == 'Adelie']
x = species_df['bill_length_mm']
y = species_df['bill_depth_mm']
z = species_df['flipper_length_mm']
ax.scatter(x, y, z, c='blue', label='Adelie')

species_df = df[df['species'] == 'Chinstrap']
x = species_df['bill_length_mm']
y = species_df['bill_depth_mm']
z = species_df['flipper_length_mm']
ax.scatter(x, y, z, c='orange', label='Chinstrap')

species_df = df[df['species'] == 'Gentoo']
x = species_df['bill_length_mm']
y = species_df['bill_depth_mm']
z = species_df['flipper_length_mm']
ax.scatter(x, y, z, c='green', label='Gentoo')

ax.set_title("3D Plot of Penguin Data Set")
ax.set_xlabel("bill_length_mm")
ax.set_ylabel("bill_depth_mm")
ax.set_xlabel("flipper_length_mm")
plt.legend()
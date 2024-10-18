import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d

plt.figure(figsize=(12, 12))
points = np.array([[1, 3], [5, 1], [9, 2], [7, 7], [3, 9], [5, 5], [3, 6], [10, 9], [8, 4]])

vor = Voronoi(points)
print(vor.vertices)
print()
print(vor.ridge_points)

fig = voronoi_plot_2d(vor)
plt.show()
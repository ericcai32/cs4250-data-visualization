import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay

plt.figure(figsize=(12, 12))
points = np.array([[1, 3], [5, 1], [9, 2], [7, 7], [3, 9], [5, 5], [3, 6], [10, 9], [8, 4]])

tri = Delaunay(points)
print(tri.simplices)
print()
print(points[tri.simplices])
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.grid()

plt.triplot(points[:,0], points[:,1], tri.simplices, c="black")
plt.plot(points[:,0], points[:,1], "o")
plt.show()

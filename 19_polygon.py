import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12, 12))
points = np.array([[1, 3], [5, 1], [9, 2], [7, 7], [3, 9], [5, 5], [3, 6], [10, 9], [8, 4]])

plt.xlim(0, 12)
plt.ylim(0, 12)
plt.grid()
for k in range(9):
    plt.scatter(points[k, 0], points[k, 1], s=200)
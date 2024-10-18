import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import Voronoi, voronoi_plot_2d

df = pd.read_csv("data/JointNCWeather.csv")

points = np.zeros((15, 2))

for i in range(15):
    points[i, 0] = df['LONGITUDE'][i]
    points[i, 1] = df['LATITUDE'][i]
    
print(points)

vor = Voronoi(points)
print(vor.vertices)
print()
print(vor.ridge_points)

fig = voronoi_plot_2d(vor)
plt.show()
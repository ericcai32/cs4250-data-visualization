import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

df = pd.read_csv("data/iris_data.csv")

plt.rcParams['figure.figsize'] = [12, 12]

headings = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
titles = ["", "Setosa is red", "Versicolor is green", "Virginica is orange"]

for i in range(16):
    plt.subplot(4, 4, i + 1)
    
    if i > 11:
        plt.xlabel(labels[i - 12])
    if i % 4 == 0:
        plt.ylabel(labels[int(i / 4)])
    if i < 4:
        plt.title(titles[i])
    if i % 5 == 0:
        continue
    
    plt.scatter(df[headings[i % 4]][:50], df[headings[math.floor(i / 4)]][:50], c='red')
    plt.scatter(df[headings[i % 4]][50:100], df[headings[math.floor(i / 4)]][50:100], c='green')
    plt.scatter(df[headings[i % 4]][100:150], df[headings[math.floor(i / 4)]][100:150], c='orange')
    
    plt.grid(True)

plt.suptitle("Plot submitted by student 441")

plt.savefig('P01-441.png')
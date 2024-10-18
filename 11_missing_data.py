import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import nan

dataset = pd.read_csv('data/pima-indians-diabetes.csv', header=None)
pd.options.display.max_columns = None

# Summarize the data set
print(dataset.shape)
print(dataset.head(10))
print(dataset.describe())

num_missing = (dataset[[1, 2, 3, 4, 5]] == 0).sum()
print(num_missing)

# dataset.dropna
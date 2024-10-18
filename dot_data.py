import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

guesses = pd.read_csv('data/class_dots.csv')
print(guesses)
df = pd.read_csv('data/correct_dots.csv')
print(df)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/tips.csv')

sns.scatterplot(x='total_bill', y='tip', data=df)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/P3PenguinData.csv')

pd.options.display.max_columns = None
print(df.head)

chinstrap_df = df[df['species'] == 'Chinstrap']
print(chinstrap_df.head)

species = ['Adelie', 'Chinstrap']
species_df = df[df['species'].isin(species)]
print(species_df.head)

dream_species_df = df[df['species'].isin(species) & (df['island'] == 'Dream')]
print(dream_species_df.head)

sns.countplot(dream_species_df, x='species')
plt.text(-.04, len(dream_species_df[dream_species_df['species'] == 'Adelie']) - 10, len(dream_species_df[dream_species_df['species'] == 'Adelie']))
plt.text(.96, len(dream_species_df[dream_species_df['species'] == 'Chinstrap']) - 10, len(dream_species_df[dream_species_df['species'] == 'Chinstrap']))
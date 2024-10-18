import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None) 

df = sns.load_dataset('titanic')

print(df.columns)

sh_df = df[df['embark_town'] == 'Southampton']

for pclass in range(1, 4):
    print(f"\nPCLASS = {pclass}")
    class_df = sh_df[sh_df['pclass'] == pclass]
    
    class_count = len(class_df)
    print(f"Total in Class {pclass}: {class_count}")
    
    survived_df = class_df[class_df['survived'] == 1]
    survived_count = len(survived_df)
    print(f"Total Survived in Class {pclass}: {survived_count}")
    
    survivor_percentage = survived_count / class_count
    print(f"% Survivors For Class {pclass}: {survivor_percentage * 100}")
    
    sexes = ['male', 'female']
    for sex in sexes:
        full_sex_df = class_df[class_df['sex'] == sex]
        full_sex_count = len(full_sex_df)
        print(f"Total {sex.title()}s: {full_sex_count}")
        sex_df = survived_df[survived_df['sex'] == sex]
        sex_count = len(sex_df)
        print(f"Total {sex.title()} Survivors In Class {pclass}: {sex_count}")
        
        sex_survived_percentage = sex_count / full_sex_count
        print(f"% {sex.title()} Survivors For Class {pclass}: {sex_survived_percentage * 100}")

print(sh_df.sort_values('age', ascending=False).head(20))
print(sh_df.sort_values('fare', ascending=False).head(20))
print(len(sh_df[sh_df['age'] > 50]))
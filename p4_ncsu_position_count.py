import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

file = input("Enter your file: ")
ncsu = pd.read_csv(file)

departments = [
    'Biological And Agricultural En',
    'Architecture',    
    'Computer Science-engr',
    'Chemistry'
    ]

plot_titles = [
    'Biological and Agricultural Engineering - College of Agriculture and Life Sciences',
    'Architecture - College of Design',
    'Computer Science - College of Engineering',
    'Chemistry - College of Sciences'
    ]

plt.figure(figsize=[16.25, 22.5])

for i in range(4):
    department_ncsu = ncsu[ncsu['EMPLOYEE HOME DEPARTMENT'] == departments[i]]
        
    plt.subplot(2, 2, i + 1)
    ax = sns.countplot(department_ncsu, x='JOB CATEGORY', order=['Lecturer', 'Assistant Professor', 'Associate Professor', 'Professor'])
    ax.bar_label(ax.containers[0])
    plt.title(plot_titles[i])
    plt.ylabel("Number of Positions")
    plt.xlabel("Job Category")
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
    'Biological and Agricultural Engineering — College of Agriculture and Life Sciences',
    'Architecture - College of Design',
    'Computer Science - College of Engineering',
    'Chemistry - College of Sciences'
    ]

plt.figure(figsize=[16.25, 22.5])

for i in range(4):
    department_ncsu = ncsu[ncsu['EMPLOYEE HOME DEPARTMENT'] == departments[i]]
        
    plt.subplot(2, 2, i + 1)
    ax = sns.barplot(department_ncsu, x='JOB CATEGORY', y='EMPLOYEE ANNUAL BASE SALARY', order=['Lecturer', 'Assistant Professor', 'Associate Professor', 'Professor'], errorbar=None)
    plt.title(plot_titles[i])
    ax.bar_label(ax.containers[0])
    plt.ylabel("Average Salary")
    plt.xlabel("Job Category")
    
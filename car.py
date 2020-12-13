# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:34:25 2020

@author: msado
"""


import  pandas as pd

data = pd.read_csv("C:/Users/msado/Documents/CarMax.csv") 

print(data)
data.head()


data.groupby('insert_num')['subsequent_purchases'].head().sort_values(ascending = False)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
matplotlib inline              

plt.figure(figsize=(8,6))                                                                                            
plt.rcParams['patch.force_edgecolor'] = True      
ratings_mean_count['rating_counts'].hist(bins=50)
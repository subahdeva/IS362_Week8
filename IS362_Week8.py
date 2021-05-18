#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt %matplotlib inline
import seaborn as sns

df = pd.read_fwf('auto-mpg.data', header=None)
columns = ['mpg',
          'cylinders',
          'displacement',
          'horsepower',
          'weight',
          'acceleration',
          'model_yr',
          'origin',
          'car_name']
df.columns = columns

df.horsepower = df.horsepower.replace('?', np.nan)
df.horsepower = pd.to_numeric(df.horsepower)


origins = {1: 'USA', 
          2: 'Asia',
          3: 'Europe'}

df.origin = df.origin.map(origins)

distribution_of_cylinders = sns.countplot(x="cylinders", hue='origin' ,data=df)
plt.xlabel("Distribution of Cylinders",size = 20)
plt.ylabel("Count",size = 20)


df.head(10)

#df.info()


# In[11]:


relationship_between_horsepower_and_weight = sns.regplot(x="horsepower", y="weight", data=df, color='m')
plt.title('The Relationship between Horsepower and Weight', fontsize=20)
plt.xlabel("Horsepower",size = 15)
plt.ylabel("Weight",size = 15)


# In[13]:


MPG_Over_Time_by_Origin = sns.lmplot(x='model_yr', y='mpg', hue='origin', data=df)
plt.title('MPG Over Time by Origin', fontsize=22)
plt.xlabel('Model Year', fontsize=15)
plt.ylabel('Miles Per Gallon', fontsize=15)


# In[ ]:





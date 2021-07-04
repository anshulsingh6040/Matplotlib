#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# In[2]:


df = pd.read_csv(r'C:\Users\NEW\Downloads\winequality-red.csv', delimiter = ';')


# In[3]:


df.head()


# In[4]:


fig, ax = plt.subplots(nrows = 1, ncols = 2)
print(ax)
plt.show()


# In[5]:


fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex = True)
ax[0].scatter(df['fixed acidity'], df['pH'], ec = 'k',
             color = 'skyblue')
ax[0].set_ylabel('pH')
ax[0].set_title('Relation b/w Acidity & pH')


ax[1].scatter(df['fixed acidity'], df['volatile acidity'], ec = 'k',
             color = 'skyblue')
ax[1].set_xlabel('Fixed Acidity')
ax[1].set_ylabel('Volatile Acidity')
ax[1].set_title('Relation b/w Acidities')
plt.tight_layout()
plt.show()


# In[6]:


fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (10,10))
ax[0,0].scatter(df['fixed acidity'], df['volatile acidity'], ec = 'k',
             color = 'slateblue')
ax[0,0].set_xlabel('Fixed Acidity')
ax[0,0].set_ylabel('Volatile Acidity')
ax[0,0].set_title('Relation b/w Acidities')


ax[0,1].bar(df['quality'], df['alcohol'],
           color = 'red')
ax[0,1].set_ylabel('Alcohol')
ax[0,1].set_xlabel('Quality')
ax[0,1].set_title('Relation Alcohol & Quality')


ax[1,0].scatter(df['fixed acidity'], df['pH'], ec = 'k',
             color = 'skyblue')
ax[1,0].set_ylabel('pH')
ax[1,0].set_xlabel('Fixed Acidity')
ax[1,0].set_title('Relation b/w Acidity & pH')

freq, bins = np.histogram(df['fixed acidity'], bins = 15)
ax[1,1].hist(df['fixed acidity'], ec = 'k',
            bins = bins)
ax[1,1].set_xlabel('Fixed Acidity')
ax[1,1].set_ylabel('Frequency')
ax[1,1].set_title('Distribution of Fixed Acidity')


fig.suptitle('Key Indicators for Red wine')

plt.tight_layout()
plt.show()


# In[ ]:





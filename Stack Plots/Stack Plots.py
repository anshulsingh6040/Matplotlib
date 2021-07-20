#!/usr/bin/env python
# coding: utf-8

# <h1><center>Stack Plots</center></h1>
# A stack plot is a plot that shows the whole data set with easy visualization of how each part makes up the whole. Each constituent of the stack plot is stacked on top of each other. It shows the part makeup of the unit, as well as the whole unit.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#plt.style.available --to see all available styles


# In[2]:


colors = ['#CD6155','#5499C7','#AF7AC5','#48C9B0','#52BE80','#F4D03F']


# In[3]:


frog = pd.read_csv(r'C:\Users\abc\Desktop\STATISTICAL THINKING PART 2\frog_tongue.csv',
                  skiprows = 14)
bank = pd.read_csv(r'C:\Users\abc\Desktop\stock.csv')


# In[4]:


emp1 = [5, 3, 4, 5, 1, 2, 3, 1]
emp2 = [6, 5, 5, 8, 2, 6, 8, 5]
emp3 = [2, 6, 7, 4, 1, 7, 2, 6]
days = [1, 2, 3, 4, 5, 6, 7, 8]


# In[5]:


plt.stackplot(days, emp1, emp2, emp3)
plt.show()


# In[6]:


plt.stackplot(days, emp1, emp2, emp3, labels = ['Emp1','Emp2','Emp3'])
plt.xlabel('Days')
plt.ylabel('Working hours')
plt.legend()
plt.show()


# In[7]:


plt.stackplot(days, emp1, emp2, emp3, labels = ['Emp1','Emp2','Emp3'],
             linewidth = 1, ec='k',
             alpha = 0.7)
plt.xlabel('Days')
plt.ylabel('Working hours')
plt.legend()
plt.show()


# In[8]:


frog.head()


# In[9]:


frog1 = frog.iloc[:,2:7]
frog1.columns


# In[10]:


trial = pd.pivot_table(index = 'trial number',
                      values = ['impact force (mN)', 'impact time (ms)',
       'impact force / body weight', 'adhesive force (mN)'],
                      aggfunc = 'mean',
                      data = frog1)


# In[11]:


trial


# In[12]:


plt.stackplot(trial.index, trial['impact force (mN)'], trial['impact time (ms)'], linewidth = 1,
             ec = 'k',
             alpha = 0.7)
plt.show()


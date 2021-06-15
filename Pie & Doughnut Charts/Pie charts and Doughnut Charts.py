#!/usr/bin/env python
# coding: utf-8

# <h1><center>Pie Charts & Doughut Charts</center></h1>

# Pie charts are nothing but a big circle. They are really easy to interpret and represent a circle that is sliced into pieces (like a pizza) based on some categories. The pie chart as a whole shows 100% data but individual slices show their own contribution to the data.
# 
# 
# Doughnut Charts are basically the same as Pie Charts, with just a hole in the middle. It is often viewed as a modification to pie charts. Doughnut charts, on the other hand, eliminates the need to compare the size or area of the slice and shifts the focus on the length of the arc, which in turn is easy to measure.
# 
# Both Doughnut Charts and Pie charts share the same advantages and disadvantages. 
# 
# ADVANTAGES :
# 1. Easy to interpret and widely used.
# 2. It visualizes data as a fractional part of the whole and which leads to effective communication.
# 3. Data comparison is very easily done at a glance.
# 
# DISADVANTAGES:
# 1. Becomes hard to interpret and read if data contains too many slices or categories.
# 2. Pie charts only represent one series of data and hence we need to draw more than one in order to compare two or more series of data.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# In[2]:


data = pd.read_csv(r'E:\Downloads\salary_cleaned.csv')


# In[3]:


data.head()


# In[4]:


colors = ['#CD6155','#5499C7','#AF7AC5','#48C9B0','#52BE80','#F4D03F']


# In[5]:


slices = [45, 56, 34, 20]


# In[6]:


plt.pie(slices)
plt.show()


# In[7]:


plt.pie(slices, wedgeprops = {'edgecolor':'k'})
plt.show()


# In[8]:


plt.pie(slices, wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold'},
       autopct = '%1.2f')
plt.show()


# In[9]:


plt.pie(slices, wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold'},
       autopct = '%1.2f%%')
plt.show()


# In[10]:


data.head()


# In[11]:


data['workclass'].unique()


# In[12]:


work_count = data['workclass'].value_counts().tolist()


# In[13]:


work_label = data['workclass'].value_counts().index


# In[14]:


plt.pie(work_count, labels = work_label,
       autopct = '%1.2f%%',
       colors = colors[:3],
       wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold', 'size':10})
plt.show()


# In[15]:


plt.pie(work_count, labels = work_label,
       autopct = '%1.2f%%',
       colors = colors[:3],
       wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold', 'size':10},
       shadow = True)
plt.show()


# In[16]:


plt.pie(work_count, labels = work_label,
       autopct = '%1.2f%%',
       colors = colors[:3],
       wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold', 'size':10},
       shadow = True,
       explode = [0.1, 0, 0])
plt.show()


# In[17]:


plt.pie(work_count, labels = work_label,
       autopct = '%1.2f%%',
       colors = colors[:3],
       wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold', 'size':15},
       shadow = True,
       explode = [0.1, 0, 0],
       startangle = 90,
       pctdistance = 0.8,
       radius = 2)
plt.show()


# In[18]:


data.head()


# In[19]:


data['occupation'].nunique()


# In[20]:


plt.pie(data['occupation'].value_counts().tolist(), labels = data['occupation'].value_counts().index,
       autopct = '%1.2f%%',
       wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold', 'size':10},
       shadow = True,
       startangle = 90,
       pctdistance = 0.8,
       radius = 2)
plt.show()


# In[21]:


plt.pie(work_count, labels = work_label,
       autopct = '%1.2f%%',
       colors = colors[:3],
       wedgeprops = {'edgecolor':'k'},
       textprops = {'fontweight':'bold', 'size':15},
       shadow = True,
       startangle = 90,
       pctdistance = 0.8,
       radius = 1.5)

plt.pie(work_count, colors = ['white'])
plt.show()


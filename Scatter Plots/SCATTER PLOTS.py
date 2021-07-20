#!/usr/bin/env python
# coding: utf-8

# <h1><center>SCATTER PLOTS</center></h1>

# Another way of converting your continuous variables to charts is to scatter plots. Scatter plots require two continuous variables in order to plot them and hence they are bivariate.
# 
# Scatter plots are also very common in practice when it comes to identifying if there exists a relationship between variables or not. They can also depict if two continuous variables have a positive correlation, negative correlation, or no correlation.
# 
# **ADVANTAGES:**
# 1. Highlights correlation
# 2. Often depicts minimum, maximum, and outliers in the data.
# 3. Shows if there is a trend in the data.

# **DISADVANTAGES :**
# 1. Only applicable to continuous variables.
# 2. Sometimes the results are inconclusive.

# In[1]:

#importing required libraries/modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# In[2]:


plt.style.available


# In[3]:


plt.style.use('seaborn')


# In[4]:


colors = ['#CD6155','#5499C7','#AF7AC5','#48C9B0','#52BE80','#F4D03F']


# In[5]:


auto = pd.read_csv(r'E:\Downloads\auto-mpg.csv')


# In[6]:


x = [130.0, 165.0, 150.0, 150.0, 140.0, 198.0, 220.0, 215.0, 225.0, 190.0, 170.0, 160.0, 
     150.0, 225.0, 95.0, 95.0, 97.0, 85.0, 88.0, 46.0]

y = [307., 350., 318., 304., 302., 429., 454., 440., 455., 390., 383.,
       340., 400., 455., 113., 198., 199., 200.,  97.,  97.]

magnitude = [12. , 11.5, 11. , 12. , 10.5, 10. ,  9. ,  8.5, 10. ,  8.5, 10. ,
        8. ,  9.5, 10. , 15. , 15.5, 15.5, 16. , 14.5, 20.5]

colors = [6, 4, 2, 5, 3, 1, 8, 8, 9, 9, 1, 4, 5, 4, 2, 6, 1, 9, 7, 7]

hex_color = ['#CD6155','#5499C7','#AF7AC5','#48C9B0','#52BE80','#F4D03F']


# In[7]:


plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[8]:


plt.scatter(x, y, color = hex_color[4])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[9]:


plt.scatter(x, y, color = hex_color[4], s = 200)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[10]:


plt.scatter(x, y, color = hex_color[4], s = 200,
           edgecolor = 'k',
           alpha = 0.7)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[11]:


plt.scatter(x, y, color = hex_color[4], s = 200,
           edgecolor = 'k',
           alpha = 0.7,
           marker = '+')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[12]:


plt.scatter(x, y, color = hex_color[4], s = 200,
           edgecolor = 'k',
           alpha = 0.7,
           marker = 'D')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[13]:


plt.scatter(x, y, color = hex_color[4], s = 200,
           edgecolor = 'k',
           alpha = 0.7,
           marker = '^')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[14]:


plt.scatter(x, y, color = hex_color[4], s = 200,
           edgecolor = 'k',
           alpha = 0.7,
           marker = 'v')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[15]:


plt.scatter(x, y, color = hex_color[4], s = 200,
           edgecolor = 'k',
           alpha = 0.7,
           marker = '*')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[16]:


auto.head()


# In[17]:


plt.figure(figsize = (10,8))
plt.scatter(auto['mpg'], auto['displacement'], 
           edgecolor = 'k',
           s = auto['acceleration'],
           sizes = (50,200),
            c = auto['horsepower'],
            cmap = 'Blues'
           )
plt.xlabel('MPG')
plt.ylabel('Displacement')

color_bar = plt.colorbar()
color_bar.set_label('Horsepower')

plt.show()


# In[18]:


plt.figure(figsize = (10,8))
plt.scatter('displacement', 'horsepower', data = auto,
           alpha = 0.7,
           edgecolor = 'k',
           s = 'weight',
            c = 'mpg',
            cmap = 'Reds',
           sizes = (50,200))
plt.xlabel('Displacement')
plt.ylabel('Horsepower')

color_bar = plt.colorbar()
color_bar.set_label('MPG')

plt.show()


# In[ ]:





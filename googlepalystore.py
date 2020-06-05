#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


app_details = pd.read_csv("C:/Users/Balabhadrapatruni/Desktop/googleplaystore.csv/googleplaystore.csv", sep = ',')
app_details.shape


# In[3]:


app_details


# In[4]:


app_details.describe()


# In[5]:


app_details.corr()


# # DATA CLEANING
# 

# In[6]:


app_details.head()


# In[7]:


app_details.isnull().any()


# In[8]:


app_details = app_details.dropna()
app_details.mean()


# In[9]:


app_details.isnull().any()


# In[10]:


app_details


# In[11]:


install = []
for i in app_details['Installs']:
    k = i[:-1]
    type(k)
    install.append(int(i[:-1].replace(',','')))
app_details['Installs'] = install


# In[12]:


category_wise = app_details.groupby(['Category']).mean()
category_wise


# In[13]:


cat = app_details.Category.unique()


# # Data Vizualizing

# # Below is the  line graph between category of app and its rating

# In[14]:


#line graph
plt.figure(figsize = (10,5))
plt.plot(cat, category_wise['Rating'])
plt.xticks(rotation = 'vertical')

plt.show()


# # Below is the  bar graph between category of app and its rating

# In[18]:



#bar grapj
plt.figure(figsize = (15,5))
plt.bar(cat,category_wise['Rating'])
plt.xticks(rotation = 'vertical')
plt.ylim(3.5,5)
plt.show()


# # Below is the line graph between category of app and its downloads

# In[16]:


#line graph
plt.figure(figsize = (10,5))
plt.plot(cat, category_wise['Installs'])
plt.xticks(rotation = 'vertical')

plt.show()


# # Below is the bar graph between category of app and its downloads

# In[17]:


plt.figure(figsize = (15,5))
plt.bar(cat,category_wise['Installs'])
plt.xticks(rotation = 'vertical')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





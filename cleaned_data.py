#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mlflow
import mlflow.sklearn
import pandas as pd


# #### Reading the imported_formatted_data.csv from Part B

# In[2]:


df = pd.read_csv('C:/Users/jcaye/D602Task2/imported_formatted_data.csv')


# #### Filtering data to only departures from LAX

# In[5]:


df = df[df['ORG_AIRPORT'] == 'LAX']


# #### Data Cleaning

# ##### Removing duplicates

# In[18]:


df = df.drop_duplicates()


# ##### Removing unnecessary column FL_DATE

# In[23]:


df = df.drop(columns='FL_DATE')


# #### Exporting the cleaned_data.csv

# In[26]:


df.to_csv('cleaned_data.csv', index=False)





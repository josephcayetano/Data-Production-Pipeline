#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mlflow
import mlflow.sklearn
import pandas as pd


# #### Reading the flight data

# In[3]:


df = pd.read_csv('C:/Users/jcaye/D602Task2/flightdata.csv')


# #### Renaming the columns

# In[4]:


df.rename(columns={
    'DAY_OF_MONTH': 'DAY',
    'ORIGIN': 'ORG_AIRPORT',
    'DEST': 'DEST_AIRPORT',
    'CRS_DEP_TIME': 'SCHEDULED_DEPARTURE',
    'DEP_TIME': 'DEPARTURE_TIME',
    'DEP_DELAY': 'DEPARTURE_DELAY',
    'CRS_ARR_TIME': 'SCHEDULED_ARRIVAL',
    'ARR_TIME': 'ARRIVAL_TIME',
    'ARR_DELAY': 'ARRIVAL_DELAY'
}, inplace=True)


# #### Filling NA with 0 and converting the datatypes of float columns to integer

# In[9]:


df.fillna(0, inplace=True)


# In[10]:


df[['DEPARTURE_TIME', 'DEPARTURE_DELAY','ARRIVAL_TIME', 'ARRIVAL_DELAY']] = df[
    ['DEPARTURE_TIME', 'DEPARTURE_DELAY','ARRIVAL_TIME', 'ARRIVAL_DELAY']
].astype(int)


# #### Exporting the imported_formatted_data.csv

# In[14]:


df.to_csv('imported_formatted_data.csv', index=False)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # EDA On Fuel Dataset for Stage A

# ### First we import our dependencies and load the data (read) into the notebook

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style='darkgrid')


# In[10]:


url = "https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv"
fuel = pd.read_csv(url)


# #### Next we take a snapshot of the data, checking summary statictics, looking at a few rows to familiarize ourselves with the data

# In[11]:


fuel.head()


# In[18]:


fuel.shape


# In[14]:


fuel.describe()


# #### We have a fairly large dataset with 29,000 rows and mean values for all numerical columns listed above. We will proceed to explore the dataset and answer a few questions

# In[45]:


fuel.duplicated().any()


# In[47]:


fuel.isnull().sum()


# In[49]:


fuel.groupby('fuel_type_code_pudl').first()


# In[ ]:





# In[ ]:





# In[15]:


fuel['fuel_qty_burned'].skew()


# In[16]:


fuel['fuel_qty_burned'].kurtosis()


# In[17]:


fuel.isnull().sum()


# In[19]:


fuel.corr()


# In[43]:


fuel.groupby(['fuel_type_code_pudl','report_year']).sum()


# In[35]:


fuel.groupby('report_year').mean().sort_values(by='fuel_cost_per_unit_delivered').tail()


# In[ ]:





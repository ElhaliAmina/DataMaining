#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip uninstall pandas-profiling')


# In[3]:


get_ipython().system('pip install pandas-profiling[notebook,html]')


# In[4]:


import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
from pandas_profiling.utils.cache import cache_file


# In[8]:


demographic = 'C:/Users/Hp/Desktop/master BIOMSCS/BIOMSCS_S3/DM/projet/Data/DEMO_J.xlsx'
d_demographic= pd.read_excel(demographic,
sheet_name=0,
header=0,
index_col=False,
keep_default_na=True
)


# In[9]:


profile1 = ProfileReport(d_demographic, title="démographie  Dataset", html={'style': {'full_width': True}}, sort="None")


# In[10]:


profile1.to_notebook_iframe()


# In[ ]:





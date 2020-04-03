#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd

from sqlalchemy import create_engine


# In[27]:


engine = create_engine(r"sqlite:///C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\salesdata.db")


# In[28]:


# Getting the table names 



# In[29]:


sql = "select name from sqlite_master"
"where type = 'table';"


# In[30]:


sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[31]:


# Selecting the table from the database

sql_table = "select * from scores"

score_data_df = pd.read_sql(sql_table, engine)

score_data_df.head()


# In[ ]:





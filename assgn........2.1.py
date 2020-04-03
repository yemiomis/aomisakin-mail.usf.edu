#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pandas as pd
import numpy as np
import glob
data = pd.DataFrame()
for i in glob.glob(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\weekly_call_data.xlsx"):
    df = pd.read_excel(i)
    data = data.append(df,ignore_index=True)
data.head()


# In[ ]:





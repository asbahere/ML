#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
data=pd.read_csv (r'C:\Users\bmsce\Desktop\testdemo.csv')
data


# In[32]:


d =np.array(data)[:,:-1]
print("n the attributes are: ",d)


# In[33]:


target = np.array(data)[:,-1]
print("n the target is: ",target)


# In[40]:


def findS(c,t):
    for i, val in enumerate(t):
         if val == 'Yes':
            specific_hypothesis = c[i].copy()
            break

             
    for i, val in enumerate(c):
        if t[i] == 'Yes':
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
        return specific_hypothesis
    
print("n the Final Hypthesis is:",findS(d,target))


# In[ ]:





# In[ ]:





# In[ ]:





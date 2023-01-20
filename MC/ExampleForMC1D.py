#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import random
import math
import numpy as np
import matplotlib as plot

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def Function(x):
    return math.sin(x)

a=0
b=np.pi
N=1000

xrand=random.uniform(a,b,N)



# In[3]:


intergral = 0
for i in range(len(xrand)):
    intergral += Function(xrand[i])
    
answer = (b-a)/float(N)*intergral

print(answer)
    


# In[ ]:





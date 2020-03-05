#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement

# Q.1 Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[2]:





# Q.2 Implement a Python program to generate all sentences where subject is in ["Americans",
# "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
# 
#     Hint: Subject,Verb and Object should be declared in the program as shown below.
#     subjects=["Americans ","Indians"]
#     verbs=["play","watch"]
#     objects=["Baseball","Cricket"]
# 
#     Output should come as below:
#     Americans play Baseball.
#     Americans play Cricket.
#     Americans watch Baseball.
#     Americans watch Cricket.
#     Indians play Baseball.
#     Indians play Cricket.
#     Indians watch Baseball.
#     Indians watch Cricket.

# In[19]:


subjects=["Americans ","Indians "]
verbs=["play","watch"]
objects=["Baseball","Cricket"]


# In[20]:


for i in subjects:
    for j in verbs:
        for k in objects:
            print(i+""+ j+" " + k+ ".")


# Q.3 Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# 
#     HINT: Such a matrix with a geometric progression in each row is named for Alexandre Theophile Vandermonde.

# In[27]:


import numpy as np
a = np.array([1, 2, 3, 5])
b = 3
print(np.vander(a, b))


# In[ ]:





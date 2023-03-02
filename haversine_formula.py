#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[3]:


def haversine(row):
    lon1 = row['Lon1']
    lat1 = row['Lat1']
    lon2 = row['Lon2']
    lat2 = row['Lat2']
    ###########################################
    R = 6371e3 #earth radius 6,371km
    pi1 = lat1 * math.pi/180
    pi2 = lat2 * math.pi/180
    delta_pi = (lat2 - lat1) * math.pi/180
    delta_lambda = (lon2 - lon1) * math.pi/180
    ###########################################
    a = math.sin(delta_pi/2) * math.sin(delta_pi/2) + math.cos(pi1) * math.cos(pi2) * math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import astropy
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time

# import data
dateobs = np.loadtxt('C:/Users/demar/Documents/ASTR320/Hw2/dateobs.txt', dtype = np.str)
starid = list(np.loadtxt('C:/Users/demar/Documents/ASTR320/Hw2/rmaster_phot_v2.dat',dtype = np.str, usecols = [3]))
data = np.loadtxt('C:/Users/demar/Documents/ASTR320/Hw2/rmaster_phot_v2.dat', usecols=[1,2])


# In[36]:


# adjust data to plot:
starid = list([s.strip('fsubbfrmaster') for s in starid])
starid = list([s.replace('fsubbfrmaster', '') for s in starid])
starid = list([s.strip('.fits') for s in starid])
starid = list([s.replace('.fits', '') for s in starid])
statid = np.asarray([float(i) for i in starid])

x = data[:,1]
magnitude = data[:,0]

## need to convert observation dates from date to mjd
date = Time(dateobs, format = 'isot', scale='utc').mjd
time = []
for i in range (0,len(date)):
    for j in range(0,30):
        time = np.append(time, x[(j + ((i)*30))] + date[i])


# In[39]:


SI = np.tile(np.arange(30),53)
plt.scatter(time,magnitude,s=1,c = SI)
plt.gca().invert_yaxis()
plt.title('Eclipsing Binary Star Magnitude versus Time')
plt.xlabel('Time (mjd)')
plt.ylabel('Magnitude')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





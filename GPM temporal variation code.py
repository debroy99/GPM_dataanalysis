#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[118]:


mfdata_DIR='E:\Debjyoti\Project Work\GPM Data\Data 23-05-14\gpm*'
df=xr.open_mfdataset(mfdata_DIR, parallel=True)


# In[119]:


df


# In[120]:


###### cropping data to required lat-lon extent
min_lon = 76.00
min_lat = 27.50
max_lon = 78.50
max_lat = 30.00

df1 = df.sel(lat=slice(min_lat,max_lat), lon=slice(min_lon,max_lon))


# In[121]:


pricp=df1.precipitationCal
time=df1.time


# In[122]:


#avgeraging over lat lon
pricp_avg=pricp.mean(dim=['lat','lon'])


# In[124]:


#conversation from half-hourly precipitation to hourly precipitation
pricp_avg1=[]  #hourly precipitation
for i in range(0 ,48,2):
    pricp_avg1.append(pricp_avg[i]+pricp_avg[i+1])
    


# In[125]:


pricp_avg1=np.asarray(pricp_avg1)


# In[126]:


pricp_avg1.shape


# In[127]:


#arranging time step
time= np.arange (0,24)
time.shape
print (time)


# In[128]:


## plotting the temporal variation
import os
if not os.path.exists('E:/Debjyoti/Project Work/Images/Dt23-05-2014'):
    os.makedirs('E:/Debjyoti/Project Work/Images/Dt23-05-2014')
    
plt.figure(figsize=(15,10))
plt.bar(time,pricp_avg1)
plt.plot(time,pricp_avg1, color="red")
plt.xticks(np.arange(0,24, step=2), fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Datetime (UTC)', fontsize=18)
plt.ylabel('Precipitation (mm)', fontsize=18)
plt.title('Temporal variation of hourly precipitation on 23-May-2014', fontsize=20 )
plt.savefig('E:/Debjyoti/Project Work/Images/Dt23-05-2014/temporal variation of hourly rainfall.tiff')


# In[ ]:





# In[ ]:





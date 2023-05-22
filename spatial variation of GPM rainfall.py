#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd


# In[2]:


shapefile_path = 'E:\Debjyoti\Project Work\Delhi shapefile\Delhi.shp'
shapefile1 = gpd.read_file(shapefile_path)


# In[3]:


shapefile1['geometry'].head()


# In[88]:


mfdata_DIR='E:\Debjyoti\Project Work\GPM Data\Data 23-05-14\gpm*'
df=xr.open_mfdataset(mfdata_DIR, parallel=True)


# In[89]:


#cropping data to required lat-lon extent
min_lon = 75.50
min_lat = 26.50
max_lon = 79.00
max_lat = 30.00

df1 = df.sel(lat=slice(min_lat,max_lat), lon=slice(min_lon,max_lon))


# In[90]:


pricp=df1.precipitationCal
time=df1.time


# In[91]:


lat=df1.lat
lon=df1.lon


# In[92]:


time


# In[96]:


pricp1=pricp[28:30,:,:]
pricp1


# In[97]:


pricp2=np.cumsum(pricp1,axis=0)
pricp3=pricp2.mean(dim='time')
pricp3.shape
#np.nanmax(pricp2)


# In[98]:


#precipitation contour plot
ax=plt.contourf(lon,lat,pricp3,cmap='GnBu')
cbar=plt.colorbar(ax)
plt.clim(0,10)
cbar.set_label('Precipitation(mm)', fontsize=18,rotation=270, labelpad=16)
plt.xlabel('longitude', fontsize=18)
plt.ylabel('latitude', fontsize=18)
plt.title('Precipitation at 14 UTC', fontsize=15)
ax=shapefile1.boundary.plot(ax=plt.gca(),color='k')
plt.savefig('E:\Debjyoti\Project Work\Images\Dt23-05-2014\spatial variation of hourly rainfall at 14UTC.tiff')
plt.show()


# In[93]:


pricp_accu=np.cumsum(pricp,axis=0)
#pricp_avg=pricp_accu.mean(dim='time')
#np.nanmax(pricp_accu)
pricp_accu.shape


# In[94]:


pricp_accu1=pricp_accu[47,:,:]
pricp_accu1


# In[95]:


#total accumulated precipitation contour plot
cf=plt.contourf(lon,lat,pricp_accu1,cmap='GnBu')
cbar=plt.colorbar(cf)
plt.clim(0,40)
cbar.set_label('Precipitation(mm)', fontsize=18,rotation=270, labelpad=16)
plt.xlabel('longitude', fontsize=18)
plt.ylabel('latitude', fontsize=18)
plt.title('Total Accumulated Precipitation on 23-May-2014', fontsize=15)
ax=shapefile1.boundary.plot(ax=plt.gca(),color='k')
plt.savefig('E:/Debjyoti/Project Work/Images/Dt23-05-2014/total accumulated rainfall on 23th May, 2014.tiff')
plt.show()


# In[ ]:





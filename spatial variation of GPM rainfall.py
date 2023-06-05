#!/usr/bin/env python
# coding: utf-8
#author=@debroy99

####################################################################
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
#######################################################################

#importing the shapefile
shapefile_path = 'path_shapefile(.shp)'
shapefile1 = gpd.read_file(shapefile_path)
shapefile1['geometry'].head()

####################################################################

#importing the gpm datasets
mfdata_DIR= 'path of downloaded data'
df=xr.open_mfdataset(mfdata_DIR, parallel=True)

########################################################################

#cropping data to required lat-lon extent
min_lon = 'min lon'
min_lat = 'min lat'
max_lon = 'max lon'
max_lat = 'max lat'

df1 = df.sel(lat=slice(min_lat,max_lat), lon=slice(min_lon,max_lon))


######################################################################

pricp=df1.precipitationCal
time=df1.time
lat=df1.lat
lon=df1.lon
#########################Plotting for specific time########################################
################################################################################
#extracting data for required for specific hour #half hourly data [so, two datasets]
pricp1=pricp['index1':'index2',:,:]
pricp1
#########################################################################
#taking sum to convert it into hourly data for specific hour

pricp2=np.cumsum(pricp1,axis=0)
pricp3=pricp2.mean(dim='time') #taking mean about time dimesion
pricp3.shape
#np.nanmax(pricp2)

###############################################################################

#plotting rainfall for specific hour 
ax=plt.contourf(lon,lat,pricp3,cmap='GnBu')
cbar=plt.colorbar(ax)
plt.clim(0,10)
cbar.set_label('Precipitation(mm)', fontsize=18,rotation=270, labelpad=16)
plt.xlabel('longitude', fontsize=18)
plt.ylabel('latitude', fontsize=18)
plt.title('Precipitation at 14 UTC', fontsize=15)
ax=shapefile1.boundary.plot(ax=plt.gca(),color='k')
plt.savefig('path_savefigfile\spatial variation of hourly rainfall at XXUTC.tiff')
plt.show()
###################################Accumulated rainfall#############################################
###########################################################################
#taking sum over time to compute accumulated rainfall from half-hourly rainfall data
pricp_accu=np.cumsum(pricp,axis=0)
#pricp_avg=pricp_accu.mean(dim='time') #taking mean over time dimension #not required
#np.nanmax(pricp_accu)
pricp_accu.shape
pricp_accu1=pricp_accu['index of last row',:,:]  #last row gives the accumulated rainfall
pricp_accu1

###############################################################################################

#plotting total accumulated rainfall
cf=plt.contourf(lon,lat,pricp_accu1,cmap='GnBu')
cbar=plt.colorbar(cf)
plt.clim(0,40)
cbar.set_label('Precipitation(mm)', fontsize=18,rotation=270, labelpad=16)
plt.xlabel('longitude', fontsize=18)
plt.ylabel('latitude', fontsize=18)
plt.title('Total Accumulated Precipitation on 23-May-2014', fontsize=15)
ax=shapefile1.boundary.plot(ax=plt.gca(),color='k')
plt.savefig('path_savefigfile/total accumulated rainfall.tiff')
plt.show()








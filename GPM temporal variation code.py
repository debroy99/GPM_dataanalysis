#!/usr/bin/env python
# coding: utf-8
#author= @debroy99



################################################################
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

################################################################
#Importing datasets using xarray liberary

mfdata_DIR='path_gpm datasets'
df=xr.open_mfdataset(mfdata_DIR, parallel=True)
df
###################################################################

###### cropping data to required lat-lon extent
min_lon = min lon
min_lat = min lat
max_lon = max lon
max_lat = max lat

df1 = df.sel(lat=slice(min_lat,max_lat), lon=slice(min_lon,max_lon))

#####################################################################
pricp=df1.precipitationCal
time=df1.time


######################################################################


#avgeraging over lat lon
pricp_avg=pricp.mean(dim=['lat','lon'])

##########################################################################

#conversation from half-hourly precipitation to hourly precipitation
pricp_avg1=[]  #hourly precipitation
for i in range(0 ,len(pricp_avg),2):
    pricp_avg1.append(pricp_avg[i]+pricp_avg[i+1])
    
##########################################################################
pricp_avg1=np.asarray(pricp_avg1)
pricp_avg1.shape
#########################################################################
#arranging time step
time= np.arange (0,24)
time.shape
print (time)
########################################################################
## plotting the temporal variation

plt.figure(figsize=(15,10))
plt.bar(time,pricp_avg1)
plt.plot(time,pricp_avg1, color="red")
plt.xticks(np.arange(0,24, step=2), fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Datetime (UTC)', fontsize=18)
plt.ylabel('Precipitation (mm)', fontsize=18)
plt.title('Temporal variation of hourly precipitation on 23-May-2014', fontsize=20 )
#######################################################################################

#saving the fig file
import os                                       
if not os.path.exists('path_savefigfile'):
    os.makedirs('path_savefigfile')
    
plt.savefig('path_savefigfile/temporal variation of hourly rainfall.tiff')






#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, os

import netCDF4

# 1. cole du lautaret simulation:
path = '/home/tintino/Documents/snowschool_lautaret_2018/Crocus_files/forcing/'
name = 'FORCING_2017080106_2018021406.nc'

id_sim = 16

### display variable names
forcing = netCDF4.Dataset(path+name) # classic opening of netCDF file

for k in forcing.variables.iterkeys():
    print k

# convert time to timestamp, figure precip
df = pd.DataFrame()
df['time'] = pd.to_datetime(forcing.variables.get('time')[:], unit='h' ,origin='2017-08-01 06:00:00')
df['Tair'] = forcing.variables.get('Tair')[:,id_sim]-273.15
df['wind_speed'] = forcing.variables.get('Wind')[:,id_sim]
df['wind_dir'] = forcing.variables.get('Wind_DIR')[:,id_sim]
df['humidity'] = forcing.variables.get('HUMREL')[:,id_sim]
df['rain'] = forcing.variables.get('Rainf')[:,id_sim]
df['snow'] = forcing.variables.get('Snowf')[:,id_sim]
df['precip'] = df.snow*3600 + df.rain*3600
df['To'] = np.abs(df.Tair*0.0)

df.set_index('time', inplace=True)

# select subset of time

df_winter = df.loc[df.index >= pd.to_datetime('2017-11-01')]
df_winter = df_winter.loc[df_winter.index <= pd.to_datetime('2018-02-17')]


# make plot like for Finse with Tair, wind speed, and precip, crop to Nov 1
fig, ax = plt.subplots(5, 1, sharex=True)
ax[0].plot(df_winter.index, df_winter.Tair, color='k')

ax[0].grid()
#ax[0].axhline(0, color='k')
ax[0].set_ylabel('Air temp. [degC]')
ax[0].fill_between(df_winter.index, df_winter.To,
                   df_winter.Tair, where=df_winter.Tair>df_winter.To, color='tomato')
ax[0].fill_between(df_winter.index, df_winter.To,
                   df_winter.Tair, where=df_winter.Tair<df_winter.To, color='lightblue')

# change color for wind above 6m/s
ax[1].plot(df_winter.index, df_winter.wind_speed, color='k')
ax[1].fill_between(df_winter.index,(df_winter.wind_speed*0+4), df_winter.wind_speed, where=df_winter.wind_speed>(df_winter.wind_speed*0+4), color='yellowgreen')

ax[1].grid(linestyle=':')
ax[1].set_ylabel('Wind speed [m/s]')

ax[2].plot(df_winter.index, df_winter.precip.cumsum(), color='k')
ax[2].grid(linestyle=':')
ax[2].set_ylabel('Precipitation cumul [kg/m2]')

    
ax[3].plot(df_winter.index, df_winter.snow, color='k')
ax[3].grid(linestyle=':')
ax[3].set_ylabel('Snow fall rate [kg/m2/s]')


ax[4].plot(df_winter.index, df_winter.rain, color='k')
ax[4].grid(linestyle=':')
ax[4].set_ylabel('Rain fall rate [kg/m2/s]')


#================================================

data['To'] = 0
data['Uth'] = 6
data['FF_24'] = data.FF.rolling(window=4, min_periods=2).mean()

f, ax = plt.subplots(4,1,sharex=True)
ax[1].plot(data.FF_24, color='k', alpha=.5)
ax[1].fill_between(data.index,data.Uth, data.FF_24, where=data.FF_24>data.Uth, color='yellowgreen')
ax[1].grid(linestyle=':')
ax[1].set_ylim([0,20])
ax[1].set_ylabel('Wind speed (m/s)')
ax[2].plot(data.TA, color='k', alpha=.5)
ax[2].fill_between(data.index,
                   data.To,
                   data.TA,
                   where=data.TA>data.To,
                   color='tomato')
ax[2].fill_between(data.index,data.To, data.TA, where=data.TA<data.To, color='lightblue')
ax[2].grid(linestyle=':')
ax[2].set_ylabel('Air temperature (degC)')
ax[0].plot(data.SA, color='k', alpha=.5)
ax[0].grid(linestyle=':')

ax[0].set_ylim([0,65])
ax[0].set_ylabel('Snow depth (cm)')
ax[3].plot(data.RR_24.dropna(), color='k', alpha=.5)
ax[3].set_ylim([0,45])
ax[3].set_ylabel('Daily precip (mm)')
ax[3].grid(linestyle=':')
months = mdates.MonthLocator()
monthsFmt = mdates.DateFormatter('%b')
days = dates.DayLocator()
ax[3].xaxis.set_major_locator(months)
ax[3].xaxis.set_major_formatter(monthsFmt)
ax[3].xaxis.set_minor_locator(days)
f.subplots_adjust(hspace=0)




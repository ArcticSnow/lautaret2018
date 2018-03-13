#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

from pylab import *
import netCDF4
import sys
import matplotlib.pyplot as plt
sys.path.append('/home/tintino/Documents/snowschool_lautaret_2018/github/SSWS_notebook_clean/snowtools_git')
#os.environ["PYTHONPATH"]="PYTHONPATH:/home/tintino/Documents/snowschool_lautaret_2018/SSWS_notebook_clean/snowtools_git/"
from plots.proReader import ProReader
from utils.obsReader import ObsReader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

id_sim = 0

#========================================================
# 1. open the three simulations at col du lautaret:
name_f06 = '/home/tintino/Documents/snowschool_lautaret_2018/Crocus_files/PRO_2017080106_2018021706_f06.nc'
pro_f06=ProReader(name_f06, point=id_sim) # add point argument if several points (,point=i)

begin="2017110100"
end="2018021700"


obs = ObsReader('/home/tintino/Documents/snowschool_lautaret_2018/github/201802141205_PitForest.caaml')

# 1. cole du lautaret simulation:
path = '/home/tintino/Documents/snowschool_lautaret_2018/Crocus_files/forcing/'
name = 'FORCING_2017080106_2018021406.nc'



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


#========================================================
# Combine weather and crocus snow evolution
fig, axes = plt.subplots(5, 1, sharex=False, sharey=False, figsize=(12,12))
pro_f06.plot(axes[0], "grain", b=begin,e=end, legend=False, cbar_on=False)
pro_f06.plot(axes[3], "temp", b=begin,e=end, cbar_on=False)
#pro_f06.plot(axes[2], "age", b=begin,e=end, cbar_on=False)


axes[1].plot(df_winter.index, df_winter.rain, color='k')
axes[1].grid()
#axes[0].axhline(0, color='k')
axes[1].set_ylabel('Rain precip. [mm]')
axes[1].set_xlim(['2017-11-01','2018-02-17'])

axes[2].plot(df_winter.index, df_winter.snow, color='k')
axes[2].grid()
#axes[0].axhline(0, color='k')
axes[2].set_ylabel('Snow precip. [mm]')
axes[2].set_xlim(['2017-11-01','2018-02-17'])


axes[4].plot(df_winter.index, df_winter.Tair, color='k')
axes[4].grid()
#axes[0].axhline(0, color='k')
axes[4].set_ylabel('Air temp. [degC]')
axes[4].set_xlim(['2017-11-01','2018-02-17'])
axes[4].fill_between(df_winter.index, df_winter.To,
                   df_winter.Tair, where=df_winter.Tair>df_winter.To, color='tomato')
axes[4].fill_between(df_winter.index, df_winter.To,
                   df_winter.Tair, where=df_winter.Tair<df_winter.To, color='lightblue')
plt.show()

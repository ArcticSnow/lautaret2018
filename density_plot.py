#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, os


#===============================================
# include functions here

dens_df = pd.read_csv('all_data/snow_distrib/depth_density_all.csv', na_values='na')

dens_df.date = pd.to_datetime(dens_df.date)
print dens_df.columns

#===============================================
# 1. Snow depth distribution plot
dens_df.SD_cm.mean()
dens_df.SD_cm.std()

plt.figure()
plt.hist(dens_df.SD_cm, bins=20, label='Alll; samples = 143')
plt.hist(dens_df.SD_cm.loc[dens_df.date==pd.to_datetime('2018/02/14')], bins=20, label='Feb 14; samples = 36', histtype='step', linewidth=3)
plt.hist(dens_df.SD_cm.loc[dens_df.date==pd.to_datetime('2018/02/15')], bins=20, label='Feb 15; samples = 107', histtype='step', linewidth=3)
plt.legend()
plt.title('Snow Depth Histogram')
plt.xlabel('Snow Depth (cm)')


plt.figure()
plt.hist(dens_df.SD_cm, bins=20, label='All; samples = 143', cumulative=True, normed=True)
plt.hist(dens_df.SD_cm.loc[dens_df.date==pd.to_datetime('2018/02/14')], bins=20, label='Feb 14; samples = 36', histtype='step', linewidth=3, cumulative=True, normed=True)
plt.hist(dens_df.SD_cm.loc[dens_df.date==pd.to_datetime('2018/02/15')], bins=20, label='Feb 15; samples = 107', histtype='step', linewidth=3, cumulative=True, normed=True)
plt.legend()
plt.title('Normalized Cumulative Snow Depth Distribution')
plt.xlabel('Snow Depth (cm)')

#==============================================================
# 2. SWE tube density plots

plt.figure()
dens_df.density_kgm3.loc[dens_df.method=='fed_sampler'].hist(alpha=.8)

plt.figure()
plt.scatter(dens_df.SD_cm.loc[dens_df.method=='fed_sampler'], dens_df.density_kgm3.loc[dens_df.method=='fed_sampler'])
plt.xlabel('Snow depth (sm)')
plt.ylabel('Density (kg/m3)')

#==============================================================
# 3. Compare bulk density from the three methods: SWE tube, small cutter, and micropen

plt.figure()
dens_df.boxplot('density_kgm3',by='method', notch=True)
plt.title('Bulk density measurements intercomparison')
plt.ylabel('Density (kg/m3)')



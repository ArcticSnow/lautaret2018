# script to plot and compare observation and CROCUS output

from pylab import *
import netCDF4
import sys
import matplotlib.pyplot as plt
sys.path.append('/home/tintino/Documents/snowschool_lautaret_2018/github/SSWS_notebook_clean/snowtools_git')
#os.environ["PYTHONPATH"]="PYTHONPATH:/home/tintino/Documents/snowschool_lautaret_2018/SSWS_notebook_clean/snowtools_git/"
from plots.proReader import ProReader


#========================================================
# 1. open the three simulations at col du lautaret:
name_f06 = '/home/tintino/Documents/snowschool_lautaret_2018/Crocus_files/PRO_2017080106_2018021706_f06.nc'
name_c13 = '/home/tintino/Documents/snowschool_lautaret_2018/Crocus_files/PRO_2017080106_2018021706_c13.nc'
name_b92 = '/home/tintino/Documents/snowschool_lautaret_2018/Crocus_files/PRO_2017080106_2018021706_b92.nc'

croc_f06 = netCDF4.Dataset(name_f06) # classic opening of netCDF file
for i in croc_f06.variables.iterkeys():
    print i

def print_sim_param(input_file, poi=19):
    '''
    Functiont to print the parameter of the simulation for a given index (point of interest)
    :param input_file: paht to the crocus output file
    :param poi: point of interest (int)
    :return: nan
    '''

    ### display variable names
    crocus = netCDF4.Dataset(input_file)  # classic opening of netCDF file
    # WSN_T_ISBA = SWE (time, Number_of_Tile, Number-of_points)
    # DSN_T_ISBA = Snow depth (time, Number_of_Tile, Number-of_points)
    # print crocus.variables
    massif = crocus.variables['massif_num']  # 15 is Oisans;
    elevation = crocus.variables['ZS']
    aspect = crocus.variables['aspect']
    slope = crocus.variables['slope']
    ### select number between 0 and 35 and see what combination you got. For investigation maybe usefull to see the netcdf file
    ### with a simple netcdf viewer like ncview (linux command line)
    information_poi = "massif: " + str(massif[poi]) + str(" elevation: ") + str(elevation[poi]) + str(
        " aspect: ") + str(aspect[poi]) + str(" slope: ") + str(slope[poi])
    print information_poi
    return information_poi


for i in range(0, 30):
    print_sim_param(name_f06, i)

print_sim_param(name_f06, 16)

pro_f06=ProReader(name_f06, point=16) # add point argument if several points (,point=i)
pro_c13=ProReader(name_c13, point=16)
pro_b92=ProReader(name_b92, point=16)

#=============================================================================
# Comparing the three simulation for a given point of interest
date='2018021518'
fig, axes = plt.subplots(1, 5, sharex=False, sharey=True, figsize=(20, 6))
pro_f06.plot_date(axes[0], "grain", date=date)
depth, temp = pro_f06.plot_date(axes[1], "temp", date=date, color='b')
depth, temp = pro_c13.plot_date(axes[1], "temp", date=date, color='red')
depth, temp = pro_b92.plot_date(axes[1], "temp", date=date, color='green')
depth2, rho = pro_f06.plot_date(axes[2], "rho", date=date)
depth2, rho = pro_c13.plot_date(axes[2], "rho", date=date, color='red')
depth2, rho = pro_b92.plot_date(axes[2], "rho", date=date, color='green')
depth3, swe = pro_f06.plot_date(axes[3], "swe", date=date)
depth3, swe = pro_c13.plot_date(axes[3], "swe", date=date, color='red')
depth3, swe = pro_b92.plot_date(axes[3], "swe", date=date, color='green')
depth4, ssa = pro_f06.plot_date(axes[4], "ssa", date=date)
depth4, ssa = pro_c13.plot_date(axes[4], "ssa", date=date, color='red')
depth4, ssa = pro_b92.plot_date(axes[4], "ssa", date=date, color='green')
axes[1].set_xlim(260,274)
axes[2].set_xlim(0,1000)
axes[0].set_ylabel('Depth (m)')
axes[0].set_title('Simulation f06')
plt.title(print_sim_param(name_f06, 16),loc='right')
plt.show()


# Comparing the grain stratigraphy inbetween the three simulation
date='2018021518'
fig, axes = plt.subplots(1, 3, sharex=False, sharey=True, figsize=(20,6))
pro_f06.plot_date(axes[0], "grain", date=date)
pro_c13.plot_date(axes[1], "grain", date=date)
pro_b92.plot_date(axes[2], "grain", date=date)
axes[0].set_ylabel('Depth (m)')
axes[0].set_title('simulation f06')
axes[1].set_title('simulation c13')
axes[2].set_title('simulation b92')
#plt.title(print_sim_param(name_f06, 16),loc='right')
plt.show()




#===========================================================================
## display the seasonnal evolution of one variable
begin="2017110100"
end="2018021700"

# Simulation f06
fig, axes = plt.subplots(5, 1, sharex=True, sharey=False, figsize=(12,12))
pro_f06.plot(axes[0], "grain", b=begin,e=end)
pro_f06.plot(axes[1], "temp", b=begin,e=end)
pro_f06.plot(axes[2], "rho", b=begin,e=end)
pro_f06.plot(axes[3], "ssa", b=begin,e=end)
pro_f06.plot(axes[4], "age", b=begin,e=end)
## possible variables to plot : tel, ram, age, swe, temp, ...
plt.show()


# Simulation c13
fig, axes = plt.subplots(5, 1, sharex=True, sharey=False, figsize=(12,12))
pro_c13.plot(axes[0], "grain", b=begin,e=end)
pro_c13.plot(axes[1], "temp", b=begin,e=end)
pro_c13.plot(axes[2], "rho", b=begin,e=end)
pro_c13.plot(axes[3], "ssa", b=begin,e=end)
pro_c13.plot(axes[4], "age", b=begin,e=end)
## possible variables to plot : tel, ram, age, swe, temp, ...
plt.show()


# Simulation b92
fig, axes = plt.subplots(5, 1, sharex=True, sharey=False, figsize=(12,12))
pro_b92.plot(axes[0], "grain", b=begin,e=end)
pro_b92.plot(axes[1], "temp", b=begin,e=end)
pro_b92.plot(axes[2], "rho", b=begin,e=end)
pro_b92.plot(axes[3], "ssa", b=begin,e=end)
pro_b92.plot(axes[4], "age", b=begin,e=end)
## possible variables to plot : tel, ram, age, swe, temp, ...
plt.show()




# Combine weather and crocus snow evolution
fig, axes = plt.subplots(4, 1, sharex=False, sharey=False, figsize=(12,12))
pro_f06.plot(axes[0], "grain", b=begin,e=end, legend=False)
pro_f06.plot(axes[1], "temp", b=begin,e=end, cbar_on=False)

fig, axes = plt.subplots(1, 1, sharex=False, sharey=False, figsize=(12,12))
pro_f06.plot(axes, "age", b=begin,e=end, cbar_on=False)



axes[3].plot(df_winter.index, df_winter.Tair, color='k')
axes[3].grid()
#axes[0].axhline(0, color='k')
axes[3].set_ylabel('Air temp. [degC]')
axes[3].fill_between(df_winter.index, df_winter.To,
                   df_winter.Tair, where=df_winter.Tair>df_winter.To, color='tomato')
axes[3].fill_between(df_winter.index, df_winter.To,
                   df_winter.Tair, where=df_winter.Tair<df_winter.To, color='lightblue')
plt.colorbar(ax=axes[3])
plt.show()



#WSN_T_ISBA = SWE (time, Number_of_Tile, Number-of_points)
#DSN_T_ISBA = Snow depth (time, Number_of_Tile, Number-of_points)


#print crocus.variables
#print crocus.variables['aspect']







# extract snow surface temperature



# compare density from obs, and snowpit


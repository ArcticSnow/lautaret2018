
# coding: utf-8

# # Read and plot output Crocus files
#  Marie Dumont and Matthieu Lafaysse, Feb. 2018 

# In[2]:


# modules import
from pylab import *
import netCDF4
from pathlib import Path
sys.path.append('/home/anselm/Seafile/diss/software/python_source_code/SSWS/SSWS_notebook_clean/snowtools_git')
from plots.proReader import ProReader


# In[3]:


## input file name
#home = str(Path.home())
home = '/home/anselm'
folder='/Seafile/diss/io/Col_de_Lautaret/Crocus/'
plot_folder='/Seafile/diss/io/Col_de_Lautaret/Crocus/plots/'
col_porte='PRO_1994100101_1995100100_24h.nc' # example from Col de Porte
###b92, c13, f06 (advise from Marie)
parameterisation='f06'
input_file=home+folder+'PRO_2017080106_2018021706_'+parameterisation+'.nc'


# In[4]:
### display variable names
crocus=netCDF4.Dataset(input_file) # classic opening of netCDF file
#WSN_T_ISBA = SWE (time, Number_of_Tile, Number-of_points)
#DSN_T_ISBA = Snow depth (time, Number_of_Tile, Number-of_points)
# print crocus.variables
massif=crocus.variables['massif_num']             #15 is Oisans; 
elevation=crocus.variables['ZS']
aspect=crocus.variables['aspect']
slope=crocus.variables['slope']
for i in range(0,len(massif),1):

    point_of_interest=i
    print i

    information_poi ="massif: ", massif[point_of_interest], " elevation: ", elevation[point_of_interest], " aspect: ", aspect[point_of_interest], " slope: ", slope[point_of_interest]
    print information_poi


    # In[5]:


    ### Load pro file
    pro=ProReader(input_file,point=point_of_interest) # add point argument if several points (,point=i)


    # In[ ]:


    ### display snow variable profiles for a given date
    import matplotlib.pyplot as plt
    ### names of needed variables: names are the one important for the ProReader obejct, nemaes in brackets are the correcponding
    ### ones if you use the netCDF4.Dataset and their full description
    ### grain (SNOWTYPE; snow layer grain type)
    ### ep (SNOWDZ; snow layer thickness); temp (SNOWTEMP; snow temp layer)
    ### rho (SNOWRHO; snow desnity); swe (WSN_VEG; snow water equivalent layer), ssa (SNOWSSA; snow layer specific surface area)
    ### plot infos about aspect.ele etc in plot
    ### print total snow resevoir; total depth and surface temperature in plot?(dsn_t_iba; total snow depth) (WSN_T_ISBA; total snow resevoir); (TS_ISBA; surface temperature)
    # possible var values are : tel, ram, age, swe, rho, ...
    output_path=home+plot_folder
    date='2018021600'
    output_file1=output_path+date+'-'+parameterisation+'-point_of_interest_'+str(point_of_interest)+'-grain_temperature_density_swe_ssa'

    fig, axes = plt.subplots(1, 5, sharex=False, sharey=True, figsize=(20,6))
    pro.plot_date(axes[0], "grain", date=date)
    depth, temp = pro.plot_date(axes[1], "temp", date=date)
    depth2, rho = pro.plot_date(axes[2], "rho", date=date)
    depth3, swe = pro.plot_date(axes[3], "swe", date=date)
    depth4, ssa = pro.plot_date(axes[4], "ssa", date=date)
    axes[1].set_xlim(260,274)
    axes[2].set_xlim(0,1000)
    axes[0].set_ylabel('Depth (m)')
    plt.title(information_poi,loc='right')
    plt.savefig(output_file1+'.png')
    plt.savefig(output_file1+'.svg')


# In[47]:



# ### display numerical value in the netCDF file
#
#
# print "depth array", depth
# print "temperature array", temp
#
#
# # In[16]:
#
#
# ## display the seasonnal evolution of one variable
# begin="19941201"
# end="19950501"
#
#
# fig, axes = plt.subplots(3, 1, sharex=True, sharey=False, figsize=(12,12))
# pro.plot(axes[0], "grain", b=begin,e=end)
# pro.plot(axes[1], "ssa", b=begin,e=end)
# pro.plot(axes[2], "rho", b=begin,e=end)
# ## possible variables to plot : tel, ram, age, swe, temp, ...
# plt.show()


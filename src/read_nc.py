#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:44:32 2023

@author: ana.becker
"""

import pandas as pd
import xarray as xr
import os
import glob


#13 estacoes# sim = pd.read_csv('data/estacoes.csv')
sim = pd.read_csv('data/estacoes.csv')[['codigo','latitude','longitude']]
sim.reset_index(drop=True, inplace=True)
path = 'data/dados-processados'
nc_files = glob.glob(os.path.join(path,"*.nc"))

 
df_est = pd.DataFrame()
psat = pd.DataFrame()
  
# 1 arquivo com tudo
for i in range(0,len(sim)):
    print('estacao '+ str(sim.codigo[i]) )
    for f in nc_files:
        xr_nc = xr.open_dataset(f).prate 
        #print('estacao ' + str(sim.id_estacao[i]) +' ' + str(???/len(nc_files)*100))
        df_mes = xr_nc.sel(lon = sim.longitude[i], lat = sim.latitude[i], method ='nearest').to_dataframe()
        df_mes['codigo'] = sim.codigo[i]   
        df_est = pd.concat([df_est,df_mes])
    psat = pd.concat([psat,df_est])
psat.to_csv('csv/35e.csv')


# df_est = pd.DataFrame()
# psat = pd.DataFrame()


# #f = '/discolocal/ana.becker/dados-processados/201906.nc'

# # 1 arquivo por estacao
# for i in range(0,len(sim)):
#     print('estacao '+ str(sim.codigo[i]) )
#     for f in nc_files:
#         xr_nc = xr.open_dataset(f).prate 
#         #print('estacao ' + str(sim.id_estacao[i]) +' ' + str(???/len(nc_files)*100))
#         df_mes = xr_nc.sel(lon = sim.longitude[i], lat = sim.latitude[i], method ='nearest').to_dataframe()
#         df_mes['codigo'] = sim.codigo[i]   
#         psat = pd.concat([psat,df_mes])
#     psat.to_csv(f'csv/13e/estacao{sim.codigo[i]}.csv')
#     print(str(i/len(sim)*100)+'%' )


#psat.to_pickle("pkl/psat.pkl")
#psat = pd.read_pickle("pkl/psat.pkl")

#psat.reset_index().rename(columns ={'time':'datahora'}, inplace = True)  

#psat.resample('D', closed='right', label='left')

#psat.reset_index().rename(columns ={'time':'datahora'}).join(psim, on = ['datahora', 'id_estacao'])

#psat.reset_index()




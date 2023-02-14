#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:04:40 2023

@author: ana.becker
"""

import plotly.graph_objects as go 
# Transformando o data frame para o lineplot
#%%
   


df['acumulado_jaxa'] = df.groupby('codigo').prate.cumsum()
df['acumulado_simepar'] = df.groupby('codigo').psim.cumsum()

df_melt = df.melt(value_vars = ['acumulado_jaxa','acumulado_simepar'], id_vars = ['time','lat', 'lon', 'codigo'])
#df_melt.replace('prate', "Satélite JAXA", inplace = True)  
#df_melt.replace('psim', "Simepar", inplace = True)   
df_melt.replace('acumulado_jaxa', "Acumulado JAXA", inplace = True)   
df_melt.replace('acumulado_simepar', "Acumulado Simepar", inplace = True)   



# Lineplot
#%%
for i in range(0,len(sim)):
        df_est = df_melt[df_melt['codigo']== sim.codigo[i]]
        fig = px.line(df_est, 
                      x='time', 
                      y="value", 
                      color='variable',
                      title = f'Estação {str(sim.codigo[i])}',
                      labels = {
                          "value":"Chuva",
                          "time": "Data",
                          "variable":"Fonte"},
                     template = "plotly_white")
        fig.write_html(f'html/[Lineplot] Chuva acumulada/{sim.codigo[i]}.html')
        
        
        
# Totais  Diarios
#%%

df_D = df_melt.set_index(['time']).groupby(['codigo','variable']).resample("D", closed='right', label='right').agg({'value' : np.sum}) 
df_D.reset_index(inplace=True)

for i in range(0,len(sim)):
        df_est = df_D[df_D['codigo']== sim.codigo[i]]
        fig = px.line(df_est, 
                      x='time', 
                      y="value", 
                      color='variable',
                      title = f'Estação {str(sim.codigo[i])}',
                      labels = {
                          "value":"Chuva",
                          "time": "Data",
                          "variable":"Fonte"},
                     template = "plotly_white")
        fig.write_html(f'html/[Lineplot] Chuva acumulada diária/{sim.codigo[i]}.html')



# Totais Mensais
#%%

df_M = df_melt.set_index(['time']).groupby(['codigo','variable']).resample("M", closed='right', label='right').agg({'value' : np.sum})
df_M.reset_index(inplace=True)


for i in range(0,len(sim)):
        df_est = df_M[df_M['codigo']== sim.codigo[i]]
        fig = px.line(df_est, 
                      x='time', 
                      y="value", 
                      color='variable',
                      title = f'Estação {str(sim.codigo[i])}',
                      labels = {
                          "value":"Chuva",
                          "time": "Data",
                          "variable":"Fonte"},
                     template = "plotly_white")
        fig.write_html(f'html/[Lineplot] Chuva acumulada mensal/{sim.codigo[i]}.html')
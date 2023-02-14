#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:22:28 2023

@author: ana.becker
"""
import numpy as np
import pandas as pd
#import seaborn as sns
import plotly.express as px

# Read data
#%%
sim = pd.read_csv('estacoes.csv')
pjaxa = pd.read_csv('csv/13e.csv')
pjaxa['time'] = pd.to_datetime(pjaxa['time'], format='%Y-%m-%d %H:%M:%S')
pjaxa.drop(pjaxa[pjaxa['prate'] < 0].index, inplace = True)
pjaxa = pjaxa.sort_values(by='time')

df = pd.merge(pjaxa, psim, on = ['time','codigo'])



# Dispersão
#%%
for i in range(0,len(sim)):
        df_est = df[df['codigo']== sim.codigo[i]]
        vmax = max(max(df_est['prate']),max(df_est['psim']))+20
        fig = px.scatter(df_est, 
                      x='prate', 
                      y="psim", 
                      title = f'Estação {str(sim.codigo[i])}',
                      labels = {
                          "prate": "Chuva Satélite JAXA",
                          "psim": "Chuva Simepar"},
                     template = "plotly_white")
        fig.add_shape(type = 'line',
                      x0 = 0,
                      y0 = 0,
                      x1 = vmax,
                      y1 = vmax,
                      line = dict(color='black',),
                      xref = 'x',
                      yref = 'y'
                      )
        fig.write_html(f'html/[Scatterplot] Dispersão/{sim.codigo[i]}.html')
        
        
# Dispersao Diaria
#%%

df_H = df.set_index(['time']).groupby('codigo').resample("H", closed='right', label='right').agg({'psim' : np.sum,
                                                                                'prate': np.sum})
#df_H['codigo']=df_H['codigo'].apply(lambda x:str(x))  
df_H.reset_index(inplace=True)
df_H.set_index(['time'],inplace=True)


for i in range(0,len(sim)):
        df_est = df_H[df_H['codigo']== sim.codigo[i]]
        vmax = max(max(df_est['prate']),max(df_est['psim']))+20
        fig = px.scatter(df_est, 
                      x='prate', 
                      y="psim", 
                      title = f'Estação {str(sim.codigo[i])}',
                      labels = {
                          "prate": "Chuva Satélite JAXA",
                          "psim": "Chuva Simepar"},
                     template = "plotly_white")
        fig.add_shape(type = 'line',
                      x0 = 0,
                      y0 = 0,
                      x1 = vmax,
                      y1 = vmax,
                      line = dict(color='black',),
                      xref = 'x',
                      yref = 'y'
                      )
        fig.write_html(f'html/[Scatterplot] Dispersão diária/{sim.codigo[i]}.html')
        
        
# Dispersao Mensal
#%%

df_M = df.set_index(['time']).groupby('codigo').resample("M", closed='right', label='right').agg({'psim' : np.sum,
                                                                                'prate': np.sum})
#df_H['codigo']=df_H['codigo'].apply(lambda x:str(x))  
df_M.reset_index(inplace=True)
df_M.set_index(['time'],inplace=True)


for i in range(0,len(sim)):
        df_est = df_M[df_M['codigo']== sim.codigo[i]]
        vmax = max(max(df_est['prate']),max(df_est['psim']))+20
        fig = px.scatter(df_est, 
                      x='prate', 
                      y="psim", 
                      title = f'Estação {str(sim.codigo[i])}',
                      labels = {
                          "prate": "Chuva Satélite JAXA",
                          "psim": "Chuva Simepar"},
                     template = "plotly_white")
        fig.add_shape(type = 'line',
                      x0 = 0,
                      y0 = 0,
                      x1 = vmax,
                      y1 = vmax,
                      line = dict(color='black',),
                      xref = 'x',
                      yref = 'y'
                      )
        fig.write_html(f'html/[Scatterplot] Dispersão mensal/{sim.codigo[i]}.html')
   
        
# Transformando o data frame para o lineplot
#%%
df_melt = df.melt(value_vars = ['prate','psim' ], id_vars = ['time','lat', 'lon', 'codigo'])
df_melt.replace('prate', "Satélite JAXA", inplace = True)  
df_melt.replace('psim', "Simepar", inplace = True)      
        
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
        fig.write_html(f'html/[Lineplot] Chuva/{sim.codigo[i]}.html')
        
        
# Boxplot
#%%

df_melt_omit = df_melt.drop(df_melt[df_melt['value'] == 0].index)
for i in range(0,len(sim)):
        df_est = df_melt_omit[df_melt_omit['codigo']== sim.codigo[i]]
        fig = px.box(df_est, 
                      x='codigo', 
                      y="value", 
                      color='variable',
                      title = f'Estação {str(sim.codigo[i])}',
                      labels = {
                          "value":"Chuva",
                          "time": "Data",
                          "variable":"Fonte"},
                     template = "plotly_white")
        fig.write_html(f'html/[Boxplot] Chuva/{sim.codigo[i]}.html')








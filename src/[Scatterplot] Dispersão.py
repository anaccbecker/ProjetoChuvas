#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:22:28 2023

@author: ana.becker
"""




# Dispersão horária
#%%
df = pd.read_csv('csv/[H] s j.csv').pivot(index=['time','codigo'],columns='variable',values='value')
df.reset_index(inplace=True)
for i in range(0,len(sim)):
        df_est = df[df['codigo']== sim.codigo[i]]
        vmax = max(np.max(df_est['JAXA']),np.max(df_est['Simepar']))+20
        fig = px.scatter(df_est, 
                      x='JAXA', 
                      y="Simepar", 
                      title = f'Estação {str(sim.codigo[i])} - {str(sim.nome[i])}',
                      labels = {
                          "JAXA": "Chuva horária JAXA (mm)",
                          "Simepar": "Chuva horária Simepar (mm)"},
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
        fig.write_html(f'html/[Scatterplot] Dispersão horária (Simepar-JAXA)/{sim.codigo[i]}.html')
        
        
# Dispersao Diaria (Simepar-JAXA)
#%%

df = pd.read_csv('csv/[D] s j c.csv').pivot(index=['time','codigo'],columns='variable',values='value')
df.reset_index(inplace=True)


for i in range(0,len(sim)):
        df_est = df[df['codigo']== sim.codigo[i]]
        vmax = max(np.max(df_est['JAXA']),np.max(df_est['Simepar']))+20
        fig = px.scatter(df_est, 
                      x='JAXA', 
                      y="Simepar", 
                      title = f'Estação {str(sim.codigo[i])} - {str(sim.nome[i])}',
                      labels = {
                          "JAXA": "Chuva diária JAXA (mm)",
                          "Simepar": "Chuva diária Simepar (mm)"},
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
        fig.write_html(f'html/[Scatterplot] Dispersão diária (Simepar-JAXA)/{sim.codigo[i]}.html')
        
        
# Dispersao Mensal (Simepar-JAXA)
#%%

df = pd.read_csv('csv/[M] s j c.csv').pivot(index=['time','codigo'],columns='variable',values='value')
df.reset_index(inplace=True)


for i in range(0,len(sim)):
        df_est = df[df['codigo']== sim.codigo[i]]
        vmax = max(np.max(df_est['JAXA']),np.max(df_est['Simepar']))+20
        fig = px.scatter(df_est, 
                      x='JAXA', 
                      y="Simepar", 
                      title = f'Estação {str(sim.codigo[i])} - {str(sim.nome[i])}',
                      labels = {
                          "JAXA": "Chuva mensal JAXA (mm)",
                          "Simepar": "Chuva mensal Simepar (mm)"},
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
        fig.write_html(f'html/[Scatterplot] Dispersão mensal (Simepar-JAXA)/{sim.codigo[i]}.html')
   
        
# Dispersao Diaria (Simepar-CPC)
#%%

df = pd.read_csv('csv/[D] s j c.csv').pivot(index=['time','codigo'],columns='variable',values='value')
df.reset_index(inplace=True)


for i in range(0,len(sim)):
        df_est = df[df['codigo']== sim.codigo[i]]
        vmax = max(np.max(df_est['CPC']),np.max(df_est['Simepar']))+20
        fig = px.scatter(df_est, 
                      x='CPC', 
                      y="Simepar", 
                      title = f'Estação {str(sim.codigo[i])} - {str(sim.nome[i])}',
                      labels = {
                          "CPC": "Chuva diária CPC (mm)",
                          "Simepar": "Chuva diária Simepar (mm)"},
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
        fig.write_html(f'html/[Scatterplot] Dispersão diária (Simepar-CPC)/{sim.codigo[i]}.html')
        
        
# Dispersao Mensal (Simepar-JAXA)
#%%

df = pd.read_csv('csv/[M] s j c.csv').pivot(index=['time','codigo'],columns='variable',values='value')
df.reset_index(inplace=True)


for i in range(0,len(sim)):
        df_est = df[df['codigo']== sim.codigo[i]]
        vmax = max(np.max(df_est['CPC']),np.max(df_est['Simepar']))+20
        fig = px.scatter(df_est, 
                      x='CPC', 
                      y="Simepar", 
                      title = f'Estação {str(sim.codigo[i])} - {str(sim.nome[i])}',
                      labels = {
                          "CPC": "Chuva mensal CPC (mm)",
                          "Simepar": "Chuva mensal Simepar (mm)"},
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
        fig.write_html(f'html/[Scatterplot] Dispersão mensal (Simepar-CPC)/{sim.codigo[i]}.html')








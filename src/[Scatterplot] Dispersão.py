#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:22:28 2023

@author: ana.becker
"""


def disp_plot (df_path, x, y):
    df = pd.read_csv(df_path).pivot(index=['time','codigo'],columns='variable',values='value')
    df.reset_index(inplace=True)
    for i in range(0,len(sim)):
            df_est = df[df['codigo']== sim.codigo[i]]
            vmax = max(np.max(df_est[x]),np.max(df_est[y]))+20
            fig = px.scatter(df_est, 
                          x=x, 
                          y=y, 
                          title = f'Estação {str(sim.codigo[i])} - {str(sim.nome[i])}',
                          labels = {
                              "x": f"Chuva horária {x} (mm)",
                              "y": f"Chuva horária {y} (mm)"},
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
            if not os.path.isdir(f'html/[Scatterplot] Dispersão horária ({x}-{y})'):
                os.makedirs(f'html/[Scatterplot] Dispersão horária ({x}-{y})')
            fig.write_html(f'html/[Scatterplot] Dispersão horária ({x}-{y})/{sim.codigo[i]}.html')


# nomes: 'CPC', 'Simepar', 'gsmap_now', 'gsmap_nrt'

# Dispersões horárias
disp_plot('csv/[H] s j.csv', 'Simepar','gsmap_now')
disp_plot('csv/[H] s j.csv', 'Simepar','gsmap_nrt')
disp_plot('csv/[H] s j.csv', 'gsmap_now','gsmap_nrt')

# Dispersões diárias
disp_plot('csv/[D] s j c.csv', 'Simepar','gsmap_now')
disp_plot('csv/[D] s j c.csv', 'Simepar','gsmap_nrt')
disp_plot('csv/[D] s j c.csv', 'gsmap_now','gsmap_nrt')   
disp_plot('csv/[D] s j c.csv', 'Simepar','CPC')
    
# Dispersões mensais
disp_plot('csv/[M] s j c.csv', 'Simepar','gsmap_now')
disp_plot('csv/[M] s j c.csv', 'Simepar','gsmap_nrt')
disp_plot('csv/[M] s j c.csv', 'gsmap_now','gsmap_nrt')   
disp_plot('csv/[M] s j c.csv', 'Simepar','CPC')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:07:06 2023

@author: ana.becker
"""
###### Configurações ######
exec(open('src/_packages.py').read())
cores_plotly =  [   
    '#1f77b4',  # muted blue
    '#ff7f0e',  # safety orange
    '#2ca02c',  # cooked asparagus green
    '#d62728',  # brick red
    '#9467bd',  # muted purple
    '#8c564b',  # chestnut brown
    '#e377c2',  # raspberry yogurt pink
    '#7f7f7f',  # middle gray
    '#bcbd22',  # curry yellow-green
    '#17becf'   # blue-teal
    ]

###### Leitura dos dados ######
# só rodar em caso de novos dados/estações
exec(open('src/read_chuvas_simepar.py').read()) #simepar
exec(open('src/read_nc.py').read()) #jaxa
exec(open('src/read_nc_noaa.py').read()) #cpc


# gerando dataframes horárias, diárias e mensais com todas as fontes de dados inclusas
exec(open('src/readData.py').read())


###### Gráficos ######
exec(open('src/[Scatterplot] Dispersão.py').read())
exec(open('src/[Boxplot] Chuva.py').read())
exec(open('src/[Lineplot] Chuva.py').read())

###### Índices ######
exec(open('src/calc.py').read())
exec(open('src/[Geo] Indices.py').read())

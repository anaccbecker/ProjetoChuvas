#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 13:26:32 2023

@author: ana.becker
"""
#Simepar x NRT

def FBS_ (psat, psim):
    FBS = (psat-psim)**2
    return(FBS)

def FSS_ (psat, psim, FBS):
    try:
        FSS = 1 - (FBS/(psim + psim))
    except:
        FSS = None
    return(FSS)


df = pd.read_csv('csv/[H] s j.csv').pivot(index=['time','codigo'],columns='variable',values='value')
df.reset_index(inplace=True)
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
df['FBS'] = None

df['FBS'] = df.apply(lambda x: FBS_(x['gsmap_nrt'], x['Simepar']), axis=1)
FBS = df.groupby('codigo').agg({'FBS':np.mean}).reset_index()
df = pd.merge(df, FBS, on = 'codigo', suffixes=('_x', '')).drop(columns=['FBS_x'])
df['Simepar**2'] = df['Simepar'].pow(2)
df['gsmap_nrt**2'] = df['gsmap_nrt'].pow(2)
psim_mse = df.groupby('codigo').agg({'Simepar**2':np.mean}).reset_index()
psat_mse = df.groupby('codigo').agg({'gsmap_nrt**2':np.mean}).reset_index()
df = pd.merge(df, psim_mse, on = 'codigo', suffixes=('_x', '')).drop(columns=['Simepar**2_x'])
df = pd.merge(df, psat_mse, on = 'codigo', suffixes=('_x', '')).drop(columns=['gsmap_nrt**2_x'])
df['FSS'] = df.apply(lambda x: FSS_(x['gsmap_nrt**2'], x['Simepar**2'], x['FBS']), axis=1)
df

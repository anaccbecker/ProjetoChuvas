#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:44:27 2023

@author: ana.becker
"""
psat_todos = pd.read_csv("csv/[TimeSpace]gsmap-nrt.csv")
psat_todos = psat_todos[['time','codigo','chuva_time']].rename({ 'chuva_time': 'chuva'}, axis='columns')
psat_todos['fonte']= 'JAXA'

psim = psim.reset_index()[['hordatahora','codigo','precipitacao(mm)']].rename({'hordatahora': 'time', 'precipitacao(mm)': 'chuva'}, axis='columns')
psim['fonte']= 'Simepar'



# parei aqui - estava dando erro correção das duplicatas
df = pd.concat([psat_todos, psim]).pivot(index=['time','codigo'],columns='fonte',values='chuva')
df.reset_index(inplace=True)
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
df['caso']=None


def classifica(prate, psim):
    if (prate == 0 and psim ==0):
        return 'h'
    if (prate != 0 and psim !=0):
        return 'cn'
    if (prate != 0 and psim ==0):
        return 'fa'
    if (prate == 0 and psim !=0):
        return 'm'
    
def ACC(h,cn,fa,m):
    total = h+cn+fa+m
    return (h+cn)/total

def POD(h,cn,fa,m):
    return h/(h+m)

def FAR(h,cn,fa,m):
    return fa/(fa+h)

def HSS(h,cn,fa,m):
    total = h+cn+fa+m
    hr = (((h+m)*(h+fa))+((cn+m)*(cn+fa)))/total
    return (h+cn-hr)/(total-hr)

def BIAS(h,cn,fa,m):
    return (h+fa)/(h+m)
    
def calcula_indices (produto):
    df['caso']= df.apply(lambda x: classifica(x[produto], x['Simepar']), axis=1)
    contagem = pd.DataFrame(df.groupby(['codigo','caso']).size())
    contagem.reset_index(inplace=True)
    contagem = contagem.pivot_table(values = 0, index = 'codigo', columns = 'caso')
    contagem['ACC'] = contagem.apply(lambda x: ACC(x['h'], x['cn'], x['fa'], x['m']), axis=1)
    contagem['POD'] = contagem.apply(lambda x: POD(x['h'], x['cn'], x['fa'], x['m']), axis=1)
    contagem['FAR'] = contagem.apply(lambda x: FAR(x['h'], x['cn'], x['fa'], x['m']), axis=1)
    contagem['HSS'] = contagem.apply(lambda x: HSS(x['h'], x['cn'], x['fa'], x['m']), axis=1)
    contagem['BIAS'] = contagem.apply(lambda x: BIAS(x['h'], x['cn'], x['fa'], x['m']), axis=1)
    contagem.to_csv(f'csv/indices_{produto}.csv')
    

calcula_indices('gsmap_now')
calcula_indices('gsmap_nrt')


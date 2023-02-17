#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:44:32 2023

@author: ana.becker
"""
def geoDist (x, y):
    rad = math.pi / 180
    a1 = x[0] * rad
    a2 = x[1] * rad
    b1 = y[0] * rad
    b2 = y[1] * rad
    dlon = b2 - a2
    dlat = b1 - a1
    a = (math.sin(dlat / 2))**2 + math.cos(a1) * math.cos(b1) * (math.sin(dlon / 2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6378.145
    d = R * c
    return(d)

############ Estações do simepar ############
sim = pd.read_csv('data/estacoes.csv')[['codigo','latitude','longitude']]
sim.reset_index(drop=True, inplace=True)

## apenas leitura dos ncs


def read_nc (path):
    nc_files = glob.glob(os.path.join(path,"*.nc"))
    df_est = pd.DataFrame()
    psat = pd.DataFrame()
    for f in nc_files:
        df_mes = xr.open_dataset(f).prate.to_dataframe()
    psat = pd.concat([psat,df_mes])
    return(psat)
    
    
now = read_nc('data/dados-processados/gsmap-now').reset_index()
nrt = read_nc('data/dados-processados/gsmap-nrt').reset_index()


import warnings
warnings.filterwarnings("ignore")


p1=0.5
p2=0.2
p3=0.05

psat = pd.DataFrame()    
for k in range(0,len(sim)): # para cada estacao do simepar
    print('estacao '+ str(sim.codigo[k]) )
    
    xr_nc = nrt
    dist = xr_nc[['lat','lon']].drop_duplicates(subset=['lat','lon'])
    dist['d']= dist.apply(lambda x: geoDist([x['lat'], x['lon']],[sim.latitude[k], sim.longitude[k]]), axis=1)
    selecao = dist[dist['d']<=20]
    selecao['pond'] = selecao.apply(lambda x: x['d']/selecao['d'].sum(), axis=1)
    
    chuvas = pd.merge(xr_nc,selecao)
    chuvas['chuva'] = chuvas.apply(lambda x: x['prate']*x['pond'], axis=1)
    chuvas_space = chuvas.groupby(['lat','lon','time']).agg({'chuva':np.mean}).reset_index()
    chuvas_space['chuva2']=None
    latlongs = chuvas_space.drop_duplicates(subset=['lat','lon'])[['lat','lon']].reset_index(drop=True)
    
    chuvas_time = pd.DataFrame()
    
    for j in range(len(latlongs)): #para cada grupo de estacoes proximas
        chuva_est = chuvas_space[(chuvas_space.lat==latlongs.lat[j]) & (chuvas_space.lon==latlongs.lon[j])].reset_index(drop=True)
        for i in range(len(chuva_est)):
            try: 
                a = chuva_est.chuva[i-2]
            except:
                a = None
            try:
                b = chuva_est.chuva[i-1]
            except:
                b = None
            try:
                c = chuva_est.chuva[i]
            except:
                c = None
            try:
                d = chuva_est.chuva[i+1]
            except:
                d = None
            try:
                e = chuva_est.chuva[i+2]
            except:
                e = None
            try:
                chuva_est.chuva2[i] = a*p3+b*p2+c*p1+d*p2+e*p3
            except:
                chuva_est.chuva2[i] = None
        chuvas_time = pd.concat([chuvas_time, chuva_est])
    psat = pd.concat([psat,chuvas_time])


psat.to_csv("csv/[TimeSpace]gsmap-nrt.csv")
    





    







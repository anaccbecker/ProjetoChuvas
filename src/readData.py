#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:59:24 2023

@author: ana.becker
"""
###### Dados horários ######
#%%
# dados simepar
path = os.getcwd()+'/data/Chuvas-simepar'
csv_files = glob.glob(os.path.join(path, "*.csv"))
psim = pd.DataFrame()
for f in csv_files:
    df_est = pd.read_csv(f)
    df_est['codigo'] = f.split("/")[-1].split("_")[0]
    psim = pd.concat([psim,df_est])    
psim['codigo'] = psim['codigo'].astype(int)
inv_est = pd.read_csv('data/estacoes.csv')[['codigo', 'nome', 'latitude', 'longitude']]
psim = psim.set_index('codigo').join(inv_est.set_index('codigo'), on='codigo', how='left')
psim.rename(columns = {'datahora': "time",
                        'chuva_mm': 'psim'}, inplace = True) 
psim['time'] = psim['time'].apply(lambda x:x.split("+")[0])
psim['min'] = psim['time'].apply(lambda x:x.split(":")[1])
psim['time'] = pd.to_datetime(psim['time'], format='%Y-%m-%d %H:%M:%S')
psim = psim[psim['min']!='30']  # devido a agregacao cumulativa foram deletados os dados de fracao de hora
psim.drop(columns=['min'], inplace=True)
psim.reset_index(inplace=True)
psim.to_csv('csv/sim_H.csv')


# dados JAXA
sim = pd.read_csv('data/estacoes.csv')[['codigo', 'nome', 'latitude', 'longitude']]
sim.sort_values(by='longitude', inplace=True)
sim.reset_index(drop=True, inplace=True)
pjaxa = pd.read_csv('csv/35e.csv')
pjaxa = pjaxa.groupby(['codigo','time']).agg({'prate' : np.mean})
pjaxa.reset_index(inplace=True)
pjaxa['time'] = pd.to_datetime(pjaxa['time'], format='%Y-%m-%d %H:%M:%S')
pjaxa.drop(pjaxa[pjaxa['prate'] < 0].index, inplace = True)
pjaxa = pjaxa.sort_values(by='time')
pjaxa_H = pjaxa.set_index(['time']).groupby(['codigo']).resample("H", closed='right', label='right').agg({'prate' : np.sum}) 
pjaxa_H.reset_index(inplace=True)
pjaxa_H.to_csv('csv/jaxa_H.csv')


# uniao dos dados no mesmo dataframe
df_H = pd.merge(pjaxa, psim, on = ['time','codigo']).melt(value_vars = ['prate','psim'], id_vars = ['time', 'codigo'])
df_H.replace('prate', "JAXA", inplace = True)  
df_H.replace('psim', "Simepar", inplace = True)  
df_H.to_csv('csv/[H] s j.csv', index=False)


###### Dados diários ######
#%%

df_D = df_H.set_index('time').groupby(['codigo','variable']).resample("D", closed='right', label='right').agg({'value' : np.sum}) 
df_D.reset_index(inplace=True)
df_D = pd.concat([df_D, pnoaa])

df_D.to_csv('csv/[D] s j c.csv', index=False)


###### Dados mensais ######
#%%
df_M = df_D.set_index(['time']).groupby(['codigo','variable']).resample("M", closed='right', label='right').agg({'value' : np.sum})
df_M.reset_index(inplace=True)
df_M.to_csv('csv/[M] s j c.csv', index=False)



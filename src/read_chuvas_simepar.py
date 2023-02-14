# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# lendo dados das estacoes
#%%
path = os.getcwd()+'/data/Chuvas-simepar'
csv_files = glob.glob(os.path.join(path, "*.csv"))
psim = pd.DataFrame()
for f in csv_files:
    df_est = pd.read_csv(f)
    df_est['codigo'] = f.split("/")[-1].split("_")[0]
    psim = pd.concat([psim,df_est])    
psim['codigo'] = psim['codigo'].astype(int)


# lendo e inserindo as coordenadas do inventário das estacoes
#%%
inv_est = pd.read_csv('data/estacoes.csv')[['codigo','latitude','longitude']]
# para o join funcionar, a coluna de interesse deve ser setada como index
psim = psim.set_index('codigo').join(inv_est.set_index('codigo'), on='codigo', how='left')







# (old) lendo arquivo das 13 estacoes
#%%

# psim = pd.read_csv('data/Chuvas_Simepar/13estacoes_horario_20170601_20230131.csv')
# psim =  psim.melt(value_vars = ['23185109', '23275159', '23445317', '24134940',
#        '24385115', '24535333', '25135001', '25215130', '25264916', '25324831',
#        '25435458', '26075241', '26285158' ], id_vars = ['Unnamed: 0'])

# psim.rename(columns = {'Unnamed: 0': "time"}, inplace = True) 
# psim['time'] = psim['time'].apply(lambda x:x.split("+")[0])
# psim['time'] = pd.to_datetime(psim['time'], format='%Y-%m-%d %H:%M:%S')
# psim.rename(columns = {'variable': "codigo",
#                        'value': 'psim'}, inplace = True) 
# psim['codigo'] = pd.to_numeric(psim['codigo'])


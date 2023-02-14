#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:31:31 2023

@author: ana.becker
"""

# ###### Dividindo o resultado por mes ######
# df['mes'] = df.time.apply(lambda x: f'{x.year}-{x.month:02d}')

# contagem = pd.DataFrame(df.groupby(['codigo','caso','mes']).size())
# contagem.reset_index(inplace=True)
# contagem = contagem.pivot_table(values = 0, index = ['codigo','mes'], columns = ['caso'])

# contagem['ACC'] = contagem.apply(lambda x: ACC(x['h'], x['cn'], x['fa'], x['m']), axis=1)
# contagem['POD'] = contagem.apply(lambda x: POD(x['h'], x['cn'], x['fa'], x['m']), axis=1)
# contagem['FAR'] = contagem.apply(lambda x: FAR(x['h'], x['cn'], x['fa'], x['m']), axis=1)
# contagem['HSS'] = contagem.apply(lambda x: HSS(x['h'], x['cn'], x['fa'], x['m']), axis=1)
# contagem['BIAS'] = contagem.apply(lambda x: BIAS(x['h'], x['cn'], x['fa'], x['m']), axis=1)

# contagem.reset_index().to_csv('csv/indices_por mes.csv')

# sim = pd.read_csv('data/estacoes.csv')
# contagem_por_mes = pd.merge(sim, contagem.reset_index())

# ###### Loop dos gráficos ######
# colors = [(1.0, 0, 0), (1.0, 1.0, 0), (0, 1.0, 0)]
# cmap = matplotlib.colors.LinearSegmentedColormap.from_list('mycmap', colors)

# for column in ['ACC', 'POD', 'BIAS', 'HSS']:
#     heat = contagem_por_mes.reset_index()[['nome','mes',column]].pivot('nome','mes',column)
#     fig, ax = plt.subplots()
#     sns.heatmap(heat, annot=False, cmap=cmap, ax=ax)
#     ax.set_title(f'{column}')
#     fig.savefig(f'img/[Heatmap] Índices por mês/{column}.png', bbox_inches='tight')
    
# ###### FAR ###### (escala inversa)
# colors = [(0, 1.0, 0), (1.0, 1.0, 0), (1.0, 0, 0)]
# cmap = matplotlib.colors.LinearSegmentedColormap.from_list('mycmap', colors)

# heat = contagem_por_mes.reset_index()[['nome','mes','FAR']].pivot('nome','mes','FAR')
# fig, ax = plt.subplots()
# sns.heatmap(heat, annot=False, cmap=cmap, ax=ax)
# ax.set_title('FAR')
# fig.savefig('img/[Heatmap] Índices por mês/FAR.png', bbox_inches='tight')
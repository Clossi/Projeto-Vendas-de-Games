# -*- coding: utf-8 -*-
"""Projeto venda de jogos no mundo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xMJ5DSso-6620IJmyMup9s6Dhdhdjc5u
"""

# Libs para modelagem e matriz
import numpy as np
import pandas as pd


# Libs para tratamento e analise grafica
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Libs para retirar os avisos
import warnings

# Comando para retirar os avisos
warnings.filterwarnings('ignore')

Base_Dados = pd.read_csv('PS4_GamesSales.csv', encoding='latin-')

Base_Dados.head()

Base_Dados.shape

Base_Dados.isnull().sum()

plt.figure( figsize=(16, 6) )
plt.title('Analise de campos nulos')

sns.heatmap( Base_Dados.isnull(), cbar=False );

Base_Dados.dropna( inplace=True )

Base_Dados.describe()

# Titulo
plt.title('Quantidade de vendas globais (mi)', loc='left', fontsize=14 )

# Grafico
sns.barplot( data=Base_Dados, x='Year', y='Global', ci=None, color='#69b3a2', estimator=sum )

# Label
plt.ylabel('Quantidade de vendas (mi)');

# Remover anos vazios 2019 e 2020

Base_Dados = Base_Dados.loc[ (Base_Dados['Year'] !=2019 ) & (Base_Dados['Year'] !=2020 ) ]

Base_Dados.head()

plt.figure( figsize=(12, 5) )

plt.style.use('ggplot')


sns.kdeplot( Base_Dados['Global'], shade=True, bw=1, color='#96a9a9', linewidth=2.5 )

plt.title('Distribuição das vendas Globais', loc='left', fontsize=14);

Base_Dados.groupby( by=['Year'] ).sum()

plt.figure( figsize=(10, 5) )

plt.title('Analise da distribuição global (mi)', loc='left' )
sns.boxplot( data=Base_Dados, x='Year', y='Global');

Base_Dados.loc[ Base_Dados['Global'] >= 10 ]

Base_Dados

Analise = Base_Dados.groupby( by=['Year'] ).sum().reset_index()

America = [ America / Total * 100 for America, Total in zip( Analise['North America'], Analise['Global'] ) ]
Europa = [ Europa / Total * 100 for Europa, Total in zip( Analise['Europe'], Analise['Global'] ) ]
Japão = [ Japão / Total * 100 for Japão, Total in zip( Analise['Japan'], Analise['Global'] ) ]
Mundo = [ Mundo / Total * 100 for Mundo, Total in zip( Analise['Rest of World'], Analise['Global'] ) ]

America, Europa, Japão, Mundo

Analise

plt.boxplot(Analise);

plt.figure( figsize=(10, 5) )

Largura_Barra = 0.85
Rotulos = Analise['Year']
Grupos = [0, 1, 2, 3, 4, 5]

plt.bar( Grupos, America, width=Largura_Barra, color= '#b5ffb9', edgecolor='white' )

plt.bar( Grupos, Europa, bottom=America, width=Largura_Barra, color= '#f9bc86', edgecolor='white' )

plt.bar( Grupos, Japão, bottom=[ A + B for A, B in zip(America, Europa) ], width=Largura_Barra, color= '#a3acff', edgecolor='white' )

plt.bar( Grupos, Mundo, bottom=[ A + B + C for A, B, C in zip(America, Europa, Japão) ], width=Largura_Barra, color= '#d3acfe', edgecolor='white' )

plt.title('Analise de Distribuição por Continentes')

plt.xticks( Grupos, Rotulos )
plt.xlabel('Grupo')
plt.ylabel('Distribuição %')

plt.legend(['America N', 'Europa', 'Japão', 'Mundo'], loc='upper left', bbox_to_anchor=(0.15, -1), ncol=4);

Base_Dados['Publisher'].unique()

from sklearn.preprocessing import LabelEncoder

Função_Label = LabelEncoder()

Base_Dados['Produtor'] = Função_Label.fit_transform( Base_Dados['Publisher'] )
Base_Dados['Genero'] = Função_Label.fit_transform( Base_Dados['Genre'] )
Base_Dados['Jogo'] = Função_Label.fit_transform( Base_Dados['Game'] )


Base_Dados.head()

Paleta_Cores = sns.color_palette('husl', 8)

Paleta_Cores

plt.figure( figsize=(20, 4))
plt.title('Analise dos Produtores de Games (mi)')

sns.scatterplot( data=Base_Dados, x='Produtor', y='Global', color=Paleta_Cores[0] );

plt.figure( figsize=(20, 4))
plt.title('Analise do Genero que mais vendeu (mi)')

sns.scatterplot( data=Base_Dados, x='Genero', y='Global', color=Paleta_Cores[0] );

plt.figure( figsize=(20, 4))
plt.title('Analise do Jogo que mais vendeu (mi)')

sns.scatterplot( data=Base_Dados, x='Jogo', y='Global', color=Paleta_Cores[3] );

fig, ax = plt.subplots( figsize=(22, 15) )

Cor_Fundo = '#f5f5f5'
ax.set_facecolor( Cor_Fundo )
fig.set_facecolor( Cor_Fundo )

plt.style.use('seaborn')

plt.suptitle('Python para analise de dados \n projeto pratico 5 - Analise de mercado games PS4', fontsize=22, color='#404040', fontweight=600)
Linhas = 3
Colunas = 2


plt.subplot( Linhas, Colunas, 1 )

# Titulo
plt.title('Quantidade de vendas globais (mi)', loc='left', fontsize=14 )

# Grafico

plt.bar( Base_Dados['Year'], Base_Dados['Global'], color='#69b3a2' )

# Label
plt.ylabel('Quantidade de vendas (mi)')

plt.subplot( Linhas, Colunas, 2 )

plt.title('Analise da distribuição global (mi)', loc='left' )
sns.boxplot( data=Base_Dados, x='Year', y='Global')



plt.subplot( Linhas, Colunas, 3 )

Largura_Barra = 0.85
Rotulos = Analise['Year']
Grupos = [0, 1, 2, 3, 4, 5]
plt.bar( Grupos, America, width=Largura_Barra, color= '#b5ffb9', edgecolor='white' )
plt.bar( Grupos, Europa, bottom=America, width=Largura_Barra, color= '#f9bc86', edgecolor='white' )
plt.bar( Grupos, Japão, bottom=[ A + B for A, B in zip(America, Europa) ], width=Largura_Barra, color= '#a3acff', edgecolor='white' )
plt.bar( Grupos, Mundo, bottom=[ A + B + C for A, B, C in zip(America, Europa, Japão) ], width=Largura_Barra, color= '#d3acfe', edgecolor='white' )
plt.title('Analise de Distribuição por Continentes', loc='left', fontsize=14)
plt.xticks( Grupos, Rotulos )
plt.xlabel('Grupo')
plt.ylabel('Distribuição %')
plt.legend(['America N', 'Europa', 'Japão', 'Mundo'], loc='upper left', bbox_to_anchor=(0.15, -1), ncol=4);


plt.subplot( Linhas, Colunas, 4 )
plt.title('Analise dos Produtores de Games (mi)', loc='left', fontsize=14)
sns.scatterplot( data=Base_Dados, x='Produtor', y='Global', color=Paleta_Cores[0] )


plt.subplot( Linhas, Colunas, 5 )
plt.title('Analise do Jogo que mais vendeu (mi)', loc='left', fontsize=14)
sns.scatterplot( data=Base_Dados, x='Jogo', y='Global', color=Paleta_Cores[3] )


plt.subplot( Linhas, Colunas, 6 )
plt.title('Analise do Genero que mais vendeu (mi)', loc='left', fontsize=14)
sns.scatterplot( data=Base_Dados, x='Genero', y='Global', color=Paleta_Cores[0] )

plt.subplots_adjust( hspace=0.35, wspace=0.15)

Rodape = '''
Este relatorio foi criado em treinamento, "Python para analise de dados"
by: Divino Clossi
'''

fig.text( 0.5, -0.03, Rodape, ha='center', va='bottom', size=12, color='#938ca1' );








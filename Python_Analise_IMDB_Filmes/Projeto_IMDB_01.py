# 18/09/2022
# Projeto Python para Análise de Filmes - Dataset do IMDB

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python usada Neste Jupyter notebook : ', python_version() )

https://pypi.org
https://pypi.org/project/imdb-sqlite/

# Instalação do Pacote que contem a base do IMDB em SQLite
# -q para não exibir o log de instalação em tela (Instalação Silenciosa)
!pip install -q imdb-sqlite

# Agora executamos o pacote para download dos datasets
# Instala o pacote
# https://pypi.org/project/pycountry/
!pip install -q pycountry

# Importando as Bibliotecas a Serem Utilizadas
import re
import time
import sqlite3
import pycountry
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

# Carregando os Dados
# Primeiro temos que baixar os dados!

# Comando para ver o quanto tempo uma celula ficou executando
# E comando de sistema operacional para baixar e instalar o dados IMDB
%%time
!imdb-sqlite

# Conecta no banco de dados
conn = sqlite3.connect('imdb.db')

# Extrai a lista de tabelas
tabelas = pd.read_sql_query("SELECT NAME AS 'Table_Name' FROM sqlite_master WHERE type = 'table' ", conn)

# Tipo do Objeto
type(tabelas)

# Visualização do Resultado - Lista apenas alguns registros
tabelas.head()

# Converte o DataFrame em uma Lista
tabelas = tabelas["Table_Name"].values.tolist()

# Percorre a lista de tabelas no banco de dados e extrai o esquema de cada um
for tabela in tabelas:
    consulta = "PRAGMA TABLE_INFO({})".format(tabela)
    resultado = pd.read_sql_query(consulta, conn)
    print("Esquema da tabela : ", tabela)
    display(resultado)
    print("-" * 100)
    print("\n")

# Quais São as Categorias de Filmes Mais Comuns no IMDB
# Quais são os principais tipos (categorias) dos títulos (filmes)

# Criando uma Consulta SQL
consulta1 = '''SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type'''

# Extraindo o Resultado
resultado1 = pd.read_sql_query(consulta1, conn)

# Visualizando o Resultado
display(resultado1)

# Criando uma coluna e Calculando o Percentual para cada Tipo
resultado1[percentual] = (resultado1['COUNT'] / resultado1['COUNT'].SUM()) * 100

# Visualizando o Resultado
display(resultado1)

# Criando um grafico com apenas 4 categorias
# As 3 categorias com mais titulos e 1 categoria com todo o restante
# Cria um dicionário vazio
others = {}

# Filtra o percentual em 5% e soma o total
others['COUNT'] = resultado1[resultado1['percentual'] < 5]['COUNT'].sum()

# Grava o percentual
others['percentual'] = resultado1[resultado1['percentual'] < 5]['percentual'].sum()

# Ajusta o nome
others['type'] = 'others'

# Visualiza
others

# Filtra o dataframe de resultado
resultado1 = resultado1[resultado1['percentual'] > 5]

# Append com o dataframe de outras categorias
resultado1 = resultado1.append(others, ignore_index = True)

# Ordena o resultado
resultado1 = resultado1.sort_values(by = 'COUNT', ascending = False)

# Visualiza alguns registros
resultado1.head()

# Ajusta os Labels
labels = [str(resultado1['type'][i]) + ' ' + '[' + str(round(resultado1['percentual'][i],2)) + '%' + ']' for i in resultado1.inc

# Plot
# Mapa de Cores
# https://matplotlib.org/stable/tutoriais/colors/colormaps.html
cs = cm.Set3(np.arange(100) )

# Cria a Figura
f = plt.figure()
          
# Pie Plot
plt.pie(resultado1['COUNT'], labeldistance = 1, radius = 3, colors = cs, wedgeprops = dict(width = 0.8) )
plt.legend(labels = labels, loc = 'center', prop = {'size':12})
plt.title("Distribuição de Titulos", loc = 'Center', fontdict = {'fontsize':20, 'fontweight':20})
plt.show()

# Qual o Número de Títulos Por Gênero

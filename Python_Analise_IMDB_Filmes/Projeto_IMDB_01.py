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

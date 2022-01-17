-- Script documentação Python + Power BI para Analise de Dados

# Carregando e Instalando Pacotes

# Versão da Linguagem Python
from platform import python_version
print("Versão da Linguagem Python Usada Neste Jupyter Notebook:", python_version() )

# Executar no terminal ou prompt de comando
# Esse pacote é usado para gravar as versões de outros pacotes usados neste jupyter notebook
!pip install -q -U watermark

# Imports
import numby  as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Consultando Versões de pacotes usados neste Jupyter Notebook
%reload_ext watermark
%watermark -a "Data Science Academy" -- iversions

# Carregando os Dados
dadosRH = pd.read_csv('dadosRH.csv') # Ler
dadosRH.head() # Visualizar amostra - primeiras linhas
dadosRH.shape # Visualiza Total de Linhas e Colunas da Tabela

# Analise Exploratória, Limpeza e Transformação do Dados

dadosRH.isnull().sum() # Total de registros NULL para cada Coluna
dadosRH.groupby(['educacao']).count() # Realiza um Agrupamento pela coluna educacao e exibe o total de registros - não considera valores ausentes
sns.countplot(dadosRH[educacao]) # Cria um Grafico de Barras com a coluna educacao
dadosRH.groupby(['aval_ano_anterior']).count()
sns.countplot(dadosRH[aval_ano_anterior])
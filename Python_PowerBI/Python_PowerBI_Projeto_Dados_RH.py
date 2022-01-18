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

dadosRH['educacao'].fillna(dadosRH['educacao'].mode()[0], inplace = True) # Preenche valores ausentes com o valor do calculo da moda
dadosRH['aval_ano_anterior'].fillna(dadosRH['aval_ano_anterior'].median(), inplace = True) # Preenche valores ausentes com o valor do calculo da mediana
dadosRH.isnull().sum()
dadosRH.groupby(['educacao']).count()
dadosRH.groupby([aval_ano_anterior]).count()

dadosRH.groupby(['promovido']).count()
sns.countplot(dadosRH['promovido'])
df_classe_majoritaria = dadosRH[dadosRH.promovido == 0]
df_classe_minoritaria = dadosRH[dadosRH.promovido == 1]
df_classe_majoritaria.shape
df_classe_minoritaria.shape

# Técnica - Upsample
# Upsample da classe minoritaria - Exemplo de balanceamento entre valores - conjunto de dados
# Cria amostragem dos dados
from sklearn.utils import resample
df_classe_minoritaria_upsampled = resample(df_classe_minoritaria,
                                           replace = True,
                                           n_samples = 50140,
                                           random_state = 150)
                                           

dadosRH_balanceados = pd.concat([df_classe_majoritaria, df_classe_minoritaria_upsampled]) # Concatenando os valores das classes / variaveis
dadosRH_balanceados.promovido.value_counts() # Contando o total de registros da coluna promovido
dadosRH_balanceados.info() # Informações de totas variáveis do conjunto de dados
sns.countplot(dadosRH_balanceados['promovido']) # Criando Grafico novamente

# Salvando os dados balanceados em disco
dadosRH_balanceados.to_csv('dadosRH_modificado.csv', encoding = 'utf-8', index = False)

dataset = pd.read_csv(''dadosRH_modificado.csv')
dataset.head()
dataset.shape
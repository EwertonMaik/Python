-- Script documentação Python + Power BI para Analise de Dados

Biblioteca Python para Analise de Dados (Py Data Stack)

Matplotlib
https://matplotlib.org/

Seaborn
https://seaborn.pydata.org/

Pandas
https://pandas.pydata.org/

NumPy - Operações matemática de dados
https://numpy.org/

Comunidade DSA
https://www.datascienceacademy.com.br/social

Anaconda Python
https://www.anaconda.com

Instalação do Interpretador Python
anaconda.com (Possui o Interpretador + biblioteca dos pacotes Python)

# Atividade 1 - Violin Plot

# Carregando DataSet
import pandas as pd
dataset = pd.read_csv('Usuarios.csv')

# Criando Grafico
import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(x = 'salario', data = dataset)
plt.show() # Exibe a visualização do Grafico

# Matriz de correlação para variáveis numericas
# Matriz de associação para variáveis categoricas
# Correlação não implica causalidade

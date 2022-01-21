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

# Pergunta 1 - Qual a correlação entre os atributos dos funcionarios
import matplotlib.pyplot as pl
import seaborn as sns
corr = dataset.corr()
sns.headmap(corr, cmap = "Y10rRd", linewidths = 0.1)
plt.show()

# Pergunta 2 - Qual o tempo de serviço da maioria dos funcionarios
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(dataset['tempo_servico'], color = 'green')
plt.title('Distribuição do Tempo de Serviço dos Funcionários', fontsize = 15)
plt.xlabel('Tempo de Serviço em Anos', fontsize = 15)
plt.ylabel('Total')
plt.show()

# Pergunta 3 - Qual avaliação do ano anterior foi mais comum
import matplotlib.pyplot as plt
import seaborn as sns
dataset['aval_ano_anterior'].value_counts().sort_values().plot.bar(color = 'blue', figsize = (10, 5) )
plt.title('Distribuição da Avaliação do Ano anterior dos Funcionários', fontsize = 15)
plt.xlabel('Avaliações', fontsize = 15)
plt.ylabel('Total')
plt.show()

# Pergunta 4 - Qual a distribuição das idades dos funcionarios
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(dataset['idade'], color = 'magenta')
plt.title('Distribuição da Idade dos Funcionários', fontsize = 15)
plt.xlabel('Idade', fontsize = 15)
plt.ylabel('Total')
plt.show()

Pergunta 5 - Qual o Número de Treinamentos mais frequente
import matplotlib.pyplot as plt
import seaborn as sns
sns.violinplot(dataset['numero_treinamentos'], color = 'red')
plt.title('Número de Treinamentos Feitos Pelos Funcionarios', fontsize = 15)
plt.xlabel('Número de Treinamentos', fontsize = 15)
plt.ylabel('Frequencia')
plt.show()

-- Pergunta 6 - Qual a Proporção dos Funcionários Por Canal de Recrutamento
import matplotlib.pyplot as plt
import seaborn as sns
dataset['canal_recrutamento'].value_counts()
fatias  = [55375, 42358, 2547]
labels  = "Outro","Outsourcing","Indicação"
colors  = ['purple', 'lime', 'yellow']
explode = [0, 0, 0]
plt.pie(fatias, labels = labels, colors = colors, explode = explode, shadow = True, autopct = "%.2f%%")
plt.title('Percentual de Funcionarios Por Canal de Recrutamento', fontsize = 15)
plt.axis('off')
plt.legend()
plt.show()

-- Pergunta 7 - Qual a Relação Entre a Promoção e a Avaliação do Ano Anterior
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.crosstab(dataset['aval_ano_anterior'], dataset['promovido'] )
data.div(data.sum(1).astype(float), axis = 0 ).plot(kind    = 'bar',
                                                    stacked = True,
                                                    figsize = (16, 9),
                                                    color   = ['blue', 'magenta']
                                                    )
plt.title('Relação Entre Avaliação do Ano Anterior e a Promoção', fontsize = 15)
plt.xlabel('Avaliação do Ano Anterior', fontsize = 15)
plt.legend()
plt.show()
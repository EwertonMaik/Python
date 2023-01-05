-- Documentação Sobre Pacote PANDAS


## PANDAS - Criando Séries
from pandas import Series
import pandas as pd
pd.__version__

# Crimando uma série sem especificar os índices
Obj = Series([67, 78, -56, 13])

Obj

type(Obj)

Obj.values

Obj.index

# Criando uma série e especificando os índices
Obj2 = Series([67, 78, -56, 13], index = ['a','b','c','d'])
Obj2
Obj2.values
Obj2.index
Obj2[Obj2 > 3]
Obj2['b']
'd' in Obj2

# Criando uma série de dados passando um dicionário como parâmaetro
dict = {'Futebol':5200, 'Tenis':120, 'Natação':698, 'Volleyball':1550}

# Criando uma série a partir de um dicionário
Obj3 = Series(dict)

Obj3
type(Obj3)

## PANDAS - Manipulando Séries

# criando uma lista
esportes = ['Futebol','Tenis','Natação','Basketball']

# Criando uma serie e usando uma lista como índice
Obj4 = Series(dict, index = esportes)

Obj4

pd.isnull(Obj4)
pd.notnull(Obj4)

Obj4.isnull()

# Concatenando Series
Obj3 + Obj4

Obj4.name = 'população'
Obj4.index.name = 'esporte'
Obj4


## DataFrames
from pandas import DataFrame

data = {'Estado': ['Santa Catarina','Paraná','Goiás','Bahia','Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]
        }

frame = DataFrame(data)
frame
type(frame)
DataFrame(data, columns = ['Ano', 'Estado', 'População'])

# criando outro dataframe com os mesmos dados anteriores mas adicionando uma coluna
frame2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'],
                         index = ['um','dois','três','quatro','cinco'] )

# Imprimindo o Datafr,ame
frame2

# Imprimindo apenas uma coluna do DataFrame
frame2['Estado']
type(frame2)
frame2.index
frame2.columns
frame2.values
frame2.dtypes
frame2['Ano']
frame2.Ano
frame2[:2]

## Usando Numpy e Pandas
import numpy as np

## Usando o Numpy para alimentar uma das colunas do dataframe
frame2['Débito'] = np.arange(5.)
frame2
frame2.values
frame2.describe()
frame2['dois':'quatro']
frame2 < 5

## Localizando Registros Dentro do DataFrame
frame2.loc['quatro']
frame2.iloc[2]

## Invertendo as Colunas e Índices
## Criando um Dicionario
web_stats = {'Dias' : [1,2,3,4,5,6,7]
             'Visitantes' : [45,23,67,78,23,12,14],
             'Taxas' : [11,22,33,44,55,66,77]
                }

df = pd.DataFrame(web_stats)
print(df)

## Visualizando uma coluna como index
print(df.set_index('Dias') )
print(df.head() )
print(df['Visitantes'] )
print(df[['Visitantes'], ['Taxas'] ] )


## DataFrames e Arquivos CSV
## Usando o método read_csv

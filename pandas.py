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

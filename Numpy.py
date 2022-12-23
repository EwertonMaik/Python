## Conhecendo o Pacote Numpy e suas Operações

## Instalando o pacote Numpy
pip install numpy -U

## Importando pacote Numpy
import numpy as np

## Consultando versão do pacote
np.__version__

## Função help para listar sintaxe da função
help(np.array)

## Criando Array a partir de uma lista
vetor01 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

## Imprimindo o vetor
print(vetor01)

## Usando função type para lista o tipo do Objeto
type(vetor01)

## Função que retorna a soma cumulativa dos elementos do vetor
vetor01.cumsum()

## Criando uma Lista de valores
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

## Imprimindo o tipo do Objeto
type(lista)

## Imprimindo o valor de uma posição 5 do Vetor
print(vetor01[5])

## Atribuindo um novo valor a posição 5 do vetor
vetor01[5] = 100
vetor01[5] = 'Novo Elemnto String' ## Obtêm erro devido array ser apenas de um tipo

## Função que retorna quantas dimensões e elementos o vetor possui
print(vetor01.shape)

## Numpy - Metódo e Operações com DataSets
## Usando o Método Random() do Numpy
print(np.random.rand(10) )

import matplotlib.pyplot as plt
%matplotlib inline

print(np.random(10) )

plt.show((plt.hist(np.random.rand(1000))))

print(np.random.randn(5,5))

plt.show(plt.hist(np.random.randn(1000)) )

imagem = np.random.rand(30, 30)
plt.imshow(imagem, cmap = plt.cm.hot)
plt.colorbar()

## Operações com datasets
import os
filename = os.path.join('iris.csv')

## No Windows use !more iris.csv. Mac ou Linux use !head iris.csc
!head iris.csv

# Carregando um dataset para dentro de um array
arquivo = np.loadtxt(filename, delimiter='', usecols=(0,1,2,3), skiprows=1)
print(arquivo)

type(arquivo)

# Gerando um plot a partir de um arquivo usando o Numpy
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0,1), skiprows=1, unpack=True)
plt.show(plt.plot(var1, var2, 'o', markersize = 8, alpha = 0.75))

## Estatística
# Criando um Array
A = np.array([15, 23, 63, 94, 75])


# Em estatística a média é o valor que aponta para onde mais se concentram os dados de uma distribuição
np.mean(A)

# O Desvio padrão mostra o quanto de variação ou dispersão existe em relação à média (ou valor esperado)
# Um baixo desvio padrão indica que os dados tendem a estar próximos da média.
# Um desvio padrão alto indica que os dados estão espalhados por uma gama de valores
np.std(A)

# Variãncia de uma variável aleatória é uma medida de sua dispersão estatística, indicando o  quão longe em geral os valores se
# Encontram do valor esperado
np.var(A)

d = np.arange(1, 10)
np.sum(d)

# Retorna o produto dos Elementos
np.prod(d)

# Soma acumulada dos elementos
np.cumsum(d)

a = np.random.randn(400,2)
m = a.mean(0)
print(m, m.shape)

plt.plot(a[:0], a[:,1], 'o', markersize = 5, alpha = 0.50)
plt.plot(m[0], m[1], 'ro', markersize = 10)
plt.show()

# Outras Operações com Arrays
# Slicing

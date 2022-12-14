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

# Modulos e Pacotes
Repositório de Pacotes do Python - Pypi - Python Package Index - htttps://pypi.python.org/pypi
import pacote.modulo

cond list -- Comando cmd para listar todos os pacotes que estão instalados na instalação de sua instância Python

-- Comando cmd para para realizar instalação de um pacote Python
conda install "nome_do_modulo"
pip install "nome_do_modulo"
pip install python-pptx -- Pacote que cria e manipular arquivos do Microsoft Power Point a partir do Python.
keras 2.1.5 - Pacote para trabalhar com Deep Learning For Humans


-- Verifico todos os métodos disponíveis do pacote MATH
dir(math)
print(dir(math) )

-- Apresenta informações de ajuda sobre a utilização do método
help(sqrt)

import math -- Importanto Biblioteca matemática - todas as funções do pacote
math.sqrt(25) -- Chamamndo o método sqrt para calcular a raiz quadrada de 25

from math import sqrt -- Importando apenas uma função especifica do pacote math
sqrt(9) -- Chamando apenas o método importado

import random -- Pacote para gerar números randômicos
random.choice(['Maça', 'Banana', 'Laranja']) -- Escolhe de maneira aleatória uma fruta
random.sample(range(100), 10) -- Gera um range de valores de 10 números na faixa de 0 até 100

import statistics -- Pacote com métodos de operações estatisticas
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(dados) -- Calcula a média dos valores
statistics.median(dados) -- Calcula a mediana dos valores

import os -- Pacote com métodos para sistema operacional
os.getcwd() -- Retorna o diretorio atual em que esta trabalhando

import sys -- Pacote para interagir com Sistema Operacional
sys.stdout.write('Teste')
sys.version

import urllib.request --Pacote para trabalhar com links web
resposta = urllib.request.urlopen('http://python.org') -- Variável armazena objeto da página web
print(resposta)
html = resposta.read() -- Lê o código html da página e salva na variável
print(html)

## Trabalhando com Datas
import datetime

var01 = datetime.datetime.now() -- Variável recebendo data e hora atual
print(var01)

var02 = datetime.time(8, 25, 55) -- Variável recebendo uma data configurada manualmente
print(var02)

-- Extraindo da variável var02 a hora, minutos, segundos e milisegundos individualmente
print ('Hora  :', var02.hour)
print ('Minute:', var02.minute)
print ('Segundo:', var02.second)
print ('Microsegundo:', var02.microsecond)

print(datetime.time.min)
-- Definindo uma variável para receber a data atual e logo extraindo Tempo, Ano, Mês e Dia
var03 = datetime.date.today()
print (var03)
print ('ctime:', var03.ctime())
print ('Ano:', var03.year)
print ('Mês :', var03.month)
print ('Dia :', var03.day)

-- Definindo uma data manualmente para uma variável
var04 = datetime.date(2015, 4, 28)
print ('var04 : ', var04)

-- Definindo uma data para variável var05, porém usando a função replace pegando a data da variável var04 e atualizando apenas o ano de 2015 para 2016
var05 = var04.replace( year = 2016)
print ('var05 : ', var05)

-- Realizando operação de subtração de datas
var05 - var04

## Pacote Map
# Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Celsius
def celsius(T):
    return (float(5)/9)*(T-32)
  
map(fahrenheit, temperaturas) -- 1º parâmetro é uma função criada anteriormente, que transforma os valores da lista do 2º parâmetro em temperatura Fahrenheit.
list(map(fahrenheit, temperaturas)) -- É utilizado a função list para converter a operação anterior comentada em uma lista

--Utilizando a mesma operação map anterior, porém em um for para imprimir os valores da lista
for temp in map(fahrenheit, temperaturas):
    print(temp)

map(celsius, temperaturas) -- Utilizando map para converter um lista de valores em temperatura Celsius
list(map(celsius, temperaturas)) -- Converte e imprime a lista de valores convertidos

-- Realizando a operação anterior, porém com uma expressão Lambda
map(lambda x: (5.0/9)*(x - 32), temperaturas) -- Realiza a conversão, no lugar da chamada função é escrito a expressão lambda
list(map(lambda x: (5.0/9)*(x - 32), temperaturas))  -- Da mesma forma, utilizando a expressão lambda no lugar da função, realizado a impressão

-- Realizando operações com lista através de expressões Lambda
a = [1,2,3,4]
b = [5,6,7,8]
list(map(lambda x , y : x + y, a, b)) -- Imprimindo a lista

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
list(map(lambda x, y, z : x + y + z, a, b, c))

--Programação Funcional - Programação Orientada à Expressão
map(Função, Sequência)
reduce(Função, Sequência)
lambda
list comprehension

## Utilizando a função REDUCE do pacote functools
from functools import reduce

-- Função manual para para somar valores
lista [10, 20 ,30, 40, 50]

def soma(a,b): -- Criando Função manual
    x = a + b
    return x

reduce(soma, lista) -- Chamando a função reduce que recebe como primeiro parâmetro, a entrada da função soma, que é aplicado ao segundo parâmetro, somando cada item conforme a função.
reduce(lambda x, y : x  + y, lista) -- Mesma chamada do anterior, porém no lugar da função soma é utilizado uma expressão lambda.
max_find = lambda a, b : a if (a > b) else b -- Expressão Lambda, porém salva em uma variável
type (max_find) -- Função que apresenta o tipo da função

reduce(max_find, lista)

## Utilizando a função FILTER do pacote
--Função para aplicar um filtro com uma determinada regra em uma sequencia de valores
filter(funcao, sequencia) -- Retornar um Iterator

# Criando uma função para calcular se um número é par ou impar, retornar um tipo booleano
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
verificaPar(50) -- Chamando a função para verificar se o número do parâmetro é par ou impar
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] -- Criando uma lista para ser utilizada
filter(verificaPar, lista) -- Utilizando a função filter para aplicar a função verificaPar na lista de valores - Valor retornado é um Iterator
list(filter(verificaPar, lista)) -- Convertendo o resultado final para uma lista para poder ser visualizada
list(filter(lambda x : x % 2 == 0, lista)) -- Possível utilizar no lugar da função verificaPar - uma expressão lambda diretamente
list(filter(lambda num : num > 8, lista)) -- Utilizando uma expressão Lambda para tratar outra situação, trás todos os números maiores que 8
    
## List Comprehension -- Recurso Python mais performatico que MAP, RECUDE, FILTER e Expressões LAMBDA
lst = [x for x in 'Laranja'] -- Cria uma lista onde cada caracter da palavra laranja é uma posição dentro da variável lst
print(lst) -- Imprimindo
type(lst) -- Exibindo tipo da variávlel

lst = [x**2 for x in range(0, 11)] -- Eleva a potência de 2 para cada valor da lista criada pelo range de 0 até 11
print(lst)

lst = [x for x in range(11) if x % 2 == 0] -- Para cada valor da lista criada com range, é retornado apenas os números pares, que atendem a condição IF
print(lst)

celsius = [0,10,20.1,34.5] -- Criado uma Lista que contêm valores em temperatura Celsius
fahrenheit = [ ((float(9)/5) * temp + 32) for temp in celsius ] -- Utilizando List Comprehension, é aplicado uma expressão que converte o valor da temperatura Celsius para Fahrenheit
A primeira parte é uma expressão que tem um parâmetro que faz referência a cada valor da lista Celsius.

print(fahrenheit)

-- Realizando uma operação Aninhada com List Comprehension / é elevado a potência de 2, uma lista que também está sendo elevada a potência de 2, gerada por um range
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)

-- ## Utilizando ZIP e ENUMERATE

zip(sequencia, sequencia) -- Agrega valores de duas sequencias e retorna uma tupla
enumerate(sequencia) -- Retorna o indice e valor de cada

# Criando duas listas
x = [1,2,3]
y = [4,5,6]

zip(x, y) -- Unindo as duas listas, retorna um Iterator
list(zip(x,y)) -- Convertendo o Iterator para ser exibido em uma lista

list(zip('ABCD', 'xy')) -- Unindo duas sequencias de caracteres, as tuplas montadas seram sempre com a quantidade da sequencia menor

a = [1,2,3]
b = [4,5,6,7,8]

list(zip(a, b)) -- Unindo duas sequencias de listas, as tuplas montadas seram sempre com a quantidade da sequencia menor

# Criando 2 dicionários - Chave : Valor
d1 = {'a': 1,'b': 2}
d2 = {'c': 4,'d': 5}

list(zip(d1, d2)) -- Unindo as CHAVES dos Dicionários 
list(zip(d1, d2.values())) -- Unindo a CHAVE do Dicionário d1, com o VALOR do dicionário d2

-- Função armazenada que realiza a mesma operação do comando anterior, de UNIR a CHAVE do Dicionário d1, com o VALOR do dicionário d2
-- Recebe como parâmetro os dois Dicionários, cria um Dicionário, e utilizndo um FOR, percorre as CHAVES de d1, e VALORES de d2 e salva no Dicionário criado
-- Por fim retorna o Dicionario
def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp

trocaValores(d1, d2) -- Chamando a função

-- ## Enumerate
# Criando uma lista
seq = ['a','b','c']
enumerate(seq) -- Retorna uma Enumerator
list(enumerate(seq)) -- Converte o Enumerator para lista, para ser exibido em lista

-- Utilizando um FOR e ENUMERATE para percorrer toda sequencia e imprimir sua CHAVE / VALOR, apelidados como indice / valor
for indice, valor in enumerate(seq):
    print (indice, valor)

-- Utilizando exemplo anterior, porem com uma condição if, que sai do loop for, quando o indice for maior ou igual a 2
for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print (valor)

-- Criando uma lista de Strings, que também é uma sequencia dentro do PYTHON
lista = ['Marketing', 'Tecnologia', 'Business']

-- Como exemplo posterior, utilizando FOR para percorrer e imprimir a sequencia
for chave, valor in enumerate(lista):
    print(chave, valor)

-- Utilizando FOR para percorrer e imprimir a sequencia da String
for chave, valor in enumerate('Isso é uma string'):
    print(chave, valor)

-- Utilizando FOR para percorrer e imprimir a sequencia criada usando RANGE - Cria a lista com 10 valores
for i, item in enumerate(range(10)):
    print(i, item)


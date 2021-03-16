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

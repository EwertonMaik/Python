## Desenvolvimento da Linguagem Python com conexão ao Banco de Dados MONGODB

## Comando de instalação do pacote para trabalhar e conectar com o MongoDB
## Comando deve conter a exclamação, pois faz parte da execução e instalação do SHELL
## pip é um pacote de instalção de programas do Python
!pip install -q pymongo

## Realizando a importação da função MongoClient que conecta ao Banco MongoDB
from pymongo import MongoClient

## Criando instância de objeto que conecta ao Banco de Dados MongoDB e passando os parâmetros de host e porta
conn = MongoClient('localhost', 27017)

## Usando a Função type para verificar o tipo de objeto
type(conn)

## OBS um Banco ou uma Collection do MongoDB só é criando efetivamente, quando o primeiro registros é inserido
## Uma instância permite a criação de diversos Bancos de Dados
db = conn.cadastradodb


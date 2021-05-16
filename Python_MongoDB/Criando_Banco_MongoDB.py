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

## Usando a Função type para verificar o tipo de objeto
type(db)

## Criando um objeto Collection, que é similar a uma tabela no modelo realcional de Banco de Dados
collection = db.cadastrodb

## Usando a Função Type para verificar o tipo de objeto
type(collection)

## Importando a pacote de data e hora para utilização em um INSERT
import datetime

## Criando uma variável DICIONÁRIO que recebe uma estrutura de JSON - com registro de Chave e Valor e possue lista também
post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": datetime.datetime.utcnow()}

## Usando a Função type para verificar o tipo do objeto
type(post1)

## Fazendo o Objeto COLLECTION receber receber a coleção chamada POST
collection = db.post

## Criando uma variavél que recebe e insere o registro da váriavel post1
## E em segundo momento, essa variável é chamada para visualização o id que foi gerado para o INSERT
post_id = collection.insert_one(post1)
post_id.inserted_id

## Criando uma 2º variável DICIONÁRIO que recebe uma estrutura de JSON - com registro de Chave e Valor e possue lista também
post2 = {"codigo": "ID-2209876",
        "prod_name": "Televisor",
        "marcas": ["samsung", "panasonic", "lg"],
        "data_cadastro": datetime.datetime.utcnow()}

## Fazendo o Objeto COLLECTION receber receber a coleção chamada POST
collection = db.posts

## Criando uma variavél que recebe e insere o registro da váriavel post2
post_id = collection.insert_one(post2).inserted_id

## Essa variável é chamada para visualização o id que foi gerado para o INSERT
post_id

## Utilizando a variável collection e chamando a função find_one para buscar o registro da chave / valor passado no parãmetro
collection.find_one({"prod_name": "Televisor"})

## utilizando a estrutura de controle FOR para percorrer a coleção COLLECTION post e buscar e imprimir cada registro
for post in collection.find():
    print(post)

## Comando para verificar o nome do Banco de Dados que esta em uso
db.name

## Utilizando Python para consultar dados no MongoDB

## Importando 
import pymongo

## Criando uma variável que recebe a conexão com o Banco de Dados MongoDB
## Quando não é passado o host e a porta de conexão ao Banco, por padrão é usado a DEFAULT loocalhost / 27017
client_con = pymongo.MongoClient()

## Usando a variável de conexão para chamar a função database_names() para listar os Bancos da Instância
client_con.database_names()

# Criando variável objeto que acessa o Banco de Dados cadastrodb
db = client_con.cadastrodb

## Usando a variável db que tem acesso ao banco cadastrodb e chamando a função collection_names() para listar as coleções do Banco
db.collection_names()

# Criando uma Coleção - COLLECTION dentro do Banco de Dados cadastrodb
db.create_collection("mycollection")

# Comando para Listar as COLLECTIOS do Banco de DADOS
db.collection_names()

# Realizando um INSERÇÃO no Banco (cadastrodb) e na coleção (mycollection)
db.mycollection.insert_one({
   'titulo': 'MongoDB com Python', 
   'descricao': 'MongoDB é um Banco de Dados NoSQL',
   'by': 'Data Science Academy',
   'url': 'http://www.datascienceacademy.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})

## Utilizando a Função find_one() para listar um registro da coleção
db.mycollection.find_one()

## Criando uma variável que contêm um dicionário de DADOS - Chave / Valor
doc1 = {"Nome":"Donald","sobrenome":"Trump","twitter":"@POTUS"}

## Adicionando um registro na Coeleção mycollection, passando a variável dicionário doc1
db.mycollection.insert_one(doc1)

# Criando uma segunda variável dicionário
doc2 = {"Site":"http://www.datascienceacademy.com.br",
        "facebook":"facebook.com/dsacademybr"}

# Adicionando um 2º Registro na Coleção mycollection, passando a variável dicionário doc2
db.mycollection.insert_one(doc2)

# Utilizando a estrutura de  controle FOR percorrer a coleção e imprimir
for rec in db.mycollection.find():
    print(rec)

# Criando uma nova
col = db["mycollection"]

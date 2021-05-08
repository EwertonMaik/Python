## Trabalhando com SELECT leitura de dados

-- Importando os pacotes que iremos trabalhar
import sqlite3
import random
import time
import datime

## Realizando a conexão com o arquivo do banco, caso não exista, é criado
conn = sqlite3.connect('dsa.db')

## Criando o objeto de conexão ao CURSOR
cur = conn.cursor()

## Criando uma função para criar uma Tabela
def create_table():
  cur.execute('CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
             'prod_name TEXT, valor REAL)' )

## Criando uma função para inserir apenas um registro
def data_insert():
  cur.execute("INSERT INTO produtos VALUES(002, '02-05-2020', 'teclado', 130)" )
  conn.commit()
  cur.close()
  conn.close()

## Criando uma função de INSERT que utiliza variáveis passada como parâmetro no VALUES
def data_insert_var():
  new_data = datetime.datetime.now()
  new_prod_name = 'monitor'
  new_valor = random.randrange(50, 100)
  cur.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?) ", (new_date, new_prod_name, new_valor) )
  conn.commit()

## Criando Função para Leitura de Dados
def leitura_todos_dados():
  cur.execute("SELECT * FROM PRODUTOS")
  for linha in cur.fetchall(): ## Utilizando FOR para percorrer todos os registros carregados com FETCHALL do cursor
    print(linha)

## Criando Função para Leitura de registros, porem com uma condição WHERE
  def leitura_registros():
    cur.execute("SELECT * FROM PRODUTOS WHERE valor > 60.0")
    for linha in cur.fetchall():
      print(linha)
 
## Criando Função para Leitura apenas da coluna 4 da tabela
def leitura_colunas():
  cur.execute("SELECT * FROM PRODUTOS") ## Apesar da query selecionar todos os campos
  for linha in cur.fetchall():
    print(linha[3])

## Executando as funções criadas
leitura_todos_dados()
leitura_registros()
leitura_colunas()
cur.close()
conn.close()

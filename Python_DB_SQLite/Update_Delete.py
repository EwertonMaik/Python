## Utilizando as instruções Update e Delete com SQLite

## Importando os pacote que serão utilizados
import sqlite3
import random
import time
import datetime

## Criando uma conexão com o arquivo do Banco Dados, caso não exista é criado
conn sqlite3.connect('dsa.db')

## Criando o objeto de conexão Cursor
cur = conn.cursor()

## Criando uma função para Criar uma TABELA
def create_table():
  cur.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
             'prod_name TEXT, valor REAL)' )

## Criando função para Inserir uma linha na tabela Criada
def data_insert();
  cur.execute("INSERT INTO produtos VALUES(002, '02-05-2020', 'teclado', 130 )" )
  conn.commit()
  cur.close()
  conn.close()

## Criando função para Inserir dados usando variáveis
def data_insert_var():
  new_date = datetime.datetime.now()
  new_prod_name = 'Monitor'
  new_valor = random.randrange(50, 100)
  cur.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?) ", (new_date, new_prod_name, new_valor) )
  conn.commit()

## Criando Função para Leitura de Dados
def leitura_todos_dados():
  cur_execute("SELECT * FROM PRODUTOS")
  for linha in cur.fetchall():
    print(linha)

## Criando Função de Leitura de registro filtrados com WHERE
def leitura_registros():
  cur.execute("SELECT * FROM PRODUTOS WHERE valor > 70.0")
  for linha in cur.fetchall():
    print(linha)

## Criando Função para Ler uma coluna em especifico
def leitura_colunas():
  cur.execute("SELECT * FROM PRODUTOS")
  for linhas in cur.fetchall():
    print(linha[3]) ## Passando a posição da COLUNA

## Criando Função para Atualizar Dados
def atualiza_dados():
  cur.execute("UPDATE PRODUTOS set valor = 70.00 WHERE valor = 98.0")
   conn.commit()

## Criando Função para Excluir Dados
def remove_dados():
  cur.execute("DELETE FROM PRODUTOS WHERE valor = 62.0")
   conn.commit()

## Executando as Funções Criadas
atualiza_dados()
leitura_todos_dados()
remove_dados()
leitura_todos_dados()

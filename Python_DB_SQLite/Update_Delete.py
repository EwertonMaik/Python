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

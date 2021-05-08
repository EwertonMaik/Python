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

## Criando

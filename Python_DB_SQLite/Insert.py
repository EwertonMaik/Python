-- Importando pacote OS e utilizando a função remove para remove-lo caso exista
import os
os.remove("dsa.db") if os.path.exists("dsa.db") else None

-- Importando pacote sqlite3 para acesso e manipulação ao Banco SQLite
import sqlite3
 
# Criando um objeto para conectar no arquivo do Banco dsa.db, caso ele não exista o arquivo é criado
conn = sqlite3.connect('dsa.db')   

# Criando um cursor para receber a conexão anterior criada
cur = conn.cursor()
 
# Criando uma função para  criar uma TABELA
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS produtos '\
                '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
                 'prod_name TEXT, valor REAL)')
    
# Criando uma função que aplica um INSERT na tabela anterior criada
def data_insert():
    cur.execute("INSERT INTO produtos VALUES(10, '2020-05-02 14:32:11', 'Teclado', 90 )")
    conn.commit() -- Sempre importante aplicar o commit para não ter transação em aberto e o dado não confirmado no banco
    cur.close()   -- Sempre importante fechar a conexão do Cursor
    conn.close()  -- Sempre importante fechar a conexão do objeto Connect SQLite

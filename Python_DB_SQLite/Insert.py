-- Importando pacote OS e utilizando a função remove para remove-lo caso exista
import os
import sqlite3
import time
import datatime


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


# Chamando a função para criação da TABELA e INSERT
create_table()
data_insert()


# Criando outra Função para aplicar uma INSERT, porém é passado os valores do VALUES como váriaveis
def data_insert_var():
    new_date = datetime.datetime.now()        # Váriável que irá receber a data e a hora sempre a cada iteração
    new_prod_name = 'Monitor'                 # Neste caso, a váriavel do nome do produto está fixa, porém poderia estar buscando de outro local
    new_valor = random.randrange(50,100)      # Aqui é gerado um valor randomico para cada iteração, mas poderia estar buscando o valor em outro local
    cur.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor)) # Cursor realizando a execução da iteração
    conn.commit() -- Aplicando commit

# Utilizando a estrutura de controle FOR para iterar de i até o range de 10
# Para cada Iteração é chamado e executado a função de insert com variável e executado do pacote time o sleep, para aguardar 1 segundo após cada execução do INSERT
for i in range(10):
    data_insert_var()
    time.sleep(1)

cur.close() -- Encerrando Cursor
conn.close() -- Encerrando Conexão

# Site Ooficial de Documentação do Banco SQLite - https://www.sqlite.org/index.html
# Este banco é instalado automaticamente com a instalação do Anaconda

# Importamndo módulo de acesso de arquivos do sistema operacional e removendo arquivo caso ele exista já criado
import os
os.remove("aqr_banco_sqlite.db") if os.path.exists("aqr_banco_sqlite.db") else None

# Importando módulo para manipulação ao Banco de Dados SQLite
# Em segundo momento cria um Objeto de conexão com o Banco de Dados - aqr_banco_sqlite.db
# Se esse arquivo do Banco não existe, um novo arquivo é criado
import sqlite3
con = sqlite3.connect('aqr_banco_sqlite.db')

# Usando o comando Type para verificar o tipo do Objeto
type(con)

# Criando um objeto do tipo Cursor, que pode percorrer os registros do Banco de Dados
# Esse objeto recebe a chamada o objeto con.cursor()
cur = con.cursor()

# Usando o comando Type para verificar o tipo do objeto
type(cur)

# Criando uma variável que recebe um texto, mais especiificamente um comando SQLite para criar uma tabela
sql_create_table = 'CREATE TABLE CURSOS ('\
                   'id INTEGER PRIMARY KEY, '\
                   'titulo VARCHAR(100), '\
                   'categoria VARCHAR(140) )'

# Utilizando o objeto Cursor para executar a query que esta contida na variável texto - Cria a tabela no Banco de Dados
cur.execute(sql_create_table)

# Criando uma variável que recebe um texto, mais especificamente o comando de INSERT sem os parâmetros de valor
sql_insert = 'INSERT INTO CURSOS VALUES (?, ?, ?)'

# Criando uma lista, onde cada posição contêm os valores da query INSERT
registros = [(1000, 'Ciência de Dados', 'Data Science'),
             (1001, 'Big Data Fundamentos', 'Big Data'),
             (1002, 'Python Fundamentos', 'Análise de Dados')]

# Utilizando a estrutura de controle FOR, para percorrer a lista e pegar cada valor das posições e passar como parâmetro na execução do INSERT
for reg in registros:
    cur.execute(sql_insert, reg)

# Executando através do objeto de conexão para aplicar o commit
con.commit()

# Criando uma variável para armazenar a query de SELECT na tabela CURSOS
sql_select = 'SELECT * FROM CURSOS'

# Utilizando o Cursor criado para executar a query select e após esses valores serem adicionados em uma variável
cur.execute(sql_select)
dados = cur.fetchall()

# Utilizando FOR para percorrer os valores e serem impressos com PRINT
for linha in dados:
    print('Id Curso : %d, Titulo : %s, Categoria : %s \n' % linha)

# Utilizando a variável registros já criada para receber novos valores para INSERT
registros = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
             (1004, 'R Fundamentos', 'Análise de Dados')]

# Utilizando FOR para percorrer a lista e inserir os registros
for reg in registros:
    cur.execute(sql_insert, reg)

# Aplicando o commit
con.commit()

# Utilizando o objeto cursor para executar o comando SQL, porém não passado como variável, e sim escrito diretamente
cur.execute('SELECT * FROM CURSOS')

# Carregando os valores na variável dados através do cursor
dados = cur.fetchall()

# Imprimindo os valores
for linha in dados:
    print('Id Curso : %d, Título : %s, Categoria : %s \n' % linha)

# Muito Importante - Sempre fechar a conexão com o Banco de Dados
con.close()
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
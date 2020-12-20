# Usando a Biblioteca Pandas para Trabalhar com arquivos:
# O Pandas é uma biblioteca do Python utilizada para análise e manipulação de dados e nos permite trabalhar de forma rápida e eficiente com arquivos do tipo csv,excel,txt,etc.
# O Pandas gera automaticamente um índice sequencial para cada linha do arquivo.
# A biblioteca fornece duas maneiras de estruturar os nossos dados:
# DataFrame que possui uma estrutura tabular de N-dimensões, onde cada coluna é um campo da tabela e cada linha um registro.
# Series que é uma matriz unidimensional que contém uma sequencia de valores acompanhado de seus respectivos índices.
# Funções para ler e converter dados tabulares: read_csv, read_excel e read_table

# Realizando a chamada de importação da biblioteca pandas e atribuindo um apelido para sua utilização
import pandas as pd

va01 = "arquivos/binary.csv" # Variável recebendo nome do diretório e arquivos a ser utilizado pelo pandas

df = pd.read_csv(va01)  # Variável recebendo a leitura feita pelo pandas

df.head() # Exibe a apresentação do arquivo de forma tabular, aceita parametro para delimitar suas linhas
df.head(10)

df.tail() # Exibe apenas os últimos 5 registros do arquivo

df.info() # Exibe diversas informações do arquivo

df.set_index('Department', inplace=True) # Definindo a coluna como Index

df.columns # Retorna o nome de todas as colunas da tabela

df.values # Retorna um array numpy - matriz - multi - dimencionais

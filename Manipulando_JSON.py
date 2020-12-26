# JSON - Java Script Objection Notation

# Criando uma dicionário de dados Python, onde sua estrutura é similar ao JSON, que tem Chave / Valor
dict = {
  'Nome': 'Guido van Rossum',
  'Linguagem': 'Python',
  'Similar': ['c', 'Modula-3', 'lisp'],
  'users': '1000000'
}

# Usando FOR para impprimir as chaves e valores do Dicionário
for k,v in dict.itens(): # Função do Dicionário para cada Chave / Valor
  print(k,v)

# Para manipular arquivos JSON, é utilizado a biblioteca json
import json

# utilizando uma função JSON para converter um Dicionário em json
json.dumps(dict)

# Criando um arquivo JSON - Modo w- writer
with open('arquivos/dados.json','w') as arquivo:
  arquivo.write(json.dumps(dict) ) # É escrito no arquivo o dodos do dicionário que são convertidos para json com a função dumps

# Abrindo o arquivo json anterior, agora em modo r - read
with open('arquivos/dados.json','r') as arquivo:
  texto = arquivo.read() # Variável texto recebe leitura do arquivo json
  data = json.loads(texto) # Variável data carrega os dados da variável texto em formato jason 

print(data) # Imprime todo o conjunto de chaves/valores
print(data['nome']) # Imprime só o valor da chave = nome

# Obtendo dados de um arquivo json da Internet
from urllib.request import urlopen # Importação da biblioteca

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]
print(data) # Imprimindo do o conjunto de chaves/valores
print(data['title']) # Imprimindo apenas o valor da chave title

# Pegando Dados de um JSON e Escrevendo um em TXT
import os

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

# Usando modo 01 - Abertuda do 1º arquivo em modo read e abertura do 2º arquivo em modo write
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)

# usando modo 02 - Abertuda do 1º arquivo em modo WRITE e abertura do 2º arquivo em modo READ - Obs, concatenado tudo na mesma linha
# Dentro do parâmetro do write é passado a abertuda do read
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read()) 

# Imprimindo arquivo TXT
with open('arquivos/json_data.txt','r') as arquivo: # Realizado abertura em modo read
    texto = arquivo.read() # Variável texto recebe a leitura do conteúdo
    data = json.loads(texto) # Variável data carrega dados da variável teto em formato JSON
print(data) # Imprimindo


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

print(data)


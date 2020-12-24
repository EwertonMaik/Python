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

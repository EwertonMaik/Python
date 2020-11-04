# 3 Principais Estruturas de Dados em Python são Listas, Dicionários e Tuplas

# Criando e realizando Operações com Dicionários - Mapeamento de Chaves e Valores {}

list01 = ["Maria", 30, "katia", 31, "Carina", 32] # Exemplo de Lista
dict01 = {"Maria":30, "katia":31, "Carina":32} # Exemplo de Dicionário de Dados Chave e Valor

dict01["Maria"] # Imprime o valor da chave "Maria"

dict01["Maria"] = 33 # Chave "Maria" recebe o valor 33
dict01["Joana"] = 34 # Chave e Valor não existe no dicionário, logo é adicionada

# Limpa todos os registros do Dicionário
dict01.clear()

# Exclui todo o Dicionário de Dados
del dict01

# Retorna o Tamanho do Dicionário
len(dict01)

# Imprime apenas as chaves do Dicionário
dict01.keys()

# Imprime apenas os valores do Dicionário
dict01.values()

# Imprime o conjunto de chave e valor todo dicionário
dict01.items()

# Criando um 2º Dicionário de Dados
dict02 = {"Caio":29, "Pedro":28, "Fernando":32}

# Atualiza Dicionário - É adicionada os valores do 2º Dicionário ao 1º
dict01.update(dict02)

# Criando um Dicionário Vazio
dict03 = {}

# Criando um Dicionário contendo um Lista internamente
dict04 = { 'key01':1234, 'key02':[10, 20, 30, 40], 'key3':['leite', 'ovo', 'açucar'] }

print(dict04)
print(dict04['key02']) # Imprime apenas os valores da chave 'key02'

print( dict04['key02'][0].upper() ) # Imprime apenas o valor da posição 0 da chave 'key02' e a converte para Maiúsculo

# Dicionário Aninhados - Um Dicionário Dentro do Outro
dict05 = { 'key01':{'key001'}:{'key0001'}: 'Valor - Dicionário Alinhado' }

print(dict05['key01'] ['key001'] ['key0001']) # Imprimindo o valor do Dicionário Aninhado




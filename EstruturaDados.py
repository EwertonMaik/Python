# 3 Principais Estruturas de Dados em Python são Listas, Dicionários e Tuplas

# Criando e realizando Operações com Listas

list01 = ["ovos, farinha, leite, maças"] # Uma lista com uma única string
list02 = ["ovos", "farinha", "leite", "maças"] # Uma lista com 4 registros
list03 = [10, 200, "Lista com INT e STRING"] # Lista com valores de tidos distintos

# Variáveis recebendo atribuição de valores de cada posição da lista
var01 = list03[0]
var02 = list03[1]
var03 = list03[2]
var04 = list03[3]

#Imprimindo Listas
print(list01)
print(list02)
print(list03)

# Atualizando item da Lista
list02[3] = "melancia" # Alterado o valor na posição 3 de "maças" para "melancia"

# Excluindo item da Lista
del list02[3] # Excluido o valor e a posição 3 lista


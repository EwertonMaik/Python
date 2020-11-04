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

# Lista Aninhada, uma Lista dentro de outra Lista (MATRIZ)
list04 = [ [1, 2, 3], [a, b, c, d], [10, 20, 30, 40] ] # Lista Aninhada contendo 3 listas

print(list04[0]) # Imprimindo a posição 0 da lista
var05 = list04[1] # Variável recebendo a lista da posição 1

# Imprimindo valores da Lista passando a Posição da Linha e Posição da Coluna
print(list04[0][0]) 
print(list04[1][2])
print(list04[2][3])

# Concatenando Listas
list05 = list02 + list03

print(list05)

# Verificando se um valor existe dentro Lista
print("ovos" in list02) # Se o valor "ovos" existe dentro da list02

len(list02) # Tamanho da Lista
max(list02) # Retorna o Maior Valor da Lista
min(list02) # Retorna o Menor Valor da Lista
list02.append("abacaxi") # Adiciona um valor na Lista
list02.count("abacaxi") # Quantas vezes o parâmetro existe na Lista

# Criando uma Lista Vazia
list06 = []

# Utilizando um FOR para percorrer um lista e adicionar em outra
# Adiciona na list06 vazia, os valores da list02
for item in list02:
  list06.append(item)

# Adicionando valores com Extend
list02.extend(['uva', 'morango'])
print(list02)

# Retorna o Indice de um Elemento na Lista
list02.index("leite")

# Adiciona um valor na lista na posição informada nº 2
# E o valor que estava nessa posição passa para a proxima posição e assim por diante com os demais
list02.insert(2, "carro")

# Removendo valor da Lista
list02.remove("carro")

# Invertendo os valores da Lista
list02.reverse() # Trás a listagem ao inverso, do fim para o inicio

# Ordenando os valores a Lista / Seja numérico ou alfabetico
list02.sort()




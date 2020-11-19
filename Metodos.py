-- Os métodos são funções incorporadas em objetos permite executar ações especificas no objeto e podem possuir argumentos como as funções
--Métodos de uma lista:
append
count
extend
insert
pop
remove
reverse
sort

--Criado uma Lista e atribuido valores
lista01 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

--Método para adicionar valores a lista
lista01.append(10)

--Método que adiciona valores a lista, porém precisa informar a posição e valor desejado
lst.insert(5, 11)

--Método que limpa todos valores da lista
lista01.clear()

--Formas de imprimir valores de uma lista
lista01
print(lista01)
print(lista01[3])

--Método para contar quantas vezes um valores aparece na lista
lista01.count(6)

--Método que ajuda e retorna a sintaxe do método
help(lista01.count)

--Método que lista todos métodos existente para o objeto do parâmetro
dir(lista01)

srt01 = 'Esta é uma string Python'

--Método que corta uma string em pedaços baseado em seu parêmetro
print(str01.split() )

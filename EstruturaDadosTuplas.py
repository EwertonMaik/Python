-- Estrutura de Dados Tuplas - Semelhantes às listas, porém são imutáveis, não podem ser alterados.
-- Muito usado em dados envolvendo calendário.

--Criando uma Tupla
tupla01 = ("Português", 8, "Matemática")

--Não possui métodos de adição como append ou del para exclusão de valores da tupla
--Ou de alteração
tupla01[1] = 20 -- Isso obtêm erro, devido tuplas serem imutáveis

--Listando valores da tupla
print(tupla01)

tupla01[2]

--Retorna tamanho da tupla
len(tupla01)

--Retornando fatias da tupla
tupla01[1:] -- retorna da posição 1 em diante

--Retornando o index de um valor dentro da tupla
tupla01.index('Matemática')

-- Convertendo uma TUPLA para lista com a função List
lista01 = list(tupla01)

-- Convertendo um LISTA para um Tupla com a função Tuple
tupla02 = tuple(list01)

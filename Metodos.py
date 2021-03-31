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

## Criando uma classe CIRCULO e adicionando métodos para realizar operações e gerenciar os atributos da classe
class Circulo():
    pi = 3.14 # O valor de pi é constante

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio = 5):
        self.raio = raio 

    # Esse método calcula a área. Self utiliza os atributos deste mesmo objeto
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio

circ = Circulo() # Instânciado um objeto da classe Clirculo
circ.getRaio() # Obtendo o valor do Raio do Objeto circ - Circulo
circ1 = Circulo(7) # instânciando um 2º Objeto Circulo e já definindo via parâmetro o seu atributo raio
circ.setRaio(3) # Utilizando o método interno da classe Circulo desenvolvido, que permite alterar o valor do raio, chamando o método e passandp seu valor de parâmetro







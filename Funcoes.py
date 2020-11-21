-- Funções em Python
#formato geral de uma função é:
def nome da função(arg1, arg2):

--Criando Funções
def minhaFuncao():
    print('Bem Vindo')

--Chamando a execução da função
minhaFuncao()

--Criando uma função que possui entrada de parâmetro
def segundaFuncao(nome):
    print('Olá %s ' %(nome) )

--Chamando a função
segundaFuncao('Maria')

--Criando uma função e utilizando For
def terceiraFuncao():
    for i in range(1, 10):
        print("Hoje é dia " + str(i) )

--Criando uma função para soma
def somaDoisNumeros(num01, num02):
    print("Primeiro Número : " + str(num01) )
    print("Segundo Número : + str(num02) )
    print("Soma : ", num01 + num02)

--Chamando Função
somaDoisNumeros(50, 50)

--Exemplo de Variável Global e Local
var_global = 20 # Variável Global acessivel de qualquer parte do programa

def soma(num01, num02):
    var_local = num01 + num02 #Variável Local acessivel apenas dentro destr bloco de função
    print(var_local)

--Usando Funções para COnversão - srt, int, float
idade = input("Digite sua Idade: ") # Desta forma ocorre erro devido idade receber uma string e ser camparada logo após com um tipo número
idade = int(input("Digite sua Idade: ") )
if idade > 17:
    print("Você é Maior de Idade!")

int("100") #Texto '100' é convertido para o tipo número 100
float("100.225") #Texto '100.225' é convertido para o tipo float 100.225
str(100) #Converte o número 100 para um texto '100'
len([1, 2, 3, 4, 5, 6]) #Retorna o tamanho do objeto
lista01 = ['a', 'b', 'c', 'd', 'e']
lista02 = [1, 2, 3, 4, 5]
max(lista01) #Retorna o valor máximo da lista
min(lista01) #Retorna o valor minimo da lista
sum(lista02) #Retorna a soma dos valores da lista

--Definindo uma função que recebe mais de um parâmetro
def funcaoParVariavel( par01, *parN): # O * indica que mais de 1 parâmetro pode ser passado!
    #Imprime o 1º Parâmetro
    print("O 1º parâmetro é: ", par01)

    #Imprime o 2º Parâmetro
    for i in parN:
       print("O parâmetro passado é : ", i)
    return;

var01 = 'Texto sera cortado e separado pela função Split'

print(var01.split(" ") ) #Corta a string var01 pelos espaços
print(var01.lower() ) #Imprime tudo em caixa baixa
print(var01.upper() ) #Imprime tudo em caixa alta

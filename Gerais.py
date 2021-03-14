# Instruções Gerais

# Iniciando o Anaconda Navigator via linha de comando
anaconda-navigator

# Iniciando o Jupyter Notebook via linha de comando
jupyter notebook

# Executando um script Python via linha de comando
C:\PythonFundamentos>python hello.py

# É possível executar o script dentro do shell(Interpretador) do Python, iniciando o console do Python
python

# Pequeno exemplo calculando e escrevendo valores em tela
>>> 2 + 2
4
>>>("Hello World!")
Hello World!

# Váriável Declarada e impressa com função print
varString = "Pedro"
print(varString)

# Operações Aritiméticas
2 + 2  # SOMA
10 - 5 # SUBTRAÇÃO
20 / 2 # DIVISÃO
6 ** 2 # POTÊNCIA
10 % 2 # MÓDULO (RESTO DA DIVISÃO)

# Operações com Função Built-In
type(10)   #Rertorna o tipo INT
type(10.0) #Retorna o tipo FLOAT
a = 'Texto String';
type(a)    #Retorna o tipo STRING

# Operações com FLOAT
# Float com Float retorna um Float
# Float com Int retorna Float
# Int com Int retorna Int ou Float dependendo da operação de / ou *

# Operação de conversão
float(7) # Converte para 7.0
int(5.0) # Converte para 5
int(5.5) # Converte para 5, pega só a parte inteira do Nº

# Operação coversão para Hexadecimal e Binário
hex(568) #Hexadecimal
bin(622) #Binário

# Operações com Funções
abs(-9) # Retorna valor absoluto
round(3.14151922, 2) # Retorna o Nº aredondado para 2 casa decimais
pow(5, 2) # Retorna potência

# Declaração Multipla de Variável
var01, var02, var03 = "Jose", "Carlos", "Silva"

# Cálculo entre variáveis
largura = 2
altura = 4
area = largura * altura
print(area)

# Concatenação de String
nome = "Pedro"
sobrenome = "Paulo"
nomeCompleto = nome + " " + sobrenome
print(nomeCompleto)
nomeCompleto # A variável é impressa simplesmente sem a função print também

# String armazenam informações em formato texto, em uma sequência de caracteres e tem o controle de cada elemento.
# Em Python, String aceita aspas SIMPLES ou DUPLA
# Colchetes [] representa o índice de um objeto. 0 é o primeiro valor.
texto = "Python e Análise de Dados"
# Imprime os valore das posições 0, 1, 2
texto[0]
texto[1]
texto[2]

print('Texto com Aspas Simples')
print("Texto com Aspas Dupla")

# Quebra de linha dentro da String
print("O texto \n Aqui em outra Linha \n Aqui em outra Linha")

# SLICING - Trabalha com corte da String
s = "ABCDEFGHIJ"
s[1:] # Imprime da posição 1 até p fim da String
s[:3] # Imprime da posição 0 até a posição 3 da String
s[:]  # Imprime toda String
s[-1] # Imprime do fim para o início, neste caso só a última posição (J)
s[:-1] # Imprime tudo, exceto a última posição

s[::2] # Imprime a string pulando sempre a cada 2 caracteres
s[::-2] # Mesma função da anterior, porém do fim para o início

# Imprimindo um valor da variável usando operador de multiplicação
letra = "X"
letra * 3
>>> XXX

# Demais Funções com String
s = "abcdefghij"
s.upper() # Imprime tudo Maiúsculo
s.lower() # Imprime tudo Minúsculo
s.split() # Divide a string por padrão nos espços em Branco
s.split('e') # Divide a string ao encontrar o caracter (e)

s.Capitalize() # Imprime a string com apenas a 1º Posição em Maiúsculo
s.count('a') # Retorna a quantidade de caracteres, neste caso conta apenas (a)
s.find('g') # Pesquisa e retorna a posição do caractere passado como parâmetro
s.islower() # Retorna False ou True, se tem caracter Minúsculo
s.isspace() # Retorna False ou True, se tem espaços
s.endswith('o') # Retorna False ou True, se a string termina com o parâmetro passado

# Comparando String
print("Python" == "R")
>>> False

print("Python" == "Python")
>>> True



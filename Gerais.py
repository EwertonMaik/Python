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

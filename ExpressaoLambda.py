Expressões Lambda ou Função Inline - funções Anonimas
O corpo do Lambda é uma única expressão, e não um bloco de instrução.

def - cria um objeto e atribui um nome a ele - nome da função
lambda - cria um objeto, mas o retorna como um resultado em tempo de execução

exemplo :
lambda x: x**2

--Primero exemplo de uma função Lambda - Retorna Potência de um número
varpotencia = lambda num: numm**2
potencia(5)

--Essa expressão usando Lambda pode ser feita no modelo padrão com função, segue 3 exemplos
def potencia(num):
	resultado = num**2
	return resultado

def potencia(num):
	return num**2

def potencia(num): return num**2

--
var01 = lambda x: x%2 == 0  # Retorna Valor Boleano se Resultado do Nº é igual a 0
var01(3)

varTexto = lambda s: s[0] # Retorna o valor da String na Posição 0
varTesto('Python')

soma = lambda x, y: x + y # Retorna a soma de dois números
soma(10, 20)

reverso = lambda s: s[::-1] #Retorna a string impressa ao contrario
reverso('Python')

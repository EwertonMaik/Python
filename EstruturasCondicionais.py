-- Estruturas Condicionais
-- If/ Else/ Elif
-- Repetição

--Condicional Simples
if (expressao 1):
	print("Comando Executado caso a expressão 1 seja Verdadeira")
else:
	print("Comando executado caso a expressão 1 seja Falsa")

--Condicional Aninhada
if (expressao 1):
	print("Comando Executado caso a expressão 1 seja Verdadeira")
elif (expressao 2):
	print("Comando executado caso Expr. 1 seja falso, e Expr. 2 seja verdadeira")
else:
	print("Comando executado caso a expressão 1 e e sejam Falsa")

-- Simples
if 10 > 5:
	print("Sim! 10 é Maio 5")

if 10 > 20:
	print("Sim!")
else :
	print("Não")

Nome = "Pedro"
Idade = 20
if Nome == "Pedro":
   if Idade == 20:
	print("Pedro tem 20 Anos!")
else:
	print("Invalido!")

if Idade >= 20 and Nome == "Pedro" -- Usando o Operador AND - As duas espressões devem ser verdadeiras
	print("Liberado!")
else:
	print("Bloqueado!")

-- Aninhada
dia = "Quarta"
if dia == "Quinta":
	print("Hoje é Quinta!)
elif dia == "Quarta":
	print("Hoje é Quarta!")
elif dia == "Terça":
	print("Hoje é Terça!")
else:
	print("Dia Inválido!")

if Idade >= 20 or Nome == "Pedro" -- Usando o Operador OR - Pelo menos uma expressão deve ser verdadeira
	print("Liberado!")
else:
	print("Bloqueado!")


-- Usando Entrada de dados com INPUT
nun01 = input('Digite um Número : ') -- Variável recebe valor digitado pelo usuário
	      
if (num01 % 2) == 0:
	print("Número Par!")
else:
	print("Número Impar!)

--Usando PlaceHolders para exibir valores
var01 = 'Variável 01'
var02 = 'Variável 02'
print('Imprimindo o valor var01 = %r e o valor de var02 = s%' %(var01, var02)) -- Onde existe um letra com % é substituido pelo valor das variáveis %(var01, var02) conforme a ordem






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

if Idade >= 20 and Nome == "Pedro"
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

-- Estruturas Condicionais
-- If/ Else/ Elif
-- Repeticao - LOOP FOR, WHILE

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

--Condicional While
while (expressao1):
	print("Comando executando enquanto a expressão1 for verdadeira")

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

--Utilizando a estrutura Loop For

--Usando For para imprimir valores de uma TUPLA
tupla01 = (1, 2, 3, 4, 5)
for i in tupla01:
	print(i)

--Usando For parar imprimir valores de uma LISTA
lista01 = ['Carro', 'Moto', 'Bicicleta']
for i in lista01:
	print(i)

--Imprime os números pares da lista, realizando divisão por mod, resto da divisão igual a zero	      
lista02 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lista02:
	if i % 2 == 0:
	      print(i)

--Imprimindo valores com RANGE
for cont in range(0,5):
	print(cont)

--Imprimindo valdores com RANGE de 0 até 50 e pulando em 2 em 2   
for cont in range(0,50,2):
	print(cont)

--Imprimindo sequencias de uma string
for string in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
	print(string)

--Loops Aninhados - Um Loop For dentro de outro Loop For
--A lista de 0 a´te 3 será repetida 5X
for a in range(0, 5):
	for b in range(0, 3):
	   print(b)

--Usando um Loop For para Somar os valores de uma Lista e utilizando um contador
lista03 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
soma = 0
count = 0
for i in lista03:
	soma += i --Isso é igual a soma = soma + i
	count += 1 --Isso é igual a count = count + 1
print(soma)
	  
--Imprimindo Listas dentro de uma Lista
lista04 = [ [1, 2], [1, 2, 3], [1, 2, 3, 4] ]
pos = lista04[2] -- recebe os valores da posição 2
for i in lista04:
	print(lista04)
	print(pos)

--Pesquisando valores na Lista
lista05 = ['A', 'B', 'C','D','E','F']
pesquisa = input('Digite o valorer que deseja buscar: ')
for i in lista05:
	if i == pesquisa:
	  print('Valor %r Encontrado na Lista' %(i) )









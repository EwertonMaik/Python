-- Tratamento de Erros e Exceções
-- Lista de Biblioteca Exceções Python - https://docs.python.org/3.6/library/exceptions.html
  
-- Execução da linha obtem erro devido a falta da 2º ASPAS Simples
print('Olá)
-- SyntaxError: EOL while scanning string literal


-- Criado uma simples função que divide um número pelo outro
def numDiv (num1, num2):
    resultado = num1 / num2
    print(resultado)

numDiv(4,2) -- Esta execução é bem sucedida
numDiv(4,0) -- Esta execução obtem (ZeroDivisionError: division by zero), não é tratado a Exceção de divisão por ZERO

-- A instrução abaixo obtem erro, pois não é possivel somar um tipo número com um tipo string
8 + 's' -- TypeError: unsupported operand type(s) for +: 'int' and 'str'

-- Utilizando TRY e EXCEPTION para tratar o erro anterior
-- Sabendo que a operação obtem erro, é executado a parte do Exception, que emite a mensagem que a operação não é permitida
try:
    8 + 's'
except TypeError:
    print("Operação não permitida")



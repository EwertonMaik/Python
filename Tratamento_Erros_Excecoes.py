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

-- Utilizando TRY, EXCEPTION e ELSE
-- No Bloco TRY é adicionado as linhas de código que devem ser executadas e podlem ocorrer um possível erro de exceção
-- EXCEPTION é o bloco que é executado quando ocorre a Exceção
-- ELSE é o bloco que é executado quando não ocorre Exceção, é bem sucedido. f.close() - fecha a conexão aberta com o arquivo
-- Esta código abaixo o aquivo existe e o processo é concluido com sucesso!
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()

-- Assim como o código anterior, porém apenas sem a extensão do arquivo, e aberto apenas para leitura
-- Este exemplo obtem o erro - "Erro: arquivo não encontrado ou não pode ser lido."
try:
    f = open('arquivos/testandoerros','r')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()

-- Este proximo exemplo, é bem sucedido, e tem adicionado o bloco FINALLY, que é executado independente se houver um Exception, ou se não houver erro, sendo ELSE executado.
-- O bloco FINALLY sempre é executado, muito usado para sempre fechar uma conexão que foi aberta ou algo importante que sempre deve ser executado
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()
finally:
   print ("Comandos no bloco finally são sempre executados!")

-- A função abaixo, é criada e compilada com sucesso, porêm possue uma Exceção não tratada que obtem erro
-- ValueError: invalid literal for int() with base 10: 'a'
-- Todo caracter digitado com a entrada do input, é convertido para um INTEIRO
-- Ao dar ENTER ou digitar uma entrada de letra, ou caracter que não seja número, o erro é obtido
def askint():
        try:
            val = int((input("Digite um número: ")))
        except UnboundLocalError:
            print ("Você não digitou um número!")
        finally:
            print ("Obrigado!")
        print (val) 

-- Mesma função anterior criada, porém com a modifição melhorada, adicionado a estrutura de controle WHILE e CONTINUE, que fica repetindo continuamente,
pedindo para o usuário digitar um caracter número corretamente, ou seja, digitou errado, cai na Exception e o CONTINUE repete o processo.
def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print (val)

-- Neste exemplo é criado uma TUPLA, onde seu conteúdo não pode ser alterado e adicionado
-- Dentro do bloco TRY é adicionado um instrução para aplicar uma append a tupla, logo isso obtem um erro
-- E é possível adicionar mais de um Exception, justamente para tratar diferentes possiveis tipos de erro
-- AttributeError - Classe que trata Exceções relacionadas a atributos, referências e atribuições
-- IOError - Classe que trata Exceções relacionadas uma operação de IO - Input ou Output falha
-- Erro:  'tuple' object has no attribute 'append'
tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print('Erro: ', e)
except IOError as e:
    print('Erro de I/O:', e)

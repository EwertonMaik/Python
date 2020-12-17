print("\n******************* Python Calculator *******************")

print("\n Selecione o número para operação desejada: ")
var01 = 0

#Funções para as operações Matemáticas
def opSoma(num01, num02):
    return num01 + num02

def opSubtracao(num01, num02):
    return num01 - num02

def opMultiplicacao(num01, num02):
    return num01 * num02
    
def opDivisao(num01, num02):
    return num01 / num02

#Função para ser chamada e sair da Condicional WHILE
def sair():
    global var01
    var01 = 1

while var01 == 0:
        print("1 - SOMA / 2 - SUBTRAÇÃO / 3 - MULTIPLICAÇÃO / 4 - DIVISÃO / 0 - SAIR CALC.")
        var02 = input("Digite o Nº operação desejada: ")
        
        if var02 == "0":
            #Sai o Programa
            sair()
            print("Calculadora Encerrada!")
            
        elif var02 == "1" or var02 == "2" or var02 == "3" or var02 == "4":
            var03 = int(input("Digite nº 01 : ") )
            var04 = int(input("Digite nº 02 : ") )
        
            if var02 == "1":
                #chama função soma
                result = opSoma(var03, var04)
                print('Resultado : %r' %(result) )

            elif var02 == "2":
                #chama função subtração
                result = opSubtracao(var03, var04)
                print('Resultado : %r' %(result) )

            elif var02 == "3":
                #chama função multiplicação
                result = opMultiplicacao(var03, var04)
                print('Resultado : %r' %(result) )

            elif var02 == "4":
                #chama função divisão
                result = opDivisao(var03, var04)
                print('Resultado : %r' %(result) )
        else:
            print("Por favor, Digite um opção correta! de (0 à 4)")
            

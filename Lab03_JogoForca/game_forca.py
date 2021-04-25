# Jogo Da Força - Usando Programação Orientada a Objetos

# Importando Biblioteca Random
import random

# Criando uma Lista para armazenar em cada posição um STATUS
# Que representa a evolução da FORCA - TABULEIRO DO JOGO
tabuleiro = ['''

>>>>>>>>>> TABULEIRO - JOGO DA FORCA X <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Criando Classe do JOGO DA FORCA
class JogoForca:
    # Criando o Método Construtor que recebe como parâmetro uma palavra
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_errada = []   # Lista para armazenar letras erradas
        self.letra_certa = []    # Lista para armazenar letras certas

    # Criando Método para verificar se a Letra foi Adivinhada CERTA ou ERRADA
    def adivinhar(self, letra):
        if letra in self.palavra and letra not in self.letra_certa:
            self.letra_certa.append(letra)
        elif letra not in self.palavra and letra not in self.letra_errada:
            self.letra_errada.append(letra)
        else:
            return False
        return True

    # Criando Método para verificar se o Jogo Terminou
    def jogoforca_terminou(self):
        return self.jogoforca_venceu() or (len(self.letra_errada) == 6)

    # Criando Método para verificar se o Jogador Venceu # Se não existir o (_) underline na palavra, o jogador venceu
    def jogoforca_venceu(self):
        if '_' not in self.palavra_oculta():
            return True
        return False

    # Criando Método para não exibir letra do tabuleiro do jogo
    def palavra_oculta(self):
        exibir = ''
        for letra in self.palavra:
            if letra not in self.letra_certa:
                exibir += '_'
            else:
                exibir += letra
        return exibir

    # Criando Método para verificar status do jogo e imprimir o tabuleiro em tela
    def imprimir_satus_jogo(self):
        print(tabuleiro[len(self.letra_errada)])
        print('\nPalavra: ' + self.palavra_oculta())
        print('\nLetras Erradas: ',)
        for letra in self.letra_errada:
            print(letra,)
        print()
        print('\nLetras Corretas: ',)
        for letra in self.letra_certa:
            print(letra,)
        print()

# Criando Método para escolher palavra aleatória no banco de Palavras
def escolher_palavra():
    with open("palavras.txt", "rt") as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

# Criando Método Main Para Executar o Programa
def main():
    # Criando uma instância - objeto da Classe JogoForca
    jogo = JogoForca(escolher_palavra() )

    # Bloco While para controlar o jogo. Enquanto não terminar o Jogo, imprime status, solicita letra e faz leitura
    while not jogo.jogoforca_terminou():
        jogo.imprimir_satus_jogo()
        entrada = input('\nDigite uma Letra: ')
        jogo.adivinhar(entrada)

    # Verifica Status do Jogo
    jogo.imprimir_satus_jogo()

    # De acordo com o status, imprime mensagem para o usuário
    if jogo.jogoforca_venceu():
        print('\nParabêns! Você Venceu!')
    else:
        print('\nGame Over! Você Perdeu!')
        print('\nA Paravra era : ' + jogo.palavra )

    print('\nFoi Otímo jogar com você, Agora vai Estudar!')

# Chamada para executar o PROGRAMA
if __name__ == "__main__":
    main()
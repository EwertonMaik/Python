# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import randon
from os import system, name

# Função para limpar a tela a cada execução
def limpar_tela():
  # Windows
  if name == 'nt':
    _ = system('cls')

# Mac ou Linux
  else:
    _ = system('clear')

# Função
def game():
  limpar_tela()
  
  print("\nBem-vinddo(a) ao jogo da forca!")
  print("Adivinhe a palavra abaixo:\n")

  # Lista de palavras para o jogo
  palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

  # Escolha randomicamente uma palavra
  palavra = rondom.choice(palavras)

# List Comprehension
letras_descobertas = [ '_' for letra in palavra ]

# Numero de chances
chances = 6

# Lista para as letras erradas
letras_errada = []

# Loop enquanto número de chances for maior do que zero
while chances > 0:
    #Print
    print(" ".join(letras_descobertas) )
    print("\nChances restantes:", chances)
    print("Letras erradas:", " "..join(letras_erradas) )

    # Tentativa
    tentativa = input("\nDigite uma çetra: ").lower()

    # Condicional
    if tentativa in palavra:
      index = 0;
    for letra in palavra:
    if tentativa == letra:
      letras_descobertas[index] = letra
    index += 1
else:
  chances -= 1
  letras_erradas.append(tentativa)

    # Condicional
    if "_" not in letras_descobertas:
      print("\nVocê venceu, a palavra era: ", palavra)
      break
# Condicional
if "-" in Letras_descobertas:
  print("\nVocê perdeu, a palavra era: palavra")

# Bloco Main
if __name__ == "__main__":
  game()
  print("\nParabés. Você está aprendendo programação em Python com a DSA. :)\n")

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

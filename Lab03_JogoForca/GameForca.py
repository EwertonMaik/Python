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

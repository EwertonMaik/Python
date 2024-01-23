# Criando uma classe chamada Livro
class Livro():
  # Este método vai inicializar cada objeto criado a partir desta classe
  # O nome deste método é __init__
  # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
  def __init__(self):
    # Atributos são propriedades
    self.titulo = 'sapiens - Uma Breve História da Humanidade'
    self.isbn = 9988888
    print("Contrutor chamado para criar um objeto desta classe.")

  # Métodos são funções que executam ações nos objetos da classe
  def imprime(self):
    print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn) )

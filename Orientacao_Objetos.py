## ORIENTAÇÃO A OBJETOS
## CLASSES

-- Criando uma classe LIVRO
 class Livro():
    def __init__(self): -- Método construtor da classe
    self.titulo = 'Banco de Dados' -- Criado e Definido uma atributo para classe
    self.isbn = 123456789
    print("Metodo print para imprimir e informar que dentro deste método construtor tem dois atributos que são inicializado ao instância a classe")
    
    
    def imprime(self): -- 2º Método criado que pertence a classe Livro
    print("Foi criado o livro %s e ISBN %d" %(self.titulo, self.isbn))

-- FIM da classe


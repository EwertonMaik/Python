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

Livro1 = Livro() -- Realizndo a instânciação do Objeto Livro1 que pertence a classe Livro
type(Livro1) -- Consultando o tipo do Objeto

-- Criando a classe LIVRO novamente, porém com os parâmtros de seu método construtor, não manual, e sim recebidos via parãmtro
class Livro():
    def __init__(self, titulo, isbn): -- Metódo construtor recebendo parâmentros que são atribuidos aos atributos do construtor
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe")
        
    def imprime(self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" %(titulo, isbn))
-- FIM da classe

Livro2 = Livro("Python Fundamentos", 77886611) -- Instãnciando um objeto da classe Livro e já passando via parãmetro os seus atributos
Livro2.titulo -- Consultando o valor que existe dentro do atributo titulo do objeto Livro2

-- Criando um 3º Classe - Cachorro, e adicionado o metódo construtor, recebendo dois parâmetros
class Cachorro():
    def __init__(self, raça):
        self.raça = raca
        print("Construtor chamado para criar um objeto desta classe")
-- FIM da classe

Rex = Cachorro(raca='Labrador') -- Instânciado objeto da classe Cachorro, que recebe via parâmetro o nome da raça
Golias = Cachorro(raca='Huskie') -- Mesmo exemplo anterior, porém outro objeto

Rex.raca -- Consultando o valor do atribudo raca de cada Objeto criado
Golias.raca






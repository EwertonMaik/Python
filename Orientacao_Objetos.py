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

## Tudo na Linguagem Python é orientado a objetos
lst_num = ["Data", "Science", "Academy", "Nota", 10, 10] -- Criado uma lista que pertence a classe List, o interpretador sabe pela utilização das chaves
type(lst_num) -- Consultando o tipo do Objeto criando anteriormente

-- Utilizando o método print para consultar e imprimir o tipo de cada tipo de objetos do Python
print(type(10)) -- INT - Inteiro
print(type([])) -- LIST - Lista
print(type(())) -- TUPLE - Tuplas
print(type({})) -- DICT - Dicionário
print(type('a')) -- SRT - String

-- Criando uma classe Funcionarios para os exemplos seguintes
class Funcionarios:
    def __init__(self, nome, salario): -- Méptodo construtor que recebe 2 parâmetros
        self.nome = nome
        self.salario = salario

    def listFunc(self): -- Método para Listar o Funcionário cadastrado
        print("O nome do funcionário é " + self.nome + " e o salário é R$" + str(self.salario))
-- FIM da classe

Func1 = Funcionarios("Santos", 20000) -- Instância objeto da classe funcionário e atribuido um nome e salário do funcionário
Func1.listFunc() -- Consultando dados inseridos anteriormente

## Varios métodos do Python para gerenciar atributos
hasattr(Func1, "nome") -- Método que pergunta para o objeto "Func1" se existe o atributo "nome" - Retorna TRUE ou FALSE
hasattr(Func1, "salario") -- Mesmo exemplo anterior, porém para outro atributo
setattr(Func1, "salario", 4500) -- Pergunta para o objeto se existe o atributo informado, caso exista, atribuido o novo salário de 4.500, caso não é criado e atribuido o valor
getattr(Func1, "salario") -- Consultando ao Objeto Func1 o valor do atributo salário
delattr(Func1, "salario") -- Deletando o atributo "salário" do objeto "func1"

## Herença
-- O exemplo a seguir demonstra a utilização de Heraça de uma classe especifica herdando atributos de uma classe genérica
-- Classe Animal e Classe Cachorro

class Animal(): -- ANIMAL
    def __init__(self): -- Método Construtor
        print("Animal criado")

    def Identif(self): -- Método de Identificação
        print("Animal")

    def comer(self): -- Método comum entre todos animais
        print("Comendo")

-- Classe CACHORRO que herda da Classe ANIMAL
class Cachorro(Animal):
    def __init__(self): -- Método construtor
        Animal.__init__(self) -- Dentro do método construtor é chamado e inicializado o método construtor da classe animal
        print("Objeto Cachorro criado")

    def Identif(self): -- Método pessoal da classe cachorro
        print("Cachorro")

    def latir(self): -- Método pessoal da classe cachorro
        print("Au Au!")

-- Objeto rex instânciado da classe Cachorro, pode utilizar de seus métodos internos pessoais, e também os métodos da classe Animal
rex = Cachorro()
rex.Identif()
rex.latir()
rex.comer()

## Python possui diversos métodos especiais com a sintaxe de (__) no início e fim e o nome do método ao meio.
__init__ -- Método de inicialização ao criar uma classe

class Livro(): -- Classe livro criada, contendo o método especial __init__ / __str__ e __len__
    def __init__(self, titulo, autor, paginas): -- Método especial de inicialização da classe
        print ("Livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
                
    def __str__(self): -- Método Especial __str__, é chamado internamento pelo Python, quando é utilizado o método (print)
        return "Título: %s , autor: %s, páginas: %s " \
    %(self.titulo, self.autor, self.paginas)

    def __len__(self): -- Método Especial __len__, é utilizado para retornar o tamanho da string
        return self.paginas
    
    def len(self):
        return print("Páginas do livro com método comum: ", self.paginas)


livro1 = Livro("Os Lusíadas", "Luis de Camões", 8816) -- Instânciado um objeto da classe livro e chamado alguns métodos
print(livro1)
str(livro1)
len(livro1)
livro1.len()
del livro1.paginas -- Deleta o valor definido para o atributo páginas


















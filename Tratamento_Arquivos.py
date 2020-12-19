# Leitura de Arquivos Python
# É importante frisar que ao abrir o Jupyter Notebook, seja aberto pelo no diretório que irá utilizar na leitura e gravação dos arquivos

# Função para abrir arquivo e salva em um variável, é passado o caminho do diretório, apenas r - de read / w - writer
# Observação - uma vez aperto para r ou w, só pode ser usado suas respectivas funções.
var01 = open("arquivos/arquivo01.txt", "r")

# Função para Ler e imprimir os valores da variável
print(var01.read() )

# Função que retorna os primeiros caracteres baseado no tamanho do parametro passado
print(var01.read(10) )

# Função para contar o número de caracteres da variável
print(var01.tell() )

# Função que retorna o conjunto de valores de uma posição A até posição B
print(var01.seeek(0, 10) )

# Gravando Arquivos

# Realizando abertura do arquivo em modo w - writer
# Não pode ser usados funções de r -read, visto que foi aberto como w- writer
var02 = open("arquivos/arquivo01.txt", "w")

# Gravando dados no Arquivo
var02.write("Texto sera adicionado, sobrescrevendo o conteudo existente no arquivo")
var02.close() # Importante fechar a conexão com o arquivo

# Realizando a abertuda em modo r - read e logo imprimindo seu conteúdo
var02 = open("arquivos/arquivo01.txt", "r")
print(var02.read() )

# Abrindo arquivo em modo WRITER que adiciona e não sobrepõe o conteúdo existente
var03 = open("arquivos/arquivo01.txt", "a")
var03.write("Conteúdo será adicionado")
var03.close()

var03 = open("arquivos/arquivo01.txt", "r")
print(var03.read() )

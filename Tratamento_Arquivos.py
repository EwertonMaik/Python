--Leitura de Arquivos Python
--É importante frisar que ao abrir o Jupyter Notebook, seja aberto pelo no diretório que irá utilizar na leitura e gravação dos arquivos

# Função para abrir arquivo e salva em um variável, é passado o caminho do diretório, apenas r - de read
var01 = open("arquivos/arquivo01.txt", "r")

# Função para Ler e imprimir os valores da variável
print(var01.read() )

# Função que retorna os primeiros caracteres baseado no tamanho do parametro passado
print(var01.read(10) )

# Função para contar o número de caracteres da variável
print(var01.tell() )

# Função que retorna o conjunto de valores de uma posição A até posição B
print(var01.seeek(0, 10) )


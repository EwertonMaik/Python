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

# Exemplo - Usando um INPUT para passar o nome do Arquivos
nomeArquivo = input("Digite o nome do arquivo: ")
nomeArquivo = nomeArquivo + ".txt" #Concateno o nome do arquivo com o texto - .txt para formar o nome e extensão do arquivo
var04 = open(nomeArquivo, "w") # Realizando abertura em modo w - writer
var04.write("Incluíndo texto que arquivo criado")
var04.close()

var04 = open(nomeArquivo, "r") # Realizando aberturda em modo r - read
print(var04.read() )
var04.close()

# Criando Arquivos pelo JUPYTER NOTEBOOK - Essse comando funciona somente no JUPYTER NOTEBOOK - É um comando interno da ferramenta
%%writefile arquivos/teste.txt
ESTE TEXTO SERÁ ADICIONADO AO ARQUIVO CRIADO

var05 = open("arquivos/teste.txt", "r") # Realizando a abertura do Arquivo
print(var05.read() ) # Imprime o conteúdo da variável
var05.seek(0) # Retorna o posicionamento de leitura do arquvo para posição inicial
var05.readlines() # Realiza a leitura por linhas

# Lendo e imprimindo o arquivo - utilizando um FOR
for line in  open("arquivos/teste.txt"):
  print(line)

# Abrindo e Lendo um arquivo CSV - modo - r - read
var06 = open('arquivos/salarios.csv', 'r') # Realizado abertura em modo
var07 = var06.read() # Variável recebe a leitura do arquivo
linhas = var07.split("\n") # Variável recebe o valor do arquivo split - cortado em pedaços pela quebra de linha
full_data = []

# Percorre todos linhas e adiciona - append no vetor [] - full_data
for linha in linhas:
  split_linha = linha.split(",") # Realiza o corte na ocorrencia de uma virgula
  full_data.append(split_linha)  # Adiciona a linha no vetor
  first_row = full_data[0]

print(full_data) # Imprime todo vetor

# Usando um for para contar quantas linhas o arquivo tem
count = 0
for row in full_data:
  count += 1
print(count) # Imprime a variável que foi incrementada a partir de cada linha percorrida pela for

# Usando um for para contar quantas colunas tem a tabela
count = 0
for coluna in first_row:
  count = count + 1
print(count) # Imprime a variável que foi incrementada a partir de cada coluna percorrida pela for








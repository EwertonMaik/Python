# CSV - Character Separated Values
# Python possui o pacote (import csv) para manipulação desse tipo de arquivo de dados

# Realizando importação do pacote de manipulação CSV
import csv

# Utilizando expressão WITH para abrir arquivo em modo w - writer
with open('arquivos/numeros.csv', 'w') as arquivo:
  writer = csv.writer(arquivo) # Variável writer recebe abertura para escritar no arquivo
  # Usando a função writerow para escrever linhas no arquivo
  writer.writerrow( ('JANEIRO', 'FEVEREIRO', 'MARÇO') )
  writer.writerrow( ('CARRO', 'ONIBUS', 'AVIAO') )
  writer.writerrow( (100, 200, 300) )

# Abrindo o arquivo em modo read -r e utilizando um for para percorrer e imprimir
with open('arquivos/numeros.csv', 'r') as arquivo:
leitor = csv.reader(arquivo) # Variável leitor recebe abertura para leitura do arquivo
for x in leitor:
  print('Nº Colunas : ', len(x) )
  print(x)

# Código alternativo para eventuais problemas com linhas em branco no arquivo
with open('arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:

# Transformando os dados do arquivo CSV em uma Lista no Python
with open('arquivos/numeros.csv','r') as arquivo: # Aberto modo r -read - leitura
  leitor = csv.reader(arquivo) # Váriavel recebe conteúdo da leitura do csv
  dados = list(leitor) # Função que os dados em uma LISTA
  
print(dados) # Imprimindo a LISTA

# Segunda forma de imprimir em uma Lista - Usando FOR e a variável dados usada no bloco anterior
# É usado Slice para iniciar a leitura e respectivamente a impressão a partir da posição 1
for linha in dados[1:]:
  print(linha)


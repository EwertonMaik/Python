# Criando uma váriavel texto e utilizando de concatenação e quebra de linha para adicionar valor

texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"  # Concatenação usando operador (+)
texto += "E claro, em Big Data."  # Concatenador usando o operador (+=)

# Importando o pacote que possue funções de acesso ao Sistema Operacional
import os

# Usando Função para abrir arquivo - Caso ele não exista, será criado
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')

# Utilizando um For para percorrer todo conteúdo da String, fatiando a por padrão pelo espaço () - função split, e salvando no objeto arquivo
for palavra in texto.split():
    arquivo.write(palavra+' ')

arquivo.close() # Fechado conexão com arquivo

# Realizando a abertuda do arquivo em modo r - reader e imprimindo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

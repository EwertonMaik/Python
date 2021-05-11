## Desenvolvendo um modelo de Visualização com Graficos com a Bibilioteca Matplotlib e SQLite

## Comando para Instalar pacote e verão do Matplotlib
!pip install -q -U matplotlib==3.2.1

## Importando pacote Matplotlib e consultando a sua versão
import matplotlib as mat
mat.__version__

import sqlite3
import random
import datetime
import matplotlib.pyplot as plt %matplotlib notebook ## Criar o grafico dentro do jupter notebook

## Criando uma conexão com o arquivo do Banco Dados, caso não exista é criado
conn sqlite3.connect('dsa.db')

## Criando o objeto de conexão Cursor
cur = conn.cursor()

# Criando uma função para Ler os Dados do Banco de Dados e Apresentar em Grafico da Biblioteca Matplotlib
def dados_grafico():
    cur.execute("SELECT id, valor FROM produtos") ## Objeto de conexão Cursor para realizaar a consulta aos Dados
    ids = []        ## Criando uma Lista de IDS
    valores = []    ## Criando uma Lista de Valores
    dados = cur.fetchall()  ## Variavel recebendo todos os Dados consultados através do Função FETCHALL do Cursor
    for linha in dados:     ## Utilizando a estrutura FOR para iterar e percorrer os Dados e Salvar nas Listas
        ids.append(linha[0])    ## Salva todos os valores da Posição - Coluna 1 - ID
        valores.append(linha[1]) ## Salva todos os valores da Posição - Coluna 2 - VALORES
        
    plt.bar(ids, valores)  ## Instância do plt do MatplotLib executando a função bar, que cria um grafico de barras que tem o eixo X e Y, 
    plt.show() ## Chamando a Função para exibir o Grafico em Tela


# Chamando a Função que Executa a operação anterior desenvolvida
dados_grafico()

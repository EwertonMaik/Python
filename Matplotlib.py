## Matplotlib

## Matplotlib é a blibioteca Python mais popular para visualização de dados e geração de gráficos.
## Matplotlib permite que você crie facilmente gráficos, histogramas e outras visualizações profissionais.
## Quando usado no Jupyter Notebook, Matplotlib tem recursos interativos com zoom e visão panorâmica.
## Ele possui suporte em todos os sistemas operacionais e também pode exportar gráficos para vetor comum e outros formatos como:
## pdf, svg, jpg, png, bmp, gif, etc.
## Para simples plotagem o método pyplot fornece uma interface parecida com o Matlab, especialmente quando combinado com Jupyter Notebook.
## o usuário tem total controle de estilos de linhas, propriedades de fonte, atributos, etc.. através de uma interface orientada a objetos
## ou através de um conjunto de funções familiares aos usuários do Matlab.
## A dica mais importante quando se trata de plotagem é: menos é mais
## O objetivo final da visualização de dados, é apresentar um resultado, um insight. E você não precisa de um gráfico poluído para isso.
## Acredite, visualização de dados é quase uma arte!

## Matplotlib - Construindo Plots - Construção de Visualizações / Gráficos
## Site Oficial - https://matplotlib.org/index.html

## Para atualizar o Matplotlib abra o prompt de comando ou terminal e digite:
pip install matplotlib -U

# O matplotlib.pyplot é uma coleção de funções e estilos que fazem com que o Matplotlib funcione como o Matlab.
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline ## Permite que a visualização do Gráfico fice imbutida dentro do Jupyter Notebook, e não em uma nova janela.

mpl.__version__

## O Método plot() define os eixos do gráfico
plt.plot([1, 3, 5], [2, 5, 7] )
plt.show()

x = [1, 4, 5]
y = [3, 7, 2]

plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show()

x2 = [1, 2, 3]
y2 = [11, 12, 15]

plt.plot(x2, y2, label = 'Primeira Linha')
plt.legend()
plt.show()

## Gráficos de Barras
x = [2,4,6,8,10]
y = [6,7,8,2,4]

## Funções do Pacote NumPy

# A função arange cria um vetor contendo uma progressão aritmética a partir de um intervalo - start, stop, step
vetor2 = np.arange(0., 4.5, .5)

print(vetor2)

# Verificando o tipo do objeto
type(vetor2)

# Formato do array
np.shape(vetor2)

print(vetor2.dtype)

x = np.arange(1, 10, 0.25)
print(x)

print(np.zeros(10) )

# Retorna 1 nas posições em diagonal e 0 no restante
z = np.eye(3)

z

# Os valores passados como parâmetro, formam uma diagonal
d = np.diag(np.array([1, 2, 3, 4]) )
d

# array de números complexos
c = np.array([1 + 2j, 3+4j, 5+6*1j])
c

# Array de valores booleanos
b = np.array([True, False, False, True])
b

# Array de Strings
s = np.array(['Python', 'R', 'Julia'])
s

# O método linspace (linearly spaced vector) retorna um número de valores igualmente distribuídos no intervalo especificado
np.linspace(0, 10)

print(np.linspace(0, 10, 15) )

print(np.logspace(0, 5, 10) )

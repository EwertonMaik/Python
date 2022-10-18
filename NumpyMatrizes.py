## Matrizes em NumPy

# Criando uma Matriz
matriz = np.array([ [1,2,3], [4,5,6] ])

print(matriz)

print(matriz.shape)

# Criando uma matriz 2 x 3 apenas com números "1"
matriz1 = np.ones((2, 3))

print(matriz1)

# Criando uma matriz a partir de uma lista de listas
lista = [ [13,81,22], [0,34,59], [21,48,94] ]

# A função matriz cria uma matriz a partir de uma sequência
matriz2 = np.matrix[lista]

matriz2

type(matriz2)

# Formato da Matriz
np.shape[matriz2]

matriz2.size

print(matriz2.dtype)

matriz2.itemsize

matriz2.nbytes

print(matriz2[2,1] )

# Alterando um elemento da matriz
matriz2[1,0] = 100

matriz2

x = np.array([1, 2]) # NumPy decide o tipo de dados
y = np.array([1.0, 2.0]) # NumPy decide o tipo de dados
z = np.array([1, 2], dtype = np.float64) # Formaçõs um tipo de dados em particular

print(x.dtype, y.dtype, z.dtype)

matriz3 = np.array( [24, 76], [35, 89], dtype = float)

matriz3

matriz3.itemsize

matriz3.nbytes

matriz3.ndim

matriz3[1, 1]

matriz3[1, 1] = 100

matriz3

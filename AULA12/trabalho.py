# Criando uma matriz tridimensional 3x3x3 preenchida com zeros
matriz_tridimensional = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]

# Modificando alguns elementos da matriz
matriz_tridimensional[0][1][2] = 5
matriz_tridimensional[2][2][1] = 8

# Acessando elementos da matriz
elemento = matriz_tridimensional[0][1][2]
print("Elemento na posição (0, 1, 2):", elemento)  # Saída: 5

# Imprimindo a matriz tridimensional
print("Matriz tridimensional:")
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(matriz_tridimensional[i][j][k], end=" ")
        print()
    print()

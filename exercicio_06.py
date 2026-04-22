"""Crie uma matriz 5x5 onde 
m[i][j] = (i+1) * (j+1) usando compreensão aninhada."""

matriz = [[(i+1) * (j + 1 ) for j in range(5)] for i in range(5)] 

for linha in matriz:
    print(linha)
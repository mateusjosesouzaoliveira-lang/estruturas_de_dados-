"""Dada uma lista de números [-3, -2, -1, 0, 1, 2, 3, 4, 5], 
crie outra lista com apenas 
os positivos ao quadrado usando compreensão."""

numeros = [-3, -2, -1, 0, 1, 2, 3, 4, 5]

positivos_quadrados = [ x**2 for x in numeros if x > 0]

print(positivos_quadrados)
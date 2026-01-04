# Desafio 19: Crie dois conjuntos de números e encontre a união, interseção e diferença entre eles.

# Criando os conjuntos
conjunto_1 = {1, 6, 9, 0, 2, 3, 7, 4, 8}

conjunto_2 = {1, 11, 13, 2, 5, 4, 18, 6, 19}

# Imprimindo os conjuntos separados
print(f"\nConjunto 1: {conjunto_1}")
print(f"\nConjunto 2: {conjunto_2}")

# Definindo a variável de união dos conjuntos
uniao_conjuntos = conjunto_1.union(conjunto_2)

# Imprimindo a união dos conjuntos
print(f"\n\tUnião dos conjuntos: {uniao_conjuntos}")

# Definindo a interseção dos conjuntos
intersecao = conjunto_1.intersection(conjunto_2)

# Imprimindo a interseção dos conjuntos
print(f"\n\tInterseção dos conjuntos: {intersecao}")

# Definindo a diferença entre os dois conjuntos
diferenca = conjunto_1.difference(conjunto_2)

# Imprimindo a diferença dos conjuntos
print(f"\n\tDiferença dos conjuntos: {diferenca}")

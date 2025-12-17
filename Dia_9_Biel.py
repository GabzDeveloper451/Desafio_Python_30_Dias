# Desafio 9: Use um laço for para iterar sobre a lista de frutas e imprimir cada item com sua posição.

print("\n--- Desafio 9 ---\n")

# Definindo a lista:
lista_de_frutas = ["Banana", "Maçã", "Laranja", "Limão", "Melancia"]

# Ordenando a lista alfabeticamente
lista_ordenada = sorted(lista_de_frutas)

# Imprimindo a lista enumerada
for i, fruta in enumerate(lista_ordenada, +1):
    print(i, fruta, sep=" - ")

# Muito fácil ;-;'

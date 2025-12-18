# Desafio 10: Use um laço while para contar de 1 a 10 e imprimir apenas os números pares.

print("\n--- Desafio 10 ---\n")

# Mensagem de entrada
print("\tContando de 1 a 10: \n")

# Criando o contador
contador = 0

# Criando o laço
while True:
    contador += 1

    # Imprimindo o contador
    print(contador)

    # Fazendo com que se o contador for 10, o programa acabe
    if contador == 10:

        # Resetando o contador
        contador = 0
        break

print("\n\tNúmeros pares presentes entre 1 e 10: \n")

while True:
    contador += 1

    # Salvando os números pares do contador
    if contador % 2 == 0:
        # Imprimindo os números pares do contador
        print(contador)

    else:
        continue

    if contador == 10:
        break

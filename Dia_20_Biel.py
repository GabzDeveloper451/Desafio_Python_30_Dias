# Desafio 20: Crie um programa que peça um número, mas use try/except para lidar se o usuário digitar texto.

# Pedindo ao usuário um número
while True:
    num = input("\nDigite um numero: ")

    # Verificando se o usuário mandou um número
    try:
        num = int(num)
        break
    except ValueError:

        print("\n\vERRO: Digite um número inteiro")

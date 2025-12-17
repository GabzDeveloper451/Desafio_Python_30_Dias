# Desafio 4: Peça ao usuário dois números e imprima a soma, subtração, multiplicação e divisão deles.

print("\n--- desafio 4 ---\n")

""" Mensagem de início """

import os
print(
    "\n\tOlá, neste programa, calcularei a soma, a subtração,"
    " a multiplicação e a divisão, de dois números à sua escolha."
)

# Definindo os números
while True:
    x = input("\nDigite o primeiro número: ")
    if len(x) == 0:
        print("Digite ao menos um número.")
        continue

    try:
        float_x = float(x)
    except:
        print("Digite um número válido.")
        continue

    y = input("\nDigite o segundo número: ")

    if len(y) == 0:
        print("Digite ao menos um número.")
        continue

    try:
        float_y = float(y)
    except:
        print("Digite um número válido.")
        continue



# Definindo o valor de cada variável de cálculo

    def soma(x, y):
        return x + y

    def subtracao(x, y):
        return x - y

    def multiplicacao(x, y):
        return x * y

    def divisao(x, y):
        return x / y

# Salvando se o usuário quer dividir, multiplicar, somar, ou subtrair
    os.system("clear")
    while True:
        operadores_permitidos = '+-/*'
        operador = input("\nQual operador você deseja escolher? +-/*: ")

        if operador not in operadores_permitidos:
            print("Digite um operador válido.")
            continue
        elif operador == '':
            print("\nVocê não digitou nenhum operador.")
        else:
            break

    # Realizando a conta:

    if operador == '+':
        os.system("clear")
        print("\nRealizando a conta... \n")
        print(f"{float_x:.0f} + {float_y:.0f} = {soma(float_x, float_y):.0f}")

    elif operador == '-':
        os.system("clear")
        print("\nRealizando a conta... \n")
        print(f"{float_x:.0f} - {float_y:.0f} = {subtracao(float_x, float_y):.0f}")

    elif operador == '/':
        os.system("clear")
        print("\nRealzando a conta... \n")
        print(f"{float_x:.0f} * {float_y:.0f} = {subtracao(float_x, float_y):.0f}").strip()

    else:
        os.system("clear")
        print("\nRealizando a conta... \n")
        print(f"{float_x:.0f} * {float_y:.0f} = {multiplicacao(float_x, float_y):.0f}")

    sair = input("\nDeseja sair? [S/N]: ").upper()

    if sair == "S".upper():
        print("\nAté mais!")
        break

    else:
        continue

# Desafio 3: Calcule o Índice de Massa Corporal (IMC) usando entradas de peso e altura.

print("\n--- Desafio 3 ---\n")

# Imprimindo uma mensagem de entrada
print("Olá, com esse programa, calcularei o seu Índice de Massa Corporal (IMC) para isso: ")

# Salvando o peso do usuário

# Garantindo que o usuário digite apenas o valor numérico de seu peso
while True:
    peso = input("\nDigite quanto você pesa ex(69.2): ")
    try:
        peso = float(peso)
        if peso <= 0:
            print("Por favor, digite um valor maior que zero.")
            continue
        break
    except ValueError:
        print("Por favor, digite apenas o valor numérico de seu peso.")

# Salvando a altura do usuário
while True:
    altura = input("\nDigite a sua altura ex(1.75): ")
    try:
       altura = float(altura)
       if altura <= 0:
           print("Por favor, digite um valor maior que zero.")
           continue
       break
    except ValueError:
        print("Por favor, digite apenas o valor numérico de sua altura.")
# Salvando o cálculo do IMC do usuário
imc = peso / (altura ** 2)

# Imprimino o IMC do usuário
print(
    "\n Calculando..."
    f"\n O seu Índice de Massa corporal é de {imc:.2f} kg/m²"
)

# Definindo o nome
nome = input("\nOlá! Digite o seu nome: ")

# Definindo a idade
while True:
    idade = input("\nDigite a sua idade: ")
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print("\n\tERRO: DIGITE UM NÚMERO VÁLIDO.")
        continue

# Definindo a altura
while True:
    altura = input("\nDigite a sua altura (ex: 1.75): ")

    # Verificação de formato: precisa ter ponto e duas casas decimais
    if "." in altura:
        parte_inteira, parte_decimal = altura.split(".", 2)

        # Verifica se a parte decimal tem 2 números e se tudo é numérico
        if parte_decimal.isdigit() and len(parte_decimal) == 2 and parte_inteira.replace("-", "").isdigit():
            altura = float(altura)
            break

    print("ERRO: DIGITE A ALTURA NO FORMATO NUMÉRICO COM DUAS CASAS DECIMAIS. EX: 1.75")

print(f"\nSeu nome é {nome}, você tem {idade} anos de idade e {altura}m de altura.")

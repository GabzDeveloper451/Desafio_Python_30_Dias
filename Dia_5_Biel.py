# Desafio 5: Crie um programa que verifique se um número é par ou ímpar.

# Imprimindo mensagem de entrada

print("\nOlá, neste programa, você digitará um número, e eu irei verificar se é ímpar ou par.")


while True:
    # Tentando converter o valor enviado pelo usuário para inteiro
    try:
        num = int(input("\nDigite um número: "))

    # Caso der errado, ele está enviando uma str, que não é possível converter para um inteiro, então:
    except ValueError:
        print("\nDigite um valor númerico.")
        continue

    # Verificando se o número é ímpar ou par:

    if num % 2 == 0:
        print(f"O número {num} é par")

    else:
        print(f"O número {num} é ímpar")

    sair = input("\n\tDeseja sair? [S/N] ").upper()

    if sair == "S":
        print("\nSaindo, até mais!")
        break

    else:
        continue
    

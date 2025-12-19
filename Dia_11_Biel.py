# Desafio 11: Escreva uma função que receba dois números como argumentos e retorne o maior deles.

# Mensagens de entrada:
print("\n--- Desafio 11 ---\n")

print("\tNesse programa você digitará dois números e eu lhe mostrarei qual é o maior entre os dois.")
# Definindo a função:
def maior_num(x, y):
    if x > y:
        return x
    else:
        return y

while True:
    # Definindo o primeiro e o segundo número
    num_1 = input("\nDigite o primeiro número: ")
    num_2 = input("\nDigite o segundo número: ")
    try:
        float(num_1)
        float(num_2)
    
    except:
        print("\n\vERRO: Você não digitou um número.")
        continue

    print(f"\n\tO maior número entre {num_1} e {num_2} é o número: {maior_num(num_1,num_2)}")


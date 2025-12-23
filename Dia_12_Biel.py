# Desafio 12: Crie uma função que receba uma lista de números e calcule a média.
# Mensagem de entrada
print("\n--- Desafio 12 ---\n")

print(
    "Nesse desafio, criarei um programa, onde você poderá adicionar números em uma lista,"
    "quando terminar de digitar todos os números, calcularei a média entre eles.\n"
)

lista_num = []
operadores_permitidos = 'arm'

# Salvando a resposta do usuário
while True:
    operador = input("\nO que você deseja fazer? [a]dicionar - [r]emover - [m]édia: ").strip().lower()

    if not operador:
        print("\n\vERRO: Digite um operador válido.")
        continue

    if operador not in operadores_permitidos:
        print("\n\vERRO: Digite um operador válido.")
        continue

    if operador == 'a':
        while True:
            try:
                num = float(input("\n\tDigite o número que você deseja adicionar: "))
                lista_num.append(num)
                break

            except:
                print("\n\vERRO: Digite um valor numérico.")
                continue

    if operador == 'r':
        if len(lista_num) == 0:
            print("\n\vERRO: Não há números na sua lista. ")
            continue
        else:
            while True:
                try:
                    remover = float(input("\n\tDigite o número que você deseja remover: "))

                    if remover not in lista_num:
                        print("\n\vERRO: O número que você deseja remover não existe na lista. ")
                        continue
                    else:
                        lista_num.remove(remover)
                        break

                except:
                    print("\n\vERRO: Digite um valor númerico.")
                    continue

    if operador == 'm':
        if len(lista_num) == 0:
            print("\n\vERRO: Não há números na lista.")
            continue

        else:
            def media_num(lista_num):
                return sum(lista_num) / len(lista_num)

            print(f"\n\tCalculando...\n A média da sua lista é: {media_num(lista_num):.1f}")

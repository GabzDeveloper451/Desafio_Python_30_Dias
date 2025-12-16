# Desafio 8: Adicione uma fruta, remova outra e ordene a lista em ordem alfabética.

lista_frutas = []
operador_valido = 'alrs'

while True:
    entrada = input("\nO que você deseja fazer? [a]dicionar - [l]istar - [r]emover - [s]air: ").lower().strip()

    if entrada not in operador_valido:
        print("\n\vERRO: Digite um operador válido.")
        continue

    if not entrada:
        print("\n\vERRO: Digite um operador válido.")
        continue

    while entrada == "a":
        fruta = input("\n\tDigite a fruta que você deseja adicionar: ").lower()

        if len(fruta) == 0:
            print("\n\vERRO: Digite ao menos uma fruta.")
            continue

        if len(fruta) < 3:
            print("\n\vERRO: Uma fruta tem ao menos 3 letras.")
            continue

        if fruta in lista_frutas:
            print("\n\vERRO: Essa fruta já foi adicionada na sua lista. ")
            continue

        else:
            lista_frutas.append(fruta)
            break

    while entrada == "l":

        if len(lista_frutas) == 0:
            print("\n\vERRO: Não há nenhuma fruta na sua lista.")
            break

        else:
            print("\nLista de frutas: \n")

            listar = sorted(lista_frutas)
            for i, fruta in enumerate(listar, start=1):
                print(i, fruta, sep=' - ')
            break

    while entrada == "r":

        if len(lista_frutas) == 0:
            print("\n\vERRO: Não há frutas para remover.")
            break

        else:
            print("\nLista: \n")
            for i, fruta in enumerate(lista_frutas, start=1):
                print(i, fruta, sep=' - ')

            remover_fruta = input("\n\tDigite a fruta que você deseja remover: ").lower()
            if remover_fruta not in lista_frutas:
                print("\n\vERRO: A fruta que você tentou remover, não está na sua lista.")
                continue

            else:
                lista_frutas.remove(remover_fruta)
                break

    if entrada == "s":
        print("\nSaindo... Até mais!")
        break

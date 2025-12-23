# Desafio 13: Entenda e demonstre a diferença entre variáveis locais e globais em uma função.

print("\n--- Desafio 13 ---\n")
# Variável Global
status = "Online"


def atualizar_sistema():
    # Variável Local (tem o mesmo nome, mas é um objeto diferente)
    status = "Manutenção"
    versao_local = "2.0.5"  # Existe apenas aqui dentro

    print(f"[DENTRO DA FUNÇÃO]")
    print(f"Status Local: {status}")
    print(f"Versão Local: {versao_local}")


# Execução do programa
atualizar_sistema()

print(f"\n[FORA DA FUNÇÃO]")
print(f"Status Global: {status}")

# O comando abaixo causaria um NameError:
# print(versao_local)


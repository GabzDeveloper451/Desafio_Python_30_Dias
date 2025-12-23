# Desafio 14: Importe o módulo math e calcule a área de um círculo com base no raio fornecido pelo usuário.
import math

print("\n--- Desafio 14 ---\n")
print("Nesse programa você digitará o valor do raio de um círculo, e eu direi a área dele.")

# Entrada do raio
while True:
    try:
        r = float(input("\n\tDigite o valor do raio: "))
        break
    except ValueError:
        print("\n\tERRO: Digite um valor numérico.")

# Entrada da unidade de medida (somente letras)
while True:
    unidade_medida = input("\n\tDigite a unidade de medida (ex: cm, m): ").strip()
    if unidade_medida.isalpha():
        break
    else:
        print("\n\tERRO: Digite apenas letras para a unidade de medida.")

# Cálculo da área
area = math.pi * (r ** 2)

# Saída
print(
    f"\n\tA área do círculo cujo raio é {r:.1f}{unidade_medida} "
    f"é de {area:.3f}{unidade_medida}²"
)

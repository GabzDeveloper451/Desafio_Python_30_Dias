# Desafio 15: Peça uma frase ao usuário, conte o número de vogais e substitua todos os espaços por sublinhados.

# Mensagem de entrada:
print("\n--- Desafio 15 ---\n")

# Salvando a frase
frase = input("\n\tDigite uma frase: ").strip().lower()

vogais = 'aeiou'
qtd_vogais = 0

# Verificando as vogais na frase
for letra in frase:
    if letra in vogais.lower():
        qtd_vogais += 1

# Trocando os espaços da frase por sublinhados
frase_modificada = frase.replace(" ","_")

print(f"Esta frase contém: {qtd_vogais} vogais")
print(f"Frase modificada: {frase_modificada}")

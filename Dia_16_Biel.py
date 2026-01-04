# Criando a tupla de coordenadas
coordenadas = (10, 4)

# Desempacotando os valores
longitude, latitude = coordenadas

print(f"Coordenadas originais: Longitude {longitude}, Latitude {latitude}")

# Demonstração da imutabilidade usando um bloco try-except
try:
    coordenadas[0] = 50
except TypeError as e:
    print(f"Erro ao tentar alterar: {e}")

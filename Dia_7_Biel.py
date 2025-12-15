# Desafio 7: Crie uma lista de 5 frutas e imprima cada uma delas.

# Mensagem de entrada:
print("Olá, neste programa, você digitará 7 frutas, e eu farei uma lista com cada uma delas.")

# Criando um dicionário de frutas para garantir que o usuário digite uma fruta:
dict_fruits = {
    'abacate': None,
    'abacaxi': None,
    'abiu': None,
    'abricó': None,
    'abrunho': None,
    'açaí': None,
    'acerola': None,
    'akee': None,
    'alfarroba': None,
    'ameixa': None,
    'amêndoa': None,
    'amora': None,
    'ananás': None,
    'anona': None,
    'araçá': None,
    'arando': None,
    'araticum': None,
    'ata': None,
    'atemoia': None,
    'avelã': None,
    'babaco': None,
    'babaçu': None,
    'bacaba': None,
    'bacuri': None,
    'bacupari': None,
    'banana': None,
    'baru': None,
    'bergamota': None,
    'biribá': None,
    'buriti': None,
    'butiá': None,
    'cabeludinha': None,
    'cacau': None,
    'cagaita': None,
    'caimito': None,
    'cajá': None,
    'caju': None,
    'calabaça': None,
    'calabura': None,
    'calamondin': None,
    'cambucá': None,
    'cambuci': None,
    'camu-camu': None,
    'caqui': None,
    'carambola': None,
    'carnaúba': None,
    'castanha': None,
    'castanha-do-pará': None,
    'cereja': None,
    'ciriguela': None,
    'ciruela': None,
    'coco': None,
    'cranberry': None,
    'cupuaçu': None,
    'damasco': None,
    'dekopon': None,
    'dendê': None,
    'dióspiro': None,
    'dovyalis': None,
    'durião': None,
    'embaúba': None,
    'embaubarana': None,
    'engkala': None,
    'escropari': None,
    'esfregadinha': None,
    'esporão-de-galo': None,
    'figo': None,
    'framboesa': None,
    'fruta-do-conde': None,
    'fruta-pão': None,
    'feijoa': None,
    'figo-da-índia': None,
    'fruta-de-cedro': None,
    'fruta-de-lobo': None,
    'fruta-do-milagre': None,
    'fruta-de-tatu': None,
    'gabiroba': None,
    'glicosmis': None,
    'goiaba': None,
    'granadilla': None,
    'gravatá': None,
    'graviola': None,
    'groselha': None,
    'grumixama': None,
    'guabiju': None,
    'guabiroba': None,
    'guaraná': None,
    'hawthorn': None,
    'heisteria': None,
    'hilocéreo': None,
    'ibacurupari': None,
    'ilama': None,
    'imbe': None,
    'imbu': None,
    'inajá': None,
    'ingá': None,
    'inharé': None,
    'jabuticaba': None,
    'jaca': None,
    'jambo': None,
    'jambolão': None,
    'jamelão': None,
    'jaracatiá': None,
    'jatobá': None,
    'jenipapo': None,
    'jerivá': None,
    'juá': None,
    'jujuba': None,
    'kiwi': None,
    'kumquat': None,
    'kinkan': None,
    'kino': None,
    'kiwano': None,
    'kabosu': None,
    'karité': None,
    'korlan': None,
    'laranja': None,
    'limão': None,
    'lima': None,
    'lichia': None,
    'longan': None,
    'lucuma': None,
    'lacucha': None,
    'lulo': None,
    'lobeira': None,
    'langsat': None,
    'laranja-de-pacu': None,
    'mabolo': None,
    'maçã': None,
    'macadâmia': None,
    'macaúba': None,
    'mamão': None,
    'mamey': None,
    'mamoncillo': None,
    'maná-cubiu': None,
    'manga': None,
    'mangaba': None,
    'mangostão': None,
    'maracujá': None,
    'marango': None,
    'marmelo': None,
    'marolo': None,
    'marula': None,
    'massala': None,
    'melancia': None,
    'melão': None,
    'meloa': None,
    'mexerica': None,
    'mirtilo': None,
    'morango': None,
    'murici': None,
    'naranjilla': None,
    'nectarina': None,
    'nêspera': None,
    'noni': None,
    'noz': None,
    'noz-pecã': None,
    'noz-macadâmia': None,
    'oiti': None,
    'oxicoco': None,
    'orangelo': None,
    'pera': None,
    'pêssego': None,
    'pitanga': None,
    'pinha': None,
    'pitaia': None,
    'pitomba': None,
    'pitangatuba': None,
    'pindaíba': None,
    'pequi': None,
    'pequiá': None,
    'physalis': None,
    'pulasan': None,
    'pomelo': None,
    'pupunha': None,
    'puçá': None,
    'patauá': None,
    'pajurá': None,
    'pixirica': None,
    'pistache': None,
    'quina': None,
    'quiui': None,
    'quixabeira': None,
    'romã': None,
    'rambai': None,
    'rambutão': None,
    'rukam': None,
    'saguaraji': None,
    'salak': None,
    'santol': None,
    'sapota': None,
    'sapoti': None,
    'sapucaia': None,
    'saputá': None,
    'seriguela': None,
    'sorvinha': None,
    'tangerina': None,
    'tamarindo': None,
    'tâmara': None,
    'toranja': None,
    'tucumã': None,
    'taiuva': None,
    'tapiá': None,
    'tarumã': None,
    'tangor': None,
    'tucujá': None,
    'uva': None,
    'umbu': None,
    'uvaia': None,
    'uchuva': None,
    'umê': None,
    'uxi': None,
    'ucuuba': None,
    'vacínio': None,
    'veludo': None,
    'vergamota': None,
    'veludo-branco': None,
    'wampi': None,
    'xixá': None,
    'yamamomo': None,
    'yuzu': None,
    'zimbro': None
}

# Criando a lista de frutas:
lista_frutas = []

# Definindo as frutas:
# Criando a lista de frutas:
lista_frutas = []

# Definindo as frutas:

# Código original:
while True:
    fruta_1 = input("\n1ª fruta: ").lower()
    if fruta_1 not in dict_fruits:
        print("Essa fruta não existe! Tente novamente")
        continue

    if fruta_1 in lista_frutas:
        print("Essa fruta já foi adicionada na lista de frutas!")
        continue

    if fruta_1 == ' '.strip():
        print("Você não digitou uma fruta.")
        continue

    lista_frutas.append(fruta_1)
    break

while True:
    fruta_2 = input("\n2ª fruta: ").lower()
    if fruta_2 not in dict_fruits:
        print("Essa fruta não existe! Tente novamente")
        continue

    if fruta_2 in lista_frutas:
        print("Essa fruta já foi adicionada na lista de frutas!")
        continue

    if fruta_2 == ' '.strip():
        print("Você não digitou uma fruta.")
        continue

    lista_frutas.append(fruta_2)
    break

while True:
    fruta_3 = input("\n3ª fruta: ").lower()
    if fruta_3 not in dict_fruits:
        print("Essa fruta não existe! Tente novamente")
        continue

    if fruta_3 in lista_frutas:
        print("Essa fruta já foi adicionada na lista de frutas!")
        continue

    if fruta_3 == ' '.strip():
        print("Você não digitou uma fruta.")
        continue

    lista_frutas.append(fruta_3)
    break

while True:
    fruta_4 = input("\n4ª fruta: ").lower()
    if fruta_4 not in dict_fruits:
        print("Essa fruta não existe! Tente novamente")
        continue

    if fruta_4 in lista_frutas:
        print("Essa fruta já foi adicionada na lista de frutas!")
        continue

    if fruta_4 == ' '.strip():
        print("Você não digitou uma fruta.")
        continue

    lista_frutas.append(fruta_4)
    break

while True:
    fruta_5 = input("\n5ª fruta: ").lower()
    if fruta_5 not in dict_fruits:
        print("Essa fruta não existe! Tente novamente!")
        continue

    if fruta_5 in lista_frutas:
        print("Essa fruta já foi adicionada na lista de frutas!")
        continue

    if fruta_5 == ' '.strip():
        print("Você não digitou uma fruta.")
        continue

    lista_frutas.append(fruta_5)
    break

while True:
    fruta_6 = input("\n6ª fruta: ").lower()
    if fruta_6 not in dict_fruits:
        print("Essa fruta não existe! Tente novamente!")
        continue

    if fruta_6 in lista_frutas:
        print("Essa fruta já foi adicionada na lista de frutas!")
        continue

    if fruta_6 == ' '.strip():
        print("Você não digitou uma fruta.")
        continue

    lista_frutas.append(fruta_6)
    break

while True:
    fruta_7 = input("\n7ª fruta: ").lower()
    if fruta_7 not in dict_fruits:
        print("Essa fruta não existe! Tente novamente!")
        continue

    if fruta_7 in lista_frutas:
        print("Essa fruta já foi adicionada na lista de frutas!")
        continue

    if fruta_7 == ' '.strip():
        print("Você não digitou uma fruta.")
        continue

    lista_frutas.append(fruta_7)
    break
# Imprimindo a lista final:
print("\nLista de frutas escolhidas:")

for i, f in enumerate(lista_frutas, start=1):
    print(i, f, sep=' - ')

# Código feito com a ia

# Desafio 7: Crie uma lista de 5 frutas e imprima cada uma delas.

# print("Olá, neste programa, você digitará 5 frutas, e eu farei uma lista com cada uma delas.")
# 
# # Lista de frutas válidas (pode ser expandida se quiser)
# frutas_validas = [
#     'abacaxi', 'banana', 'maçã', 'laranja', 'uva',
#     'morango', 'melancia', 'pera', 'manga', 'kiwi'
# ]
# 
# lista_frutas = []
# 
# # Loop para coletar 5 frutas
# while len(lista_frutas) < 5:
#     fruta = input(f"Digite a fruta {len(lista_frutas)+1}: ").lower()
#     if fruta not in frutas_validas:
#         print("Essa fruta não existe!")
#     elif fruta in lista_frutas:
#         print("Essa fruta já foi adicionada!")
#     else:
#         lista_frutas.append(fruta)
# 
# # Imprimindo frutas enumeradas
# print("\nLista de frutas escolhidas:")
# for i, fruta in enumerate(lista_frutas, start=1):
#     print(f"{i}. {fruta}")

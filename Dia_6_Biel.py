# Implemente um sistema de notas que classifique a pontuação do usuário (A, B, C, D, F).

# Mesagem de entrada:
print("Neste programa, você digitará a sua nota e eu a classificarei da seguinte forma: A, B, C, D, F")

# Iniciando o programa:
while True:
    try:

        # Salvando a nota do usuário:
        nota = float(input("\nDigite a sua nota: "))

        # Arredondando a nota do aluno
        nota_arredondada = round(nota) # --> Parte perguntada para a IA 
        nota = round(nota) 

        # Definindo a classe do aluno:
        if nota == 10:
            classe = "A"
        elif nota >= 8:
            classe = "B"
        elif nota >= 6:
            classe = "C"
        elif nota >= 4:
            classe = "D"
        else:
            classe = "F"

        # Imprimindo a classe e a nota do aluno:
        print(f"\n\tVocê está na classe: {classe} - nota: {nota}")
        break

    except ValueError:
        print("Digite um valor numérico.")

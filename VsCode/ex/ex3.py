#3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o usuário digite -1. Em seguida, exiba a média das notas.

notas = []
nota = float(input("Digite uma nota (ou -1 para sair): "))

while nota != -1:
    notas.append(nota)
    nota = float(input("Digite uma nota (ou -1 para sair): "))

    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print("Média das notas:", media)
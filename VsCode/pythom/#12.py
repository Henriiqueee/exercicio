#12. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores= int(input("Digite o número de eleitores: "))
canditato = 3
candidato1 = 0
candidato2 = 0
candidato3 = 0
for i in range(eleitores):
    voto = int(input("Digite seu voto: "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
        print("Candidato 1: ", candidato1)
    print("Candidato 2: ", candidato2)
    print("Candidato 3: ", candidato3)
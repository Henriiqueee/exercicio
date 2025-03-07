#10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo (5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de votos nulos e brancos. A entrada 0 encerra a votação.

votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total_votos = 0

print("Sistema de Votação")
print("Vote em um candidato (1 a 4), nulo (5) ou branco (6). Digite 0 para encerrar.")

while True:
    voto = int(input("Digite seu voto: "))
    
    if voto == 0:
        break
    elif voto in votos:
        votos[voto] += 1
        total_votos += 1
    else:
        print("Voto inválido. Tente novamente.")

print("\nResultados da Votação:")
for candidato in range(1, 5):
    print(f"Candidato {candidato}: {votos[candidato]} votos")

if total_votos > 0:
    percentual_nulos = (votos[5] / total_votos) * 100
    percentual_brancos = (votos[6] / total_votos) * 100
    
    print(f"\nPorcentagem de votos nulos: {percentual_nulos:.2f}%")
    print(f"Porcentagem de votos brancos: {percentual_brancos:.2f}%")
else:
    print("Nenhum voto foi registrado.")
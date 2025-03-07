#16. Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
# Lista para armazenar as idades
idades = []

# Recebendo a idade de 15 pessoas
for i in range(1, 16):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    idades.append(idade)

# Contando as faixas etárias
faixa_etaria = {
    "Até 15 anos": 0,
    "De 16 a 30 anos": 0,
    "De 31 a 45 anos": 0,
    "De 46 a 60 anos": 0,
    "Acima de 61 anos": 0
}

for idade in idades:
    if idade <= 15:
        faixa_etaria["Até 15 anos"] += 1
    elif 16 <= idade <= 30:
        faixa_etaria["De 16 a 30 anos"] += 1
    elif 31 <= idade <= 45:
        faixa_etaria["De 31 a 45 anos"] += 1
    elif 46 <= idade <= 60:
        faixa_etaria["De 46 a 60 anos"] += 1
    else:
        faixa_etaria["Acima de 61 anos"] += 1

# Total de pessoas
total_pessoas = len(idades)

# Calculando porcentagens
percentual_primeira_faixa = (faixa_etaria["Até 15 anos"] / total_pessoas) * 100 if total_pessoas > 0 else 0
percentual_ultima_faixa = (faixa_etaria["Acima de 61 anos"] / total_pessoas) * 100 if total_pessoas > 0 else 0

# Exibindo os resultados
print("\nQuantidade de pessoas em cada faixa etária:")
for faixa, quantidade in faixa_etaria.items():
    print(f"{faixa}: {quantidade}")

print("\nPercentagens:")
print(f"Percentagem de pessoas até 15 anos: {percentual_primeira_faixa:.2f}%")
print(f"Percentagem de pessoas acima de 61 anos: {percentual_ultima_faixa:.2f}%")
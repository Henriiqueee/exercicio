#1. Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até esse número.

numero = int(input("Digite um número inteiro positivo: "))

while numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

print("Números pares de 2 até", numero, ":")
for i in range(2, numero + 1):
    if i % 2 == 0:
        print(i)
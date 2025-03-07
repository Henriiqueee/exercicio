#9. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

#Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

#Verifica se o número é primo
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

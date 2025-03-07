#13. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

num= int(input("Digite um número: "))
for i in range(num):
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")
#14. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota= int(input("Digite uma nota: "))
for i in range(nota):
    if nota >= 0 and nota <= 10:
        print("Válido")
    else:
        print("Inválido")
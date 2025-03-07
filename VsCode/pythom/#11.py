#11Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
n = int(input("Digite o número de pessoas: "))
soma = 0
for i in range(n):
    idade = int(input("Digite sua idade: "))
    soma += idade
media = soma / n
                
if media <= 25:
    print("Turma jovem")
elif media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
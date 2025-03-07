#7. Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar um número até acertar. (Declare um valor e receba outro)


senha_secreta = 9

senha_secreta = int(input("Digite o numero secreto de (1 a 10): "))
while senha_secreta != 9:
    print("Número incorreta, tente novamente")
    senha_secreta = int(input("Digite o número: "))  
else:
    print("Número correta")

    
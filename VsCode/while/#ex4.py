#4. O usuário deve digitar a senha correta (1234). Enquanto errar, o programa deve pedir novamente.

senha = 1234

senha = int(input("Digite a senha: "))
while senha != 1234:
    print("Senha incorreta, tente novamente")
    senha = int(input("Digite a senha: "))  
else:
    print("Senha correta")
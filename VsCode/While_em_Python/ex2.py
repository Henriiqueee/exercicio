#2. Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha correta definida previamente.

senha_correta = "senha123"
senha_digitada = input("Digite a senha: ")

while senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

    print("Acesso permitido!")
#10. Apenas aceitar números positivos. O programa deve continuar pedindo um número até o usuário digitar um número negativo.


while True:
    num = int(input("Digite um número positivo: "))
    if num < 0:
        print("Número negativo digitado. Encerrando o programa.")
        break
    else:
        print("Número positivo digitado:", num)
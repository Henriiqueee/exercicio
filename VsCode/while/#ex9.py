#9. Contar quantos números pares o usuário digitar. O programa deve contar quantos números pares o usuário inseriu. O usuário para digitando -1

num = int(input("Digite um numero: "))
pares = 0
while num != -1:
    if num % 2 ==0:
        pares += 1
    num = int(input("Digite um numero (ou -1 para sair): "))
print(pares)
#8. Encontrando o maior número inserido pelo usuário. Peça números ao usuário e, ao digitar 0, exiba o maior número inserido.

maior_numero= 0 
num = int(input("Digite um numero: "))
while num != 0:
    if num > maior_numero:
        maior_numero = num
    num = int(input("Digite um numero: "))
print("O maior numero inserido foi: ", maior_numero)

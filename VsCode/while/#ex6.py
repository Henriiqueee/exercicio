#6. Some todos os números pares de 1 a 100 e mostre o resultado.

soma = 0
for num in range(2, 101, 2):
    soma += num
print("A soma dos números pares de 1 a 100 é:", soma)
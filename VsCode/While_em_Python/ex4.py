#4. Solicite ao usuário que insira números. O programa deve continuar até que um número negativo seja inserido. No final, exiba o maior número informado.

maior_numero = None

while True:
    numero = float(input("Insira um número (ou um número negativo para sair): "))
    
    if numero < 0:
        break
    
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

if maior_numero is not None:
    print("O maior número informado foi:", maior_numero)
else:
    print("Nenhum número válido foi informado.")
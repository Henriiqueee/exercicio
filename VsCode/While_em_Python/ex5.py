#5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.

contador = 0
ultimo_numero = None

while True:
    numero = float(input("Insira um número: "))
    
    if numero == ultimo_numero:
        break
    
    ultimo_numero = numero
    contador += 1

print("Você inseriu", contador, "números.")
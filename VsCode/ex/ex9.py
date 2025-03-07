#9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos desejados. O programa deve calcular o valor total e permitir que o usuário finalize o pedido digitando 0.

produtos = {
    1: 10.00,  # Produto 1: R$10.00
    2: 15.50,  # Produto 2: R$15.50
    3: 20.00   # Produto 3: R$20.00
}

total = 0

while True:
    codigo = int(input("Digite o código do produto (ou 0 para finalizar): "))
    
    if codigo == 0:
        break
    
    if codigo in produtos:
        quantidade = int(input("Digite a quantidade desejada: "))
        total += produtos[codigo] * quantidade
    else:
        print("Código de produto inválido. Tente novamente.")

print("O valor total do seu pedido é: R$", total)
#8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos. A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba o troco. Após isso, o programa deve reiniciar para um novo cliente.

print("Bem-vindo ao sistema de caixa registradora!")

while True:
    total = 0

    while True:
        valor = float(input("Digite o valor do produto (ou 0 para finalizar a compra): "))
        if valor == 0:
            break
        total += valor

    print("O total da compra é: R$", total)

    valor_pago = float(input("Digite o valor pago pelo cliente: "))
    
    troco = valor_pago - total
    if troco < 0:
        print("Valor pago insuficiente. Tente novamente.")
        continue

    print("O troco é: R$", troco)

    if input("Deseja registrar uma nova compra? (s/n): ").lower() != 's':
        break

print("Obrigado por utilizar o sistema de caixa registradora!")
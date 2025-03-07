#10. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
#foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
#valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

faturamento_loja_A = 0
faturamento_loja_B = 54000

# Cadastrar 5 clientes
for i in range(5):
    nome_cliente = input(f"Digite o nome do cliente {i + 1}: ")
    valor_compra = float(input(f"Digite o valor da compra do cliente {nome_cliente}: "))
    faturamento_loja_A += valor_compra

# Verificar se o faturamento da loja A foi superior à loja B
if faturamento_loja_A > faturamento_loja_B:
    superacao = faturamento_loja_A - faturamento_loja_B
    print(f"O faturamento da loja A foi superior à loja B em {superacao:.2f}.")
else:
    print("O faturamento da loja A não superou o da loja B.")
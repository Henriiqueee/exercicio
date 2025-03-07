#15. Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500. A cada 100
#reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%.
#Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
#Faça um programa que exiba essa tabela de descontos no seguinte formato:
#Valordacompra – porcentagem de desconto – valor final

# Definindo os limites e as variáveis
valor_inicial = 500
valor_final = 1000  
incremento = 100

print("Valor da compra - Porcentagem de desconto - Valor final")
print("-------------------------------------------------------")

# Loop para calcular os descontos
for valor_compra in range(valor_inicial, valor_final + 1, incremento):
    if valor_compra > 500:
        # Calculando a porcentagem de desconto
        percentual_desconto = min((valor_compra - 500) // 100 + 1, 25)
    else:
        percentual_desconto = 0

    # Calculando o valor final após o desconto
    valor_com_desconto = valor_compra * (1 - percentual_desconto / 100)
    
    # Exibindo os resultados
    print(f"R${valor_compra:.2f} - {percentual_desconto}% - R${valor_com_desconto:.2f}")
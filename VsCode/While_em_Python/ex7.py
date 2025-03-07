#7. Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B com 200.000 habitantes e taxa de 1,5%. Determine quantos anos serão necessários para que a população do país A ultrapasse a população do país B.

populacao_A = 80000  
populacao_B = 200000 
taxa_crescimento_A = 0.03  
taxa_crescimento_B = 0.015  

anos = 0

while populacao_A <= populacao_B:
    populacao_A *= (1 + taxa_crescimento_A)
    populacao_B *= (1 + taxa_crescimento_B)
    anos += 1

print("Serão necessários", anos, "anos para que a população do país A ultrapasse a população do país B.")
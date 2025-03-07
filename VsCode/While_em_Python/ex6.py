#6. Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até que o usuário informe um valor válido.

nota = -1  

while nota < 0 or nota > 10:
    nota = float(input("Por favor, insira uma nota entre 0 e 10: "))
    
    if nota < 0 or nota > 10:
        print("Nota inválida. Tente novamente.")

print("Nota válida informada:", nota)

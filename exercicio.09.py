nota = int(input("digite uma nota"))
print("esse é o numero que voce digitou:", nota)

soma = int(input("Digite outro numero: "))
print("esse é o numero que voce digitou:", soma)

qtd = 0

soma += nota
qtd += 1

if qtd > 0:
    print("A média das notas é:", soma / qtd)
else:
    print("Nenhuma nota foi digitada.")
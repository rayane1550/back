palavra = input("Digite uma palavra ")

if palavra == palavra[::-1]:
    print(palavra, "é um palíndromo!")
else:
    print(palavra, "não é um palíndromo!")

valor = int(input("Digite o valor em reais: "))
for c in [100, 50, 20, 10, 5, 2, 1]:
    print(valor // c, "cédula(s) de R$", c)
    valor %= c
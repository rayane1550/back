numero = int(input("digite um numero"))
print("esse é o numero que voce digitou:", numero)
if numero <= 1:
    print("não é primo")
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print("não é primo")
            break
    else:
        print("é primo")
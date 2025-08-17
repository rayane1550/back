numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))
numero_3 = int(input("Digite um número: "))
numero_4 = int(input("Digite um número: "))
numero_5 = int(input("Digite um número: "))

print("Esses são os números digitados:", numero_1, numero_2, numero_3, numero_4, numero_5)

maior = menor = numero_1

if numero_2 > maior:
    maior = numero_2
elif numero_2 < menor:
    menor = numero_2

if numero_3 > maior:
    maior = numero_3
elif numero_3 < menor:
    menor = numero_3

if numero_4 > maior:
    maior = numero_4
elif numero_4 < menor:
    menor = numero_4

if numero_5 > maior:
    maior = numero_5
elif numero_5 < menor:
    menor = numero_5

print("O maior número digitado foi: " + str(maior))
print("O menor número digitado foi: " + str(menor))
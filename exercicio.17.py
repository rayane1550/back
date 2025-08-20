import random


tentativas = 0


while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    tentativas += 1
    soma = dado1 + dado2


    if soma == 7:
        print(f"Soma 7! Dados: {dado1} + {dado2}")
        break


print(f"Foram necessárias {tentativas} tentativas.")
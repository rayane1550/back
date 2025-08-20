import random

segredo = random.randint(1, 100)  # Número secreto entre 1 e 100
tentativas = 0

while True:
    palpite = int(input("Seu chute: "))
    tentativas += 1


    if palpite == segredo:
        print(f"Acertou! O número era {segredo}. Você conseguiu em {tentativas} tentativas 🎉")
        break
    elif palpite < segredo:
        print("É mais alto")
    else:
        print("É mais baixo")
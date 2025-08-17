positivos = 0

for i in range(1, 11):
    num = int(input(f"Digite o número {i}: "))
    if num > 0:
        positivos += 1

print(f"Você digitou {positivos} números positivos.")
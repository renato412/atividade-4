A = []
soma_quadrados = 0

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número inteiro: "))
    A.append(num)
    soma_quadrados += num ** 2

print(f"\nVetor A: {A}")
print(f"A soma dos quadrados dos elementos é: {soma_quadrados}")

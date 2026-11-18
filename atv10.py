vetor1 = []
vetor2 = []
vetor3 = []

print("--- Preenchendo o 1º Vetor ---")
for i in range(1, 11):
    num = int(input(f"Digite o {i}º elemento do vetor 1: "))
    vetor1.append(num)

print("\n--- Preenchendo o 2º Vetor ---")
for i in range(1, 11):
    num = int(input(f"Digite o {i}º elemento do vetor 2: "))
    vetor2.append(num)


for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(f"\nVetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor 3 (intercalado): {vetor3}")

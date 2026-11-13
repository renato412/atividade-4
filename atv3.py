notas = []

for i in range(1, 5):
    nota = float(input(f"digite a {i} nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas digitadas:", notas)
print(f"A média das notas é: {media:.2f}")
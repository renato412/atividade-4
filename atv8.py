idade = []
altura = []

for i in range(1,6):
    id = int(input(f"digite a {i} sua idade: "))
    al = float(input(f"digite a {i} sua altura: "))

    idade.append(id)
    altura.append(al)

print("\n--- Ordem Inversa ---")

for i in range(4, -1, -1):
    print(f"Idade: {idade[i]} | Altura: {altura[i]:.2f}")
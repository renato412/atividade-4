numeros = []
soma = 0
multiplicacao = 1

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)
    soma += num
    multiplicacao *= num

print("\nNúmeros digitados:", numeros)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
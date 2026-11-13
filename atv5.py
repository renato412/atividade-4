numero = []
impa = []
par = []

for i in range(1, 21):
    num = int(input(f"digite o {i} numero: "))
    if num % 2 == 0:
     par.append(num)

    else:
     impa.append(num)


print(f"total dos números é {num} ")
print(f"total de números par é {par}")
print(f"total de números impares é {impa}")
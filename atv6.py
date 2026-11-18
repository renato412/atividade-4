ALUNOS = 10
NOTAS = 4

medias = []
alunos_aprovados = 0

for i in range(ALUNOS):
    soma = 0.0
    for j in range(NOTAS):
        nota = float(input(f"Digite a nota {j + 1} do aluno {i + 1}: "))
        soma += nota

    media = soma / NOTAS
    medias.append(media)

    if media >= 7.0:
        alunos_aprovados += 1

print("\nMédias dos alunos:", [round(m, 2) for m in medias])
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

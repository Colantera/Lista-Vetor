# 8. Faca um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
# e imprima a media geral.

notas = [0] * 15
i = 0
soma = 0

while i < 15:
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas[i] = nota
    soma += nota
    i += 1

media = soma / 15

print(f"A média geral é: {media}")
# 7. Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor. Imprima
# o vetor, o maior elemento e a posicao que ele se encontra.
vetor = [0] * 10
i = 0

while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor[i] = numero
    i += 1

maior = vetor[0]
posicao = 0

i = 1
while i < 10:
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i
    i += 1

print("Vetor: ", vetor)
print(f"Maior vetor: {maior}")
print(f"Posição: {posicao}")
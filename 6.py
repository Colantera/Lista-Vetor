# 6. Faca um programa que receba do usuario um vetor com 10 posicoes. Em seguida devera
# ser impresso o maior e o menor elemento do vetor
vetor = [0] * 10
i = 0

while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor[i] = numero
    i += 1

maior = vetor[0]
menor = vetor[0]

i = 1
while i < 10:
    if vetor[i] > maior:
        maior = vetor[1]
    if vetor[i] < menor:
        menor = vetor[i]
    i += 1

print(f"O maior elemento do vetor é: {maior}")
print(f"O menor elemento do vetor é: {menor}")
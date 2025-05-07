# 5. Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui.
vetor = [0] * 10  
i = 0
contador_pares = 0

while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor[i] = numero
    i += 1

i = 0
while i < 10:
    if vetor[i] % 2 == 0:
        contador_pares += 1
    i += 1

print(f"{contador_pares} valores são pares.")
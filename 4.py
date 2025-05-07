# 4. Faca um programa que leia um vetor de 8 posicoes e, em seguida, leia tambem dois valores
# X e Y quaisquer correspondentes a duas posicoes no vetor. Ao final seu programa
# devera escrever a soma dos valores encontrados nas respectivas posicoes X e Y .

posi = [1, 2, 3, 4, 5, 6, 7, 8]

x = int(input("Digite uma posição de (0 a 7): "))
y = int(input("Digite uma posição de (0 a 7): "))

soma = posi[x] + posi[y]

print(f"X: {posi[x]}")
print(f"Y: {posi[y]}")
print(f"Soma: {soma}")
# 11. Fazer um programa para ler 5 valores e, em seguida, mostrar a posicao onde se encontram o maior e o menor valor.
valor = [0] * 5
i = 0

while i < 5:
    numero = int(input(f"Digite o {i+1}º número: "))
    valor[i] = numero
    i += 1

maior = valor[0]
menor = valor[0]
pos_maior = 0
pos_menor = 0

i = 1
while i < 5:
    if valor[i] > maior:
        maior = valor[i]
        pos_maior = i
    if valor[i] < menor:
        menor = valor[i]
        pos_menor = valor[i]
    i += 1

print("Valores:", valor)
print(f"Maior valor: {maior} na posição {pos_maior + 1}")
print(f"Menor valor: {menor} na posição {pos_menor + 1}")

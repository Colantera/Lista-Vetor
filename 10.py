# 10. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
# juntamente com o maior, o menor e a media dos valores.
valor = [0] * 5
soma = 0
i = 0

while i < 5:
    numero = int(input(f"Digite o {i+1}º número: "))
    valor[i] = numero
    soma += numero
    i += 1

media = soma / 5
maior = valor[0]
menor = valor[0]

i = 1
while i < 5:
    if valor[i] > maior:
        maior = valor[1]
    if valor[i] < menor:
        menor = valor[i]
    i += 1

print("Valores: ", valor)
print(f"O Maior número é: {maior}")
print(f"O Menor número é: {menor}")
print(f"A média é: {media}")
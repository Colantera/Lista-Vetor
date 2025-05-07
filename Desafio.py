# 1. Implemente um programa em Python para verificar quantos números
# uma aposta acertou na Mega Sena. O programa deve ler do teclado os 6 números apostados e comparar com os 6 números sorteados.
# Ao final, o programa deve exibir os números sorteados, números jogados e quantidade de acertos.
# Obs: Faça essa atividade usando apenas os conceitos de vetores, sem utilizar nenhuma funcionalidade de listas.
import random

aposta = [0] * 6
sorteio = [0] * 6

print("Digite os 6 números apostados:")
i = 0
while i < 6:
    numero = int(input(f"{i+1}º aposta:"))
    if numero < 1 or numero > 20:
        print("Número ínvalido! Escolha um número de 1 a 20.")
    elif numero in aposta[:i]:
        print("Número repetido! Digite outro.")
    else:
        aposta[i] = numero
        i += 1

i = 0
while i < 6:
    numero = random.randint(1,20)
    s = 0
    repedido = False
    while s < i:
        if sorteio[s] == numero:
            repedido = True
            break
        s += 1
    if not repedido:
        sorteio[i] = numero
        i += 1

acertos = 0
i = 0
while i < 6:
    s = 0
    while s < 6:
        if aposta[i] == sorteio[s]:
            acertos += 1
            break
        s += 1
    i += 1

print("\nNúmeros apostados:", aposta[0], aposta[1], aposta[2], aposta[3], aposta[4], aposta[5])
print("Números sorteados:", sorteio[0], sorteio[1], sorteio[2], sorteio[3], sorteio[4], sorteio[5])
print("Quantidade de acertos:", acertos)
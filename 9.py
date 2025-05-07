# 9. Faca um programa que preencha um vetor com 10 numeros reais, calcule e mostre a
# quantidade de numeros negativos e a soma dos numeros positivos desse vetor.
vetor = [0] * 10
negativos = 0
soma_positivos = 0
i = 0

while i < 10:
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor[i] = numero
    if numero < 0:
        negativos += 1
    else:
        soma_positivos += numero
    i += 1

print(f"Negativos: {negativos}")
print(f"Soma dos positivos: {soma_positivos}")
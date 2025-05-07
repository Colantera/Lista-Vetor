# 1. Fac¸a um programa que possua um vetor denominado A que armazene 6 n´umeros inteiros.
# O programa deve executar os seguintes passos:
# (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
# (b) Armazene em uma vari´avel inteira (simples) a soma entre os valores das posic¸ ˜oes
# A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
# (c) Modifique o vetor na posic¸ ˜ao 4, atribuindo a esta posic¸ ˜ao o valor 100.
# (d) Mostre na tela cada valor do vetor A, um em cada linha.

A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]
print("Soma: " + str(soma))

A[4] = 100

print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])
print(A[5])
#Formas de imprimir o número para o usuário em Python

print("Este é o capítulo 2 do livro")

A = 12
print(A)

B = 19
print(B)

print(A, B)

print("Valor de A =", A)

print("Valor de A = {0} e valor de B = {1}" .format(A, B))

print("=+"*40)

print(A, B, sep="-")
print(A, B, sep=";")
#utilização de separadores

print("Valor de A = {0:d} e valor de B = {1:d}" .format(A, B)) #d - número inteiro em base 10
print("A = {0:5d}".format(A)) #numero inteiro ocupando no mínimo 5 caracteres alinhado à direita
print("A = {0:f}".format(A)) #numero real, exibindo o padrão de 6 casas após a vírgula
print("A = {0:2f}".format(A)) #número real, 2 casas após a vírgula
print("A = {0:6.3f}".format(A)) #numero real, ocupando no mínimo 6 caracteres e exibindo 1 casa após a vírgula
print("qq{:7d}qq".format(A)) #número inteiro ocupando no minimo 7 caracteres à direita
print("qq{:<7d}qq".format(A)) #alinhamento a esquerda
print("qq{:^7d}qq".format(A)) #alinhamento centralizado
#formatação

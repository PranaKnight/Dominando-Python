# #Break and Continue
# X = 1
# while X != 0:
#     X = int(input("Digite um valor: "))
#     if X <= 0:
#         continue
#     P = int(input("Digite o primeiro termo: "))
#     R = int(input("Digite a razão: "))
#     cont = 0
#     Q = int(input("Digite o número de elementos da PA: "))
#     soma = 0
#     Termo = 1
#     while cont < Q:
#         soma +=P
#         print("Termo {0} da PA = {1}".format(Termo, P))
#         P += R
#         cont +=1
#         Termo +=1

#     print("Valor da soma = {}".format(soma))

# #Continue ==> Caso a condição seja satisfeita retorna pro cabeçalho do laço

# while True:
#     X = int(input("Digite um valor: "))
#     if X == 0:
#         break
#     #bloco de código

# # break ==> Quebra a execução do laço

N = int(input("Digite N: "))
i = 2
while i < N:
    R = N % i
    if R == 0:
        print("{} não é primo".format(N))
        break
    i += 1
else:
    print("{} é primo".format(N))
#Utilizando else junto com while
#Else só vai ser executado se o while tiver terminado normalmente

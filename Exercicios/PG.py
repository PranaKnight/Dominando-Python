#Continuação dos Exercícios de Fluxo

# P1 = int(input("Digite o primeiro termo da PG: "))
# R = int(input("Digite a razão da PG: "))
# Q = int(input("Digite o número de termos da PG: "))

# cont = 0
# sum = P1
# P = P1
# while cont < Q:
#     print(P)
#     print(sum)
#     P *=R
#     sum +=P
#     cont += 1

# print("Inicio do programa de números divisíveis por 5")

# Min = int(input("Digite o valor mínimo: "))
# Max = int(input("Digite o valor máximo: "))
# print("Min [{0}] e Max [{1}]".format(Min, Max))

# if Min > Max:
#     print("O valor minimo é maior que o máximo e serão invertidos\n")
#     Min, Max = Max, Min

# x = Min

# while x <= Max:
#     r = x % 5
#     if r == 0:
#         print(x)

#     x +=1


# print("Maior e Menor de uma sequencia")

# I = int(input("Digite o inteiro a ser comparado: "))
# Min = I
# Max = I
# while True:
#     R = float(input("Digite um número pra ser comparado ou 0 para encerrar: "))
    
#     if R <= I:
#         Min = R

#     elif R >= I:
#         Max = R

#     else:
#         break

#     print("Min = {0} e Max = {1}".format(Min, Max))


# print("Maior e Menor de uma sequencia")

# I = int(input("Digite o inteiro a ser comparado: "))
# Min = I
# Max = I
# while True:
#     R = float(input("Digite um número pra ser comparado ou 0 para encerrar: "))
    
#     if R < 0:
#         print("Esse valor é menor que 0")
#         continue
    
#     elif R <= I and R > 0:
#         Min = R

#     elif R >= I and R > 0:
#         Max = R

#     else:
#         break

#     print("Min = {0} e Max = {1}".format(Min, Max))


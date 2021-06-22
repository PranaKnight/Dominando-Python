#Exemplos de Loops

print("While com contador\n")

# cont = 1 #inicialização

# while cont <= 10: #condição
#     print(cont) #corpo
#     cont = cont + 1 #iteração
# print("=+"*40)
# #while

# X = 1
# while X != 0:
#     X = int(input("Digite o valor de X: "))
#     if X % 2 == 0:
#         print("{} é par".format(X))
#     else:
#         print("{} é impar".format(X))
#Par e impar
###################################################
# P = int(input("Digite o primeiro termo: "))
# R = int(input("Digite a razão: "))

# cont = 0
# while cont < 10:
#     print(P)
#     P = P + R
#     cont = cont + 
# #PA
#########################################################
# X = int(input("Digite o valor de X: "))
# soma = 0
# cont = 0
# while X != 0:
    
#     soma +=X
#     X = int(input("Digite o Valor de X: "))
#     cont +=1

# print("Total dos valores = {}".format(soma))
# print("Numero de valores digitados = {}".format(cont))
##############################################################
P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
cont = 0
Q = int(input("Digite o número de elementos da PA: "))
soma = 0
Termo = 1
while cont < Q:
    soma +=P
    print("Termo {0} da PA = {1}".format(Termo, P))
    P += R
    cont +=1
    Termo +=1

print("Valor da soma = {}".format(soma))
#PA_ex_1
#############################################################


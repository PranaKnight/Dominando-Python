#Continuação de Exercicios de Controle de Fluxo

Min = 9999999999999999999999999999999999999999999999999999999999
Max = -1
Q = 0
Soma = 0
Media = 0
while True:
    X = int(input("Digite um valor inteiro positivo ou menor igual a 0 para parar: "))
    
    if X <=0:
        Media = Soma/Q
        break
    
    Q += 1
    Soma += X
    if Min >= X and X > 0: 
        Min = X

    if Max <= X and X > 0:
        Max = X

print("Min = {0}, Max = {1}, Quantidade = {2}, Soma = {3} e Media = {4}".format(Min, Max, Q, Soma, Media ))
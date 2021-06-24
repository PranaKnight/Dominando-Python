#Numero de Fibonacci depois de Prim

Prim = int(input("Escolha o Prim: "))
N = int(input("Digite o numero de termos da sequencia: "))

F1 = 0
F2 = 1
cont = 0

while True:
#    print(F1)
    if F2 >= Prim:
        break
    t = F2
    F2 = F1 + F2
    F1 = t


while cont < N:
    print(F2)
    t = F2
    F2 = F1 + F2
    F1 = t
    cont += 1



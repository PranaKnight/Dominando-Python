#Condições compostas

A, B, C = 15, 9, 9

print(B==C or A < B and A < C)

print((B==C or A < B) and A < C)

#Prioridades de comparação (Primeiro 'not', depois and 'e' por fim 'or')

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

if A<= B and A<=C:
    if B<=C:
        print("Ordem crescente: {0}, {1}, {2}".format(A,B,C))
    else:
        print("Ordem crescente: {0}, {1}, {2}".format(A,C,B))

elif B <= A and B <= C:
    if A <= C:
        print("Ordem crescente: {0}, {1}, {2}".format(B,A,C))
    else:
        print("Ordem crescente: {0}, {1}, {2}".format(B,C,A))

else:
    if A<=B:
        print("Ordem crescente: {0}, {1}, {2}".format(C,A,B))
    
    else:
        print("Ordem crescente: {0}, {1}, {2}".format(C,B,A))

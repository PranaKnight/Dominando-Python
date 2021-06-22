#Demonstração de identificadores apontando para mesmo objeto na memória

A = 15
B = A

print(id(A))
print(id(B))
#Ambos possuem o mesmo id

L = [12, 24, 36]
print(id(L))
M = L
print(id(M))
M[0] = 0
print(M)
print(L)
#Nesse caso ao identificador M é atribuido L fazendo M ter o mesmo objeto
#Caso seja mudado um dado em M em L também o será.

print("=+"*45)
L = [12, 24, 36]
print(id(L))
M = [12, 24, 36]
print(id(M))
M[0] = 0
print(M)
print(L)

#Porém, caso a M seja atribuido os mesmos valores de L ao invés de L em sí
#Cria-se um novo objeto e mudando-se M, L não é alterado.

#TUDO ISSO OCORRE PQ LISTAS SÃO MUTÁVEIS
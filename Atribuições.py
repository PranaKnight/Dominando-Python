#Formas de atribuir uma identidade a um objeto.

A = B = C = 1

print(id(A))
print(id(B))
print(id(C))
#Todos identificadores apontam pro mesmo objeto
print("=+"*40)
A, B, C = 1, 2, 3

print(id(A))
print(id(B))
print(id(C))
#Mudam os identificadores do objeto
print("=+"*40)
X, Y, Z = 0, -10, 10
print(X, Y)

X, Y = Y, X 
print(X, Y)
#Inversão de objetos

print(X, Y, Z)
X, Y, Z = Y, Z, X
print(X, Y, Z)
#Inversão de objetos
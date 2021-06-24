#Controle de Fluxo

# A, B = 0, -3
# print(A>B)

# X = 3.7
# print(X <= 10.0)

# A, B = 9, 16
# print(A - B >= 0)

# A, B, N = 2, 4, 10
# print(A * B < N)

# A, B, C = 3, 9, 5
# print(10 * A >= B * C)

# A, B, C = 3, 6, 5
# print(10*A >= B * C)

# N = 7
# print(N % 2 == 0)
# N = 8
# print(N % 2 == 0)

# T = "MORANGO"
# print(T == "BANANA")

# print(T > "BANANA")

# A, B, C = 10, 15, 4
# print(A < B and A < C)

# A, B, C = 10, 15, 4
# print(A < B or A < C)

# A, B, C = 1, 9, 0
# print(A >= 0 and B == C)

# A, B, C = 1, 9, 9
# print(A >= 0 and B == C)

# A, B, C = 1, 9, 0
# print(A >= 0 or B == C)

# A, B, C = 1, 9, 9
# print(A >= 0 or B == C)

# A, B, C = 0, 0, 0
# print(B != 0 and A != C)

# A, B, C = 0, 0, 25 
# print(B != 0 and A != C)

# A, B, C = 0, 0, 0
# print(B != 0 or A != C)

# A, B, C = 0, 0, 25
# print(B != 0 or A != C)


A, B, C = 10, 15, 4
print(A < B and A < C or C != 0)

A, B, C = 10, 15, 4
print(A < B and (A < C or C!=0))

A, B, C = 1, 9, 0
print(not(A >= 0 and B == C))

A, B, C = 1, 9, 9
print(not(A >= 0) and not (B == C))

A, B, C = 1, 9, 0
print((A >= 0 or B == C) and B > A)

A, B, C = -2, 0, 2
print(not (A <= B) or C > B)

A, B, C = -2, 0, 2
print(not(A <= 0 or C > B))

A, B, C = 0, 1, 0
print(A == 0 and B != 0 and C == 0)

A, B, C = 5, 0, 0
print(A == 0 and B != 0 and C == 0)

A, B, C = 5, 0, 0
print(A == 0 or B != 0 or C == 0) 

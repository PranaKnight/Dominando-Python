#Sequencia de exercícios 3

from math import sqrt

Salario = 14.25
H = 163
Hext = 20

Total = Salario*H + 2*Salario*Hext
print("Salário Mensal = {0:.2f}".format(Total))

A, B, C = 4, 5, 1
x1, y1, x2, y2 = 1, 1, 4, 5

R = (A+B)/2
print(R)
print("=+"*40)

x = (-B+sqrt(B**2-(4*A*C)))/2
print(x)
print("=+"*40)

R = (3*A+2*B)/(A+B)
print(R)
print("=+"*40)

z = 7.6*A-B**1.7
print(z)
print("=+"*40)

d = sqrt((x1-x2)**2+(y1-y2)**2)
print(d)

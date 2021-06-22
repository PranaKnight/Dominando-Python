#Sequencia4
from math import sqrt

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

d = sqrt((x1-x2)**2+(y1-y2)**2)
print("Distancia = {0:.3f}".format(d))

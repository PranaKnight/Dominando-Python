#Funções simples

from math import sqrt
from math import trunc
from math import floor
from math import ceil

x = 9
r = sqrt(x)
print(r)

y = -5
r = abs(y)
print(r)
#fornece o módulo do valor
z = 10.9
r = int(z)
print(r)
#transforma o tipo do objeto em int
r = float(r)
print(r)
#transforma o tipo do objeto em float
w = 10.9878
r = round(w, 2)
print (r)
#Arredonda com 2 números após a vírgula
r = trunc(w)
print (r)
#Trunca o número e equivale ao int()

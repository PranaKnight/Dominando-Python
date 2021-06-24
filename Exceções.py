#Tratamento de exceções

from random import randint

N = int(input("Digite N: "))
Total = 0
i = 1
while i <= N:
    x = randint(1, 50)
    print("Valor {} gerado = {}".format(i, x))

    Total +=x
    i += 1

print("\nSoma dos valores gerados = {}".format(Total))

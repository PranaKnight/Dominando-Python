#Sequencia5

prod1 = input("Digite o nome do produto: ")
qnt1 = int(input("Digite a quantidade desse produto: "))
valor1 = float(input("Digite o valor do item: "))
rec1 = qnt1*valor1
print("=+"*40)
prod2 = input("Digite o nome do proximo produto: ")
qnt2 = int(input("Digite a quantidade desse produto: "))
valor2 = float(input("Digite o valor do item: "))
rec2 = qnt2*valor2
print("=+"*40)
prod3 = input("Digite o nome do produto: ")
qnt3 = int(input("Digite a quantidade desse produto: "))
valor3 = float(input("Digite o valor do produto: "))
rec3 = qnt3*valor3

total = rec1 + rec2 + rec3
print("Receita obtida com {0} = R$ {1:.2f}\n".format(prod1, rec1))
print("Receita obtida com {0} = R$ {1:.2f}\n".format(prod2, rec2))
print("Receita obtida com {0} =R$ {1:.2f}\n".format(prod3, rec3))
print("Receita total foi = {0:.2f}".format(total))
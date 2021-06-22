#Exercícios de Python Básicos

Fixos = 500.00
Vendas = 12398.00
Comissao = 6/100

Fat = Fixos + Vendas*Comissao

print("Faturamento do mês foi R${0:.2f}".format(Fat))
print("=+"*40)
#Exercício 1

Fixos = 500.00
Vendas = float(input("Digite as vendas do mês: "))
Comissao = 6/100
Fat = Fixos + Vendas*Comissao
print("Faturamento Mensal = {0:.2f}".format(Fat))
# Exercício 2
#Pega o peso e nome de um lutador e define sua categoria

Nome = input("Digite o nome do lutador: ")
Peso = float(input("Digite o peso do Lutador: "))


if Peso < 65 :
    print("Nome fornecido: {}".format(Nome))
    print("Peso fornecido: {}".format(Peso))
    print("O lutador {0} pesa {1} e se enquadra na categoria Pena".format(Nome, Peso))

elif Peso >= 65 and Peso < 72:
    print("Nome fornecido: {}".format(Nome))
    print("Peso fornecido: {}".format(Peso))
    print("O lutador {0} pesa {1} e se enquadra na categoria Leve".format(Nome, Peso))
 
elif Peso >= 72 and Peso < 79:
    print("Nome fornecido: {}".format(Nome))
    print("Peso fornecido: {}".format(Peso))
    print("O lutador {0} pesa {1} e se enquadra na categoria Ligeiro".format(Nome, Peso))

elif Peso >= 79 and Peso < 86:
    print("Nome fornecido: {}".format(Nome))
    print("Peso fornecido: {}".format(Peso))
    print("O lutador {0} pesa {1} e se enquadra na categoria Meio-medio".format(Nome, Peso))

elif Peso >= 86 and Peso < 93:
    print("Nome fornecido: {}".format(Nome))
    print("Peso fornecido: {}".format(Peso))
    print("O lutador {0} pesa {1} e se enquadra na categoria Médio".format(Nome, Peso))

elif Peso >=93 and Peso < 100:
    print("Nome fornecido: {}".format(Nome))
    print("Peso fornecido: {}".format(Peso))
    print("O lutador {0} pesa {1} e se enquadra na categoria Meio-Pesado".format(Nome, Peso))

elif Peso > 100:
    print("Nome fornecido: {}".format(Nome))
    print("Peso fornecido: {}".format(Peso))
    print("O lutador {0} pesa {1} e se enquadra na categoria Pesado".format(Nome, Peso))

else:
    print("Insira algo que faça sentido")
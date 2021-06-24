#Verificar se um numero é divisivel por 2 e 3

while True:
    
    X = int(input("Digite um numero inteiro: "))

    if X == 0:
        break

    r = X % 2
    y = X % 3

    if r == 0 and y == 0:
        print(X)



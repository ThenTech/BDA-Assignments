def divisor_de(x):
    for i in range(2, x):
        if x%i == 0:
            return True

def es_primo(x):
    if not divisor_de(x):
        return True

def  primos_de(x):
    for i in range(2, x):
        if es_primo(i):
            print(i, end=' ')
    print()

x = int(input("i: "))
primos_de(x)
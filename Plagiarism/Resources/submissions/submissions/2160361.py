frase = input("frase: ")
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto:
    contador = 0
    for i in range(0, len(frase)):
        if (letra == frase[i]):
            contador = contador + 1
    print(letra, contador, sep=": ")




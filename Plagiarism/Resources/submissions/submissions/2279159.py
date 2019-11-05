frase = input('frase: ')
simbolos ='!@#$%^&*()_+=-{}[]:;?/><.<\,'

while frase != ' ' and frase != simbolos:
    contador = 0
    for i in range(0, len(frase)):
        if frase[i] == ' ' and frase[i - 1] != ' ':
            contador += 1

        if frase[-1] == ' ':
            contador = contador - 1

    palabras = contador+1



    print(palabras)
    break


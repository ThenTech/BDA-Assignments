def filtro(frase):
    minu = frase.lower()
    rta = ""
    for letra in minu:
        if 'a' <= letra and letra <= 'z':
            rta += letra
    return rta



def is_palindrome(palabra):
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[len(palabra) - i - 1]:
            return False
    return True



def is_palindrome_sentence(frase):
    return is_palindrome(filtro(frase))



frase = input("frase: ")

if is_palindrome_sentence(frase):
    print("True")
else:
    print("False")

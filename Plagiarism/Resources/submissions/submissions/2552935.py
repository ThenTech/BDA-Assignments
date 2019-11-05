frase = input("frase: ")
frase = frase.lower()

def is_letter(frase):
    nueva = ''
    for letra in frase:
        if 'a' <= letra <= 'z':
            nueva += letra
    return nueva


def palindroma(frase):
    frase = is_letter(frase)
    if frase[ ::-1] == frase:
        return True

if palindroma(frase):
    print("True")
else:
    print("False")
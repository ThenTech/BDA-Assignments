frase1=input("frase1: ")
frase2=input("frase2: ")

alfabeto='abcdefghijklmnopqrstuvwxyz'

esAnagrama=True

for letra in alfabeto:
    contador1=0
    for i in range(0, len(frase1)):
        if letra == frase1[i]:
            contador1 +=1


    contador2=0
    for j in range(0, len(frase2)):
        if letra==frase2[j]:
            contador2 +=1

    esAnagrama = esAnagrama and contador1==contador2

if(esAnagrama):
    print(frase1, "and ", frase2, "are anagrams")

else:
    print(frase1, "and ", frase2, "are not anagrams")

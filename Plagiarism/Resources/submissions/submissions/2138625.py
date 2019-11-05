string = input('Geef een woord in')
string_lijst = list(string)
alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for el in alfabet:
    teller = 0
    for waarde in string_lijst:
        if el == waarde:
            teller = teller + 1
    print(el, teller, sep=": ")
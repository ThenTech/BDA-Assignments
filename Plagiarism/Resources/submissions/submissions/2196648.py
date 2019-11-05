zin = input("Geef string: ")
niet = ''',?;.:/"<>[]^!'“”’ '''
getal = "0123456789"
teller = 0
for i in zin:
    if i in niet or i in getal:
        if teller != 0:
            print("", teller)
            teller = 0
        elif i == zin[len(zin)-1]:
            if i in niet:
                continue
            else:
                print("", teller)
        else:
            continue
    else:
        print(i, end="")
        teller += 1
print("", teller)
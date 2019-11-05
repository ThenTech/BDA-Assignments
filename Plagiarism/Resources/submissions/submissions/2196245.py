zin = input("Geef string: ")
niet = ''',?;.:/"<>[]^!'“”’ '''
teller = 0
woord = ""
for i in zin:
    if i in niet:
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
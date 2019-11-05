zin = input("Geef string: ")
niet = ''',?;.:/"<>[]^!'“”’ '''
teller = 0
woord = ""
for i in zin:
    if i in niet:
        if teller != 0:
            print("", teller)
            teller = 0
        else:
            continue
    else:
        print(i, end="")
        teller += 1
print("", teller)
zin = input("Geef een zin.")
zin1 = input("Geef een andere zin")
alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
counter1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = 0
for j in alfabet:
    for i in range(0, len(zin)):
        if j == zin[i]:
            counter[x] += 1
        else:
            continue
    x += 1
x = 0
for j in alfabet:
    for i in range(0, len(zin1)):
        if j == zin1[i]:
            counter1[x] += 1
        else:
            continue
    x += 1
for h in range(0,24):
    if counter[h] == counter1[h]:
        if h == 23:
            print(zin, "and", zin1, "are anagrams")
            break
        else:
            continue
    else:
        print(zin, "and", zin1, "are not anagrams")
        break